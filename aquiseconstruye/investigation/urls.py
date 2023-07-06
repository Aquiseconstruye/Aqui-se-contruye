from django.urls import path
from investigation.views import InvestigationView

urlpatterns = [
    path('investigacion', InvestigationView.as_view(), name='investigacion'),
]