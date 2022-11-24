from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder
# Create your views here.

def home(request):
    if request.method == 'POST' :
        form =SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Votre addresse est invalide')
    #create map objects
    m = folium.Map(location = [19, -12], zoom_start=2)
    #Get HTMl Representation of Map Object
    folium.Marker([lat,lng], tooltip = 'Click for more', popup=country).add_to(m)
    m = m._repr_html_()
    context = {
        'm':m,
        'form':form,
    }
    return render(request,'home.html',context)