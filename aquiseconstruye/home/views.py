from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import folium
from work.models import Work

from django.urls import reverse
from django.views.generic import ListView
from geopy.geocoders import Nominatim
import folium
from django.template.loader import render_to_string
from django.http import JsonResponse
from ipware import get_client_ip
from datetime import datetime, timedelta

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import io
import base64

import datetime


class HomeView(ListView):
    models = Work
    template_name = 'home.html'
    queryset = Work.objects.all()
    context_object_name = 'work'

    
    

    def get_context_data(self, **kwargs):
        work_obj = Work.objects.all()
        mexico = folium.Map(width='100%', height='100%', location=[24.17912575174476, -103.11313995196282], zoom_start=6)
        

        for work in work_obj:
           

            url_absoluta = reverse('obra:obra', args=[work.slug])

           
            html_amarillo="""
                <center><h2>{}</h2></center>
                    <br>
                    <div><img src="https://i.ibb.co/zsTPVdL/monedas.png" alt="logo" width=60 height=70 ></div>
                    <center><h3 style="margin-top:-50px">${}0</h3></center>
                    <br>
                    <h3 >Ver mas</h3>
                    <center><a href='{}' target="_blank"><img class="arow"style="margin-top:-50px" width=60 height=70 src="https://i.ibb.co/D72djKd/sketched-double-arrow-pointing-left-and-right.png"></a></center>
                """.format(work.name, work.price, url_absoluta)
               
                
                
      

            html_rojo="""
                    <center><h2>{}</h2></center>
                    <br>
                    <div><img src="https://i.ibb.co/zsTPVdL/monedas.png" alt="logo" width=60 height=70 ></div>
                    <center><h3 style="margin-top:-50px">${}0</h3></center>
                    <br>
                    <h3 >Ver mas</h3>
                    <center><a href='{}' target="_blank"><img class="arow"style="margin-top:-50px" width=60 height=70 src="https://i.ibb.co/D72djKd/sketched-double-arrow-pointing-left-and-right.png"></a></center>
                """.format(work.name, work.price, url_absoluta)

            html_verde="""
                <center><h2>{}</h2></center>
                    <br>
                    <div><img src="https://i.ibb.co/zsTPVdL/monedas.png" alt="logo" width=60 height=70 ></div>
                    <center><h3 style="margin-top:-50px">${}0</h3></center>
                    <br>
                    <h3 >Ver mas</h3>
                    <center><a href='{}' target="_blank"><img class="arow"style="margin-top:-50px" width=60 height=70 src="https://i.ibb.co/D72djKd/sketched-double-arrow-pointing-left-and-right.png"></a></center>
                """.format(work.name, work.price, url_absoluta)
           
            popup_amarillo = folium.Popup(folium.Html(html_amarillo, script=True), max_width=450,min_width=450)
            popup_rojo = folium.Popup(folium.Html(html_rojo, script=True), max_width=450,min_width=450)
            popup_verde = folium.Popup(folium.Html(html_verde, script=True), max_width=450,min_width=450)

            latitude = work.latitude
            longitude = work.longitude
            work_address = work.address
            if work.traffic_light == 1:
                folium.Marker([latitude, longitude],
                            popup=popup_rojo,
                          icon=folium.Icon(color='red', icon='close', prefix='fa')
                          ).add_to(mexico)
            elif work.traffic_light == 2:
                folium.Marker([latitude, longitude],
                            popup=popup_amarillo,
                          icon=folium.Icon(color='orange', icon='exclamation-triangle', prefix='fa')
                          ).add_to(mexico)
            else:
                folium.Marker([latitude, longitude],
                            popup=popup_verde,
                          icon=folium.Icon(color='green', icon='check', prefix='fa')
                          ).add_to(mexico)
                

            
    
  

        mexico = mexico._repr_html_()
        context = {
            'map': mexico,
        }

        return context
