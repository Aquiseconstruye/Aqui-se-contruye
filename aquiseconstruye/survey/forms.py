from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    obra = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Survey
        fields = ['survey', 'other', 'obra']

    def __init__(self, user=None, obra=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'] = forms.ModelChoiceField(
            queryset=User.objects.filter(id=user.id),
            widget=forms.HiddenInput()
        )
        self.fields['obra'].initial = obra.name if obra else None