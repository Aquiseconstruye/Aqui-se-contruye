from django.db import models

# Create your models here.
class Whoweare(models.Model):
    who_we_are = models.TextField(blank=True, null=True, verbose_name=('quienes somos'))
    image = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))

class IntroAquiSeConstruye(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name=('quienes somos'))
    intro = models.TextField(blank=True, null=True, verbose_name=('quienes somos'))


class Metodologic(models.Model):
    metodologic = models.TextField(blank=True, null=True,verbose_name=('Metodo'))