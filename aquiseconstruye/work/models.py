from django.db import models
from django.utils.text import slugify
from datetime import datetime
# Create your models here.
class TrafficLight(models.Model):
    color = models.CharField(max_length=300)
    trafficlight = models.ImageField(upload_to='trafficlight', blank=True, null=True, verbose_name=('semaforo'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


TRAFFIC_LIGHT_CHOICES = ((1,'Rojo'),
                    (2,'Amarillo'),
                    (3,'Verde'))
                    

class Work(models.Model):
    name = models.CharField(max_length=300, verbose_name=('Nombre de la obra'))
    slug = models.CharField(max_length=100, blank=True, null=True, unique=True, db_index=True)
    address = models.CharField(max_length=500, null=True, default='test')
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    image = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image1 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image2 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image3 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image4 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image5 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image6 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image7 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image8 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image9 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image10 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image11 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image12 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image13 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image14 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image15 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image16 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image17 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image18 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image19 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    image20 = models.ImageField(upload_to='galery/%Y-%m-%d/', blank=True, null=True, verbose_name=('galeria'))
    price = models.FloatField(blank=True, null=True, verbose_name=('precio'))
    budget = models.FloatField(blank=True, null=True, verbose_name=('presupuesto'))
    term = models.DateTimeField(blank=True, null=True, verbose_name=('plazo'))
    term2 = models.DateTimeField(blank=True, null=True, verbose_name=('días restantes'))
    start_of_work = models.DateTimeField(blank=True, null=True, verbose_name=('inicio de obra'))
    traffic_light = models.IntegerField(default=2, choices=TRAFFIC_LIGHT_CHOICES, verbose_name=('semaforo'))
    img_traffic_light = models.ForeignKey(TrafficLight, related_name="semaforo", blank=True, null=True, on_delete=models.CASCADE)
    official = models.CharField(max_length=200,blank=True, null=True, verbose_name=('funcionario'))
    dependence = models.CharField(max_length=500, blank=True, null=True,verbose_name=('dependencia'))
    constructor = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    constructor1 = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    constructor2 = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    constructor3 = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    constructor4 = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    contracts = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts1 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts2 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts3 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts4 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts5 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts6 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts7 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts8 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts9 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts10 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts11 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts12 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts13 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts14 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts15 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts16 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts17 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts18 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts19 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts20 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts21 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts22 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts23 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts24 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts25 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts26 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts27 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts28 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts29 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts30 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts31 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts32 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts33 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts34 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts35 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts36 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts37 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts38 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts39 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts40 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts41 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts42 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts43 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts44 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts45 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts46 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts47 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts48 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts49 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts50 = models.FileField(upload_to='contracts/%Y-%m-%d/', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    completate = models.BooleanField(default=False, blank=True, null=True, verbose_name=('obra completada'))
    newsletter = models.FileField(blank=True, null=True, upload_to='newsletter', verbose_name='fuentes')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.pk is not None and self.completate != self.__class__.objects.get(pk=self.pk).completate and self.completate:
            # si completate ha cambiado de False a True, actualiza la fecha de término
            self.term2 = datetime.now().date()
        elif self.pk is not None and self.completate != self.__class__.objects.get(pk=self.pk).completate and not self.completate:
            # si completate ha cambiado de True a False, reinicia la fecha de término
            self.term2 = None
        super().save(*args, **kwargs)   


