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


class HomeView(ListView):
    models = Work
    template_name = 'home.html'
    queryset = Work.objects.all()
    context_object_name = 'work'

    
    

    def get_context_data(self, **kwargs):
        work_obj = Work.objects.all()
        investigation = Investigation.objects.all()

        mapbox_access_token = settings.MAPBOX_ACCESS_TOKEN

        fig = go.Figure()

        for work in work_obj:
            color = ""
            if work.traffic_light == 1:
                color = "red"
            elif work.traffic_light == 3:
                color = "green"
            elif work.traffic_light == 2:
                color = "yellow"
            else:
                color = "blue"
            
            symbol=""
            if work.type_work == 1:
                symbol = "park"
            elif work.type_work == 2:
                symbol = "harbor"
            elif work.type_work == 3:
                symbol = "bridge"
            elif work.type_work == 4:
                symbol = "bus"
            elif work.type_work == 5:
                symbol = "monument"
            elif work.type_work == 6:
                symbol = "wetland"
            
            

            fig.add_trace(go.Scattermapbox(
                lat=[work.latitude],
                lon=[work.longitude],
                mode='markers',
                marker=go.scattermapbox.Marker(
                    size=10,
                    color=color,  # Asigna el color correspondiente según el campo "traffic_light"
                    symbol= symbol
                ),
                text=[work.name],
            ))

        fig.update_layout(
            hovermode='closest',
            margin=dict(t=30, l=0, r=0, b=0),
            mapbox=dict(
                accesstoken=mapbox_access_token,
                bearing=0,
                center=go.layout.mapbox.Center(
                    lat=25.54389,
                    lon=-103.41898
                ),
                pitch=0,
                zoom=10
            ),
        )

        # Genera el código HTML del mapa
        map_html = plot(fig, output_type='div')

        context = {
            'map_html': map_html, 'investigation':investigation
        }

        return context
