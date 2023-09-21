from django.shortcuts import render
from investigation.models import Investigation, InvestigationHome
from django.views import View
from django.views.generic.detail import DetailView
# Create your views here.



class InvestigationView(View):
    @property
    def obras(self):
        return self.kwargs["investigations"]
    def get(self, request, *args, **kwargs):
        investigations = Investigation.objects.all()
        return render(request, 'investigatons.html', {'investigations': investigations})


class InvestigationDetailView(DetailView):
    model = Investigation
    template_name = 'inves.html'
    context_object_name = 'investigation'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        investigation = Investigation.objects.filter(slug=self.kwargs.get('slug')).first()
        return context
    