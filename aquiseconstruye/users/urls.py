from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
	path('register/', SignupFormView.as_view(), name='register'),
	path('ingresar/', LoginView.as_view(), name='login'),
    path('salir/', LogoutView.as_view(), name='logout'),
	path('editar-perfil/', ProfileFormView.as_view(), name='profile_form'),
	path('perfil/', ProfileView.as_view(), name='profile'),

		
]