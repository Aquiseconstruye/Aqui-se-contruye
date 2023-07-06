from django.urls import path
from team.views import TeamView

urlpatterns = [
    path('nosotros', TeamView.as_view(), name='nosotros'),
]