from django.urls import path
from .views import ObrasView,ObraDetailView#, RegidorView

app_name = 'obra'

urlpatterns = [
   
    path('obras/',ObrasView.as_view(), name='obras'),
    path('obra/<str:slug>/',ObraDetailView.as_view(), name='obra')
    
    ]