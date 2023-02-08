from django.forms import ModelForm, Form
from .models import User


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'avatar','type_gender','birthday')