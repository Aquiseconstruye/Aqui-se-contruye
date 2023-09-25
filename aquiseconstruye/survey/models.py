from django.db import models
from users.models import User
from work.models import Work
# Create your models here.



SURVEY_CHOICES = ((1,'Afecta mi traslado'),
                    (2,'Afecta mi patrimonio'),
                    (3,'Afecta mis labores domésticas'),
                    (4,'Otro'))



class Survey(models.Model):
    survey = models.IntegerField(default=1, choices=SURVEY_CHOICES, verbose_name=('encuesta'))
    other = models.TextField(blank=True, null=True, verbose_name=('Otra'))
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True, verbose_name=('Usuario'))
    obra = models.ForeignKey(Work,on_delete=models.CASCADE, blank=True, null=True, verbose_name=('Obra'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)