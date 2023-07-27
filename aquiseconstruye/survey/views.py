from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import SurveyForm
from .models import Survey
from work.models import Work
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib import messages
import plotly.graph_objs as go
import pandas as pd
import plotly
import plotly.express as px
from plotly.subplots import make_subplots

class SurveyFormView(View):
    @property
    def id(self):
        return self.kwargs.get('survey')
    
    def get(self, request, *args, **kwargs):
        obra_id = request.GET.get('obra')
        obra = None
        if obra_id:
            try:
                obra = Work.objects.get(id=obra_id)
            except Work.DoesNotExist:
                pass
        form = SurveyForm(initial={'obra': obra, 'user': request.user})
        return render(request, 'survey_create.html', {'form': form})
    
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        obra_id = kwargs.get('obra_id')  # aquí actualiza la clave para que sea consistente
        obra = get_object_or_404(Work, id=obra_id)
        if self.id:
            survey = Survey.objects.get(id=self.id)
            form = SurveyForm(request.POST, request.FILES, instance=survey)
        else:
            form = SurveyForm(request.POST, request.FILES, initial={'obra': obra, 'user': request.user})
        
        if form.is_valid():
            survey = form.save(commit=False)
            survey.obra = obra
            survey.user = request.user
            survey.save()
            return render(request, 'survey_thankyou.html', locals())
        else:   
            messages.error(request,('No se ha registrado'))
        return render(request, 'survey_create.html', locals())
    

class GraficasView(View):

    def get(self, request, *args, **kwargs):

        # Seleccionar todos los registros de la tabla Survey
        surveys = Survey.objects.all()

        # Convertir los datos del QuerySet en un DataFrame de pandas
        df = pd.DataFrame.from_records(
            surveys.values(
                "obra__alias",
                "survey",
            )
        ).rename(
            columns={
                "obra__alias": "obra",
                "survey": "tipo_encuesta",
            }
        )

        # Mapeo de los tipos de encuesta
        tipo_encuesta_map = {
            1: "Afecta mi translado",
            2: "Afecta mi patrimonio",
            3: "Afecta mis labores domesticos",
            4: "Otro"
        }
        df["tipo_encuesta"] = df["tipo_encuesta"].map(tipo_encuesta_map)

        # Pivoteo de los datos para obtener un DataFrame donde cada columna represente un tipo de encuesta
        df_pivoted = df.pivot_table(
            index="obra",
            columns="tipo_encuesta",
            aggfunc=len,
            fill_value=0
        )

        # Suma de encuestas por cada tipo de encuesta por cada obra
        df_pivoted["total"] = df_pivoted.sum(axis=1)

        # Creación de la gráfica de barras apiladas
        fig = px.bar(
            df_pivoted,
            x=df_pivoted.index,
            y=[col for col in df_pivoted.columns if col != "total"],
            title="Encuestas por obra",
            labels={
                "x": "Obra",
                "value": "Cantidad de encuestas",
                "variable": "Tipo de encuesta"
            },
            barmode="stack",
            color_discrete_sequence=["#FFBF00", "#1C1C1C", "#fff", "#FE8E00"]
        )

        # Ajustes del layout de la gráfica
        fig.update_layout(
           
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            title='<b>Encuestas por obra</b>',
            height=600,
            barmode='stack',
            legend=dict(
                orientation="h",
                yanchor="top",
                y=1.1,
                xanchor="center",
                x=0.5
            ))
        
        fig.update_xaxes(showticklabels=False, zeroline=False)
    

        encuesta = fig.to_html(config={"displayModeBar": False})


        # Convertir los datos del QuerySet en un DataFrame de pandas para los órdenes de gobierno
        df_ordenes = pd.DataFrame.from_records(
            surveys.values(
                "obra__order_gob",
            )
        ).rename(
            columns={
                "obra__order_gob": 'Orden de gobierno',
            }
        )

        # Contar la cantidad de obras por cada orden de gobierno
        df_ordenes_grouped = df_ordenes.groupby('Orden de gobierno').size().reset_index(name='Cantidad de obras')

        # Calcular el porcentaje de obras para cada orden de gobierno
        total_obras = len(df_ordenes)
        df_ordenes_grouped['Porcentaje de obras'] = df_ordenes_grouped['Cantidad de obras'] / total_obras * 100

        # Creación de la gráfica de pastel para órdenes de gobierno
        fig_ordenes = px.pie(
            df_ordenes_grouped,
            names='Orden de gobierno',
            values='Porcentaje de obras',
            title='Porcentaje de obras por Orden de gobierno',
            labels={
                'Orden de gobierno': 'Orden de gobierno',
                'Porcentaje de obras': 'Porcentaje',
            },
        )
        # Ajustes del layout de la gráfica
        fig_ordenes.update_layout(
            
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            title='<b>Orden de gobierno</b>',
            height=600,
            barmode='stack',
            legend=dict(
                orientation="h",
                yanchor="top",
                y=1.1,
                xanchor="center",
                x=0.5
            ))

        orden = fig_ordenes.to_html(config={"displayModeBar": False})


        df_constructoras = pd.DataFrame.from_records(
            surveys.values(
            "obra__alias",
                "obra__constructor",
            )
        ).rename(
            columns={
                "obra__alias": "obra",
                "obra__constructor": 'constructora',
            }
        )
        

        # Contar cuántas veces aparece cada constructora en el DataFrame
        constructoras_count = df_constructoras['constructora'].value_counts().reset_index()
        constructoras_count.columns = ['Constructora', 'Cantidad de obras']

        # Agrupar por constructora y sumar la cantidad de obras
        constructoras_sum_obras = constructoras_count.groupby('Constructora')['Cantidad de obras'].sum().reset_index()

        # Crear la gráfica de barras
        fig_constructoras = px.bar(
            constructoras_sum_obras,
            x='Constructora',
            y='Cantidad de obras',
            title='Cantidad de obras por constructora',
            labels={
                'Constructora': 'Constructora',
                'Cantidad de obras': 'Cantidad de obras',
            },
        )
        # Ajustes del layout de la gráfica
        fig_constructoras.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            title='<b>Constructoras</b>',
            height=600,
            barmode='stack',
            legend=dict(
                orientation="h",
                yanchor="top",
                y=1.1,
                xanchor="center",
                x=0.5
            ))

        constructoras = fig_constructoras.to_html(config={"displayModeBar": False})





        return render(request, 'graficas.html', locals())

