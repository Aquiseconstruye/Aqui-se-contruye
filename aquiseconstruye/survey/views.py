from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import SurveyForm
from .models import Survey
from work.models import Work

@login_required
def survey_create_view(request, work_id):
    obra = get_object_or_404(Work, id=work_id)
    form = SurveyForm(user=request.user, obra=obra)
    if request.method == 'POST':
        form = SurveyForm(request.POST, user=request.user, obra=obra)
        if form.is_valid():
            form.save()
            return redirect('survey_thankyou')
    return render(request, 'survey_create.html', {'form': form, 'obra': obra})

# Create your views here.
