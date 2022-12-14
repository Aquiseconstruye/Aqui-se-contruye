
from django.shortcuts import render,redirect,reverse
from .models import Work
import locale
from django.views import View
from django.views import generic
from django.views.generic.detail import DetailView
# Create your views here.
class ObrasView(View):
    @property
    def regidurias(self):
        return self.kwargs["obras"]

    def get(self, request, *args, **kwargs):
        obras =  Work.objects.all()
        print(obras)
        return render(request, 'obras.html')


class ObraDetailView(DetailView):

    model = Work
    template_name = 'obra.html'
    context_object_name = 'obra'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Work.objects.filter(slug=self.kwargs.get('slug'))

        return context
