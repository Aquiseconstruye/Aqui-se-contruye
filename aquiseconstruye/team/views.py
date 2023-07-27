from django.shortcuts import render
from team.models import Whoweare, IntroAquiSeConstruye
from django.views import View
# Create your views here.


class TeamView(View):
    def get(self, request, *args, **kwargs):
        team = Whoweare.objects.all()
        return render(request, "team.html", locals())
    
class IntroView(View):
    def get(self, request, *args, **kwargs):
        intro = IntroAquiSeConstruye.objects.all()
        return render(request, "intro.html", locals())