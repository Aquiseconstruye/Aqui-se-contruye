from django.urls import path
from investigation.views import InvestigationView,InvestigationDetailView


urlpatterns = [
    path('investigationes', InvestigationView.as_view(), name='investigationes'),
    path('investigation/<str:slug>/', InvestigationDetailView.as_view(), name='investigacion_detalle'),
]