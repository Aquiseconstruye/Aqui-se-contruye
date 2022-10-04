from django.db import models

# Create your models here.

TRAFFIC_LIGHT_CHOICES = ((1,'Rojo'),
                    (2,'Amarillo'),
                    (3,'Verde'))
                    


class Work(models.Model):
    name = models.CharField(max_length=300, verbose_name=_('Nombre de la obra'))
    slug = models.CharField(max_length=100, blank=True, null=True, unique=True, db_index=True)
    image = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image1 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image2 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image3 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image4 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image5 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image6 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image7 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image8 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image9 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image10 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image11 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image12 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image13 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image14 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image15 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image16 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image17 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image18 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image19 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    image20 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=_('galeria'))
    price = models.FloatField(blank=True, null=True, verbose_name=_('precio'))
    traffic_light = models.IntegerField(default=2, choices=TRAFFIC_LIGHT_CHOICES, verbose_name=_('semaforo'))
    official = models.CharField(max_length=200, verbose_name=_('funcionario'))
    dependence = models.CharField(max_length=500, verbose_name=_('dependencia'))
    constructor = models.CharField( verbose_name=_('constructoras'))
    contracts = models.ImageField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=_('contratos y licitaciones'))