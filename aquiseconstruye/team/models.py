from django.db import models

# Create your models here.
class Whoweare(models.Model):
    who_we_are = models.TextField(blank=True, null=True, verbose_name=('quienes somos'))