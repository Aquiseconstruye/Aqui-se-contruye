from django.db import models
from datetime import datetime
from django.utils.text import slugify
# Create your models here.
class   InvestigationHome(models.Model):
    title = models.CharField(max_length=300, verbose_name=('Titulo'))
    introduccion = models.TextField(max_length=1500, verbose_name='introducción')

class   Investigation(models.Model):
    slug = models.CharField(max_length=100, blank=True, null=True, unique=True, db_index=True)
    title = models.CharField(max_length=300, verbose_name=('Titulo'))
    image = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image1 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image2 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image3 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image4 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image5 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image6 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    introduccion = models.TextField(max_length=1500, verbose_name='introducción')
    seccion1 = models.TextField(max_length=6500, blank=True, null=True, verbose_name='seccion1')
    seccion2 = models.TextField(max_length=6500, blank=True, null=True, verbose_name='seccion2')
    seccion3 = models.TextField(max_length=6500, blank=True, null=True, verbose_name='seccion3')
    seccion4 = models.TextField(max_length=6500, blank=True, null=True, verbose_name='seccion4')
    seccion5 = models.TextField(max_length=6500, blank=True, null=True, verbose_name='seccion5')
    seccion6 = models.TextField(max_length=6500, blank=True, null=True ,verbose_name='seccion6')
    by = models.CharField(max_length=800,default='Aqui se construye',verbose_name=('Escrito por')  )
    appointment = models.TextField(max_length=600, blank=True, null=True, verbose_name=('Cita'))
    name_appointment = models.TextField(max_length=600, blank=True, null=True, verbose_name=('Nombre de la cita'))
    credit = models.TextField(max_length=5500, blank=True, null=True, verbose_name=('Creditos'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)