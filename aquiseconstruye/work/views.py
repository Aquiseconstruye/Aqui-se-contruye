
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



# Create your views here.
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
        now = timezone.now().date()
        start_date = obra.start_of_work.date() if obra.start_of_work else obra.created_at.date()
        completion_date = obra.term.date() if obra.term else now

        # Calcular duración y días restantes
        duration = (completion_date - start_date).days
        days_passed = (now - start_date).days
        dias_restantes = (completion_date - now).days if obra.term else 0
        print(dias_restantes)
        print(days_passed)

        # Calcular color de la gráfica
        if obra.term:
            if dias_restantes < 0:
                color = 'gray'
            elif dias_restantes < 20:
                color = 'red'
            elif dias_restantes < 50:
                color = 'yellow'
            else:
                color = 'green'
        else:
            if days_passed < 40:
                color = 'green'
            elif days_passed < 70:
                color = 'yellow'
            else:
                color = 'red'

        context['duracion'] = duration
        context['dias_pasados'] = days_passed
        context['dias_restantes'] = dias_restantes
        context['color'] = color

        # Define los datos de la gráfica
        data = [go.Bar(            x=[dias_restantes if obra.term2 else days_passed],
            y=[obra.name],
            orientation='h',
            marker=dict(color=color)
            )]

        # Define el diseño de la gráfica
        layout = go.Layout(
            title='',
            xaxis=dict(
                title='Días Restantes' if obra.term else 'Días Transcurridos',
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

        context['is_following'] = is_following

        return context

    def download_files(self, fields=None):
        obra = self.get_object()
        response = HttpResponse(content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{obra.slug}.zip"'

        # Define la ruta absoluta al directorio de archivos
        files_dir = os.path.join(settings.MEDIA_ROOT, str(obra.pk))

        # Crea un archivo ZIP que contendrá todos los archivos asociados a la obra
        zip_file = zipfile.ZipFile(response, 'w')

        if not fields:
            # Si no se especifican campos, incluir todos los campos de archivos
            fields = [f.name for f in obra._meta.fields if isinstance(f, models.FileField)]

        for field_name in fields:
            field = getattr(obra, field_name)
            if field:
                field_files_dir = os.path.join(files_dir, field.field.upload_to)
                for filename in os.listdir(field_files_dir):
                    file_path = os.path.join(field_files_dir, filename)
                    zip_file.write(file_path, filename)

        # Cierra el archivo ZIP
        zip_file.close()

        return response
