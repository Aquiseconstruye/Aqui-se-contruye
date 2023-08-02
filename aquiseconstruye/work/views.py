
from django.shortcuts import render,redirect,reverse
from .models import Work
import locale
from django.views import View
from django.views import generic
from django.views.generic.detail import DetailView
from .filters import ObrasFilter 
import pandas as pd
import plotly
import plotly.express as px
from django_pandas.io import read_frame
import plotly.offline as opy
from django.shortcuts import render
from django.utils import timezone
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from django.utils import timezone
from datetime import datetime, date
from django.db import models
import pandas as pd
import os
import zipfile
from users.models import Relationship
from django.conf import settings
from django.http import HttpResponse
from django.views.generic import DetailView
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import get_object_or_404
import locale

# Create your views here.

def download_files(request, slug):
    obra = get_object_or_404(Work, slug=slug)
    response = HttpResponse(content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{obra.slug}.zip"'

    # Define la ruta absoluta al directorio de archivos
    files_dir = os.path.join(settings.MEDIA_ROOT)

    # Crea un archivo ZIP que contendrá todos los archivos asociados a la obra
    zip_file = zipfile.ZipFile(response, 'w')

    # Procesar los campos pasados por la URL
    fields = request.GET.getlist('fields')

    if not fields:
        # Si no se especifican campos, incluir todos los campos de archivos
        fields = [f.name for f in obra._meta.fields if isinstance(f, models.FileField)]

    for field_name in fields:
        field = getattr(obra, field_name)
        if field:
            field_files_dir = os.path.join(files_dir, field.field.upload_to)
            for filename in os.listdir(field_files_dir):
                file_path = os.path.join(field_files_dir, filename)
                zip_file.write(file_path, os.path.basename(file_path))  # Usar os.path.basename para obtener solo el nombre del archivo

    # Cierra el archivo ZIP
    zip_file.close()

    return response



class ObrasView(View):
    @property
    def obras(self):
        return self.kwargs["obras"]

    def get(self, request, *args, **kwargs):
        obras =  Work.objects.all()
     
        obras_filter = ObrasFilter(request.GET, queryset=obras)
        return render(request, 'obras.html', {'filter': obras_filter})


class ObraDetailView(DetailView):
    model = Work
    template_name = 'obra.html'
    context_object_name = 'obra'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtener la obra a través del slug en la URL
        obra = Work.objects.filter(slug=self.kwargs.get('slug')).first()

        is_following = False
        if self.request.user.is_authenticated:
            is_following = Relationship.objects.filter(user=self.request.user, work=obra).exists()

        # Obtener información de fechas
        today = date.today()
        completion_date = obra.term.date() if obra.term else None
        now = timezone.now().date()
        start_date = obra.start_of_work.date() if obra.start_of_work else obra.created_at.date()
        completion_date = obra.term.date() if obra.term else None
        conclution_date = obra.conclution.date() if obra.conclution else None

        # Calcular días pasados, días restantes y días de atraso
        if completion_date and conclution_date:
            days_passed = (conclution_date - start_date).days
            dias_restantes = (completion_date - now).days if now <= completion_date else 0
            dias_atraso = (conclution_date - obra.term.date()).days if conclution_date > obra.term.date() else 0
        elif completion_date and not conclution_date:
            days_passed = (now - start_date).days
            dias_restantes = (completion_date - now).days if now <= completion_date else 0
            dias_atraso = 0  # No hay atraso si no hay fecha de conclusión
        else:
            days_passed = (now - start_date).days
            dias_restantes = (completion_date - now).days if completion_date and now <= completion_date else None
            dias_atraso = 0  # No hay atraso si no hay fecha de plazo ni fecha de conclusión

        # Calcular el porcentaje completado
        duration = (completion_date - start_date).days if completion_date else None
        porcentaje_completado = (days_passed / duration) * 100 if duration else 0

        # Calcular el color de la barra de progreso
        if obra.term and conclution_date:
            total_days = (completion_date - start_date).days
            completed_percentage = (days_passed / total_days) * 100

            if completed_percentage >= 95:
                color = 'red'
            elif completed_percentage >= 75:
                color = 'yellow'
            else:
                color = 'green'
        elif obra.term and dias_restantes is not None:
            if dias_restantes <= -30:
                color = 'red'
            elif dias_restantes <= -20:
                color = 'yellow'
            else:
                color = 'green'
        else:
            if days_passed < 10:
                color = 'green'
            elif days_passed < 20:
                color = 'yellow'
            else:
                color = 'red'

        context['dias_pasados'] = days_passed
        context['dias_restantes'] = dias_restantes
        context['dias_atraso'] = dias_atraso
        context['porcentaje_completado'] = porcentaje_completado
        context['color'] = color



        print("dias_restantes",dias_restantes)
        print("days_passed",days_passed)
        print("completion_date",completion_date )
        print("completion_date-start_date",completion_date-start_date)
        print("color",color)

        # Define los datos de la gráfica
        if dias_restantes is not None:
            x = [dias_restantes]
            x_label = 'Días Restantes'
        else:
            x = [days_passed]
            x_label = 'Días Transcurridos'

        data = [
            go.Bar(
                x=x,
                y=[obra.alias],
                orientation='h',
                marker=dict(color=color)
            )
        ]

        # Define el diseño de la gráfica
        layout = go.Layout(
            title='',
            xaxis=dict(
                title=x_label,
                range=[0, 365]
            ),
            yaxis=dict(
                title=''
            ),
        )

        # Crea la figura de la gráfica
        fig = go.Figure(data=data, layout=layout)

        # Convierte la figura de la gráfica en un objeto HTML y lo almacena en el contexto
        div = opy.plot(fig, auto_open=False, output_type='div')
        context['graph'] = div

         # Lista de campos para la descarga
        download_fields = [
            'contracts', 'contracts1', 'contracts2', 'contracts3', 'contracts4', 'contracts5', 'contracts6', 'contracts7', 'contracts8', 'contracts9', 'contracts10',
            'contracts11', 'contracts12', 'contracts13', 'contracts14', 'contracts15', 'contracts16', 'contracts17', 'contracts18', 'contracts19', 'contracts20',
            'contracts21', 'contracts22', 'contracts23', 'contracts24', 'contracts25', 'contracts26', 'contracts27', 'contracts28', 'contracts29', 'contracts30',
            'contracts31', 'contracts32', 'contracts33', 'contracts34', 'contracts35', 'contracts36', 'contracts37', 'contracts38', 'contracts39', 'contracts40',
            'contracts41', 'contracts42', 'contracts43', 'contracts44', 'contracts45', 'contracts46', 'contracts47', 'contracts48', 'contracts49', 'contracts50',
            
            # Añade todos los demás campos necesarios
        ]

        # Formatear el campo price con comas como separadores de miles
        if obra.price:
            formatted_price = locale.format_string("%0.2f", obra.price, grouping=True)
        else:
            formatted_price = None

        # Agregar el campo formateado al contexto
        context['formatted_price'] = formatted_price

        context['download_fields'] = download_fields

        context['is_following'] = is_following

        return context
