from django.urls import path
from home.views import HomeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', HomeView.as_view(template_name="home.html")),
    path('', HomeView.as_view(), name='home'),
	
]