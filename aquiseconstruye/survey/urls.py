from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	
        path('crear_encuesta/<int:obra_id>/', survey_create_view, name='crear_encuesta'),

		
]