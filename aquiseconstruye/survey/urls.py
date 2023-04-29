from django.urls import path
from survey.views import SurveyFormView, GraficasView


urlpatterns = [
	
        path('encuesta/<int:obra_id>/', SurveyFormView.as_view(), name='encuesta'),
        path('Graficas', GraficasView.as_view(), name='graficas'),
	
]