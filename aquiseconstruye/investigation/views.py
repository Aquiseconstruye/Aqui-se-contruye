from django.shortcuts import render
from investigation.models import Investigation
from django.views import View
# Create your views here.




class InvestigationView(View):
    def get(self, request, *args, **kwargs):
        investigation = Investigation.objects.all()
        return render(request, "inves.html", locals())