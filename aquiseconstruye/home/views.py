from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import folium
from work.models import Work
from django.conf import settings
from django.urls import reverse
from django.views.generic import ListView
from geopy.geocoders import Nominatim
import folium
from django.template.loader import render_to_string
from django.http import JsonResponse
from ipware import get_client_ip
from datetime import datetime, timedelta
import plotly.graph_objects as go
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64
from plotly.offline import plot
import datetime
from investigation.models import *
from team.models import *


class HomeView(ListView):
    models = Work
    template_name = 'home.html'
    queryset = Work.objects.all()
    context_object_name = 'work'

    
    

    def get_context_data(self, **kwargs):
        works = Work.objects.all()  # Cambiar 'ubicaciones' por 'works'
        investigation = InvestigationHome.objects.all()
        intro = IntroAquiSeConstruye.objects.all()
        metodologic = Metodologic.objects.all()


        context = {
            'investigation': investigation,
            'intro': intro,
            'metodologic': metodologic,
            'works': works,  # Cambiar 'ubicaciones' por 'works'
        }

        return context
