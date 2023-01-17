import folium
from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import folium
from work.models import Work


class HomeView(ListView):
    models = Work
    template_name = 'home.html'
    queryset = Work.objects.all()
    context_object_name = 'work'


    

    def get_context_data(self, **kwargs):
        work_obj = Work.objects.all()
        mexico = folium.Map(width='100%', height='100%', location=[24.17912575174476, -103.11313995196282], zoom_start=6)
        print(work_obj)

        
        

        for work in work_obj:
            print(work.name)
            html_amarillo="""
                <center><h2>"""+work.name+"""</h2></center>
                <br>
                <div><img src=https://i.ibb.co/zsTPVdL/monedas.png alt="logo" width=60 height=70 ></span>
                <center><h3 style="margin-top:-50px">$"""+str(work.price)+"""0</h3></center></span></div>
                <br>
                <br>
                <br>
                <img src=https://i.ibb.co/cLpxYmw/Amarillo.png alt="logo" width=50 height=50 ></div>
                

                
            """

            html_rojo="""
                <center><h2>"""+work.name+"""</h2></center>
                <br>
                <div><img src=https://i.ibb.co/zsTPVdL/monedas.png alt="logo" width=60 height=70 ></span>
                <center><h3 style="margin-top:-50px">$"""+str(work.price)+"""0</h3></center></span></div>
                <br>
                <br>
                <br>
                <div><img src=https://i.ibb.co/XxBXwnL/rojo.png alt="logo" width=50 height=50 ></div>
                
                
            """

            html_verde="""
                <center><h2>"""+work.name+"""</h2></center>
                <br>
                <div><img src=https://i.ibb.co/zsTPVdL/monedas.png alt="logo" width=60 height=70 ></span>
                <center><h3 style="margin-top:-50px">$"""+str(work.price)+"""0</h3></center></span></div>
                <br>
                <br>
                <br>
                <div><img src=https://i.ibb.co/6HNLSRb/Sin-ti-tulo-2.png alt="logo" width=50 height=50 ></div>

                
            """
           
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
                

            
    
  

        mexico = mexico._repr_html_()
        context = {
            'map': mexico,
        }

        return context


