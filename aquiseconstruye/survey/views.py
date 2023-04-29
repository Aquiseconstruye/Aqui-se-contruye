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
                "obra__name",
                "survey",
            )
        ).rename(
            columns={
                "obra__name": "obra",
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
            title={
                'font_size': 24,
                'xanchor': 'center',
                'x': 0.5
            },
            legend_title_text="Tipo de encuesta",
        )

        encuesta = fig.to_html()


        df_precio = pd.DataFrame.from_records(
            surveys.values(
                "obra__name",
                "obra__price",
                "obra__budget",
            )
        ).rename(
            columns={
                "obra__name": 'Obra',
                "obra__price": 'Precio total',
                "obra__budget": 'Presupuesto asignado',
            }
        )

        # Calcular la diferencia entre el precio y el presupuesto
        df_precio['Diferencia'] = df_precio['Presupuesto asignado'] - df_precio['Precio total']

        # Crear una figura con dos subplots, uno para el precio y otro para la diferencia
        fig_presupuesto = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

        # Añadir el gráfico de precio al primer subplot
        fig_presupuesto.add_trace(
            go.Bar(
                x=df_precio['Obra'],
                y=df_precio['Precio total'],
                name='Precio total',
                marker_color='#FFBF00',
            ),
            row=1,
            col=1,
        )

        # Añadir el gráfico de presupuesto al primer subplot
        fig_presupuesto.add_trace(
            go.Bar(
                x=df_precio['Obra'],
                y=df_precio['Presupuesto asignado'],
                name='Presupuesto asignado',
                marker_color='#1C1C1C',
            ),
            row=1,
            col=1,
        )

        # Añadir el gráfico de diferencia al segundo subplot
        fig_presupuesto.add_trace(
            go.Bar(
                x=df_precio['Obra'],
                y=df_precio['Diferencia'],
                name='Diferencia',
                marker_color=df_precio['Diferencia'].apply(lambda x: 'red' if x < 0 else 'green'),
            ),
            row=2,
            col=1,
        )

        # Actualizar el diseño de la figura
        fig_presupuesto.update_layout(
            title='Comparación de precio y presupuesto por obra',
            xaxis_title='Obra',
            yaxis_title='Cantidad',
            height=600,
            barmode='group',
        )

        presupuesto = fig_presupuesto.to_html()





        return render(request, 'graficas.html', locals())

