from django.urls import path
from .views import ObrasView, ObraDetailView, download_files

app_name = 'obra'

urlpatterns = [
    path('obras/', ObrasView.as_view(), name='obras'),
    path('obra/<str:slug>/', ObraDetailView.as_view(), name='obra'),
    path('obra/<slug:slug>/download/', download_files, name='download_files'),
]