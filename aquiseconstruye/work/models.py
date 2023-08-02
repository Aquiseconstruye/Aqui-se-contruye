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


WORK_CHOICES = ((1,'Carretera'),
                    (2,'Alcantarilla'),
                    (3,'Tubería'),
                    (4,'Parque'),
                    (5,'Competidor'),
                    (6,'Agua'),
                    (7,'Edificio'),
                    (8,'Policía'),
                    (9,'Hospital'),
                    (10,'Cultura'),
                    (11,'Escuela'),
                    (12,'Familia'),
                    (13,'Industria'),
                    (14,'Femenino'),
                    (15,'Masculino'),
                    (16,'Animales'),
                    (17,'Deporte'),)


TRAFFIC_FILTER_CHOICES = (('Semáforo rojo','Rojo'),
                    ('Semáforo amarillo','Amarillo'),
                    ('Semáforo verde','Verde'))
                    

class Work(models.Model):
    no_work =  models.CharField(max_length=300,default='test', verbose_name=('Numero de la obra'))
    no_contract =  models.CharField(max_length=300, default='test', verbose_name=('Numero de contrato'))
    name = models.CharField(max_length=300, verbose_name=('Nombre de la obra'))
    alias = models.CharField(max_length=100,default='test', verbose_name=('Alias de la obra'))
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
    credits_image = models.CharField(max_length=300,null=True, blank=True, verbose_name=('Creditos de las imagenes'))
    link_image = models.URLField(null=True, blank=True,verbose_name="Link de los creditos")
    price = models.FloatField(blank=True, null=True, verbose_name=('precio'))
    money_used = models.FloatField(blank=True, null=True, verbose_name=('Dinero utilizado'))
    budget = models.FloatField(blank=True, null=True, verbose_name=('presupuesto'))
    day = models.IntegerField(blank=True, null=True, verbose_name=('Dias En los que concluyo'))
    start_of_work = models.DateTimeField(blank=True, null=True, verbose_name=('inicio de obra'))
    signing_of_contract = models.DateTimeField(blank=True, null=True, verbose_name=('Firma de contrato'))
    term = models.DateTimeField(blank=True, null=True, verbose_name=('plazo'))
    conclution = models.DateTimeField(blank=True, null=True, verbose_name=('dia que se termino'))
    traffic_light = models.IntegerField(default=2, choices=TRAFFIC_LIGHT_CHOICES, verbose_name=('semaforo'))
    traffic_light_filter = models.CharField(max_length=20, blank=True, null=True, choices=TRAFFIC_FILTER_CHOICES, verbose_name=('semaforo filtro'))
    type_work = models.IntegerField(default=1, choices=WORK_CHOICES, verbose_name=('Tipo de obra'))
    img_traffic_light = models.ForeignKey(TrafficLight, related_name="semaforo", blank=True, null=True, on_delete=models.CASCADE)
    official = models.CharField(max_length=200,blank=True, null=True, verbose_name=('funcionario'))
    dependence = models.CharField(max_length=500, blank=True, null=True,verbose_name=('dependencia'))
    constructor = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    constructor1 = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    constructor2 = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    constructor3 = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    constructor4 = models.CharField(max_length=200, blank=True, null=True, verbose_name=('constructoras'))
    entrepreneur = models.CharField(max_length=200, blank=True, null=True, verbose_name=('Empresario'))
    legal_representative = models.CharField(max_length=200, blank=True, null=True, verbose_name=('REPRESENTANTE LEGAL'))
    order_gob = models.CharField(max_length=200, blank=True, null=True, verbose_name=('orden de gobierno'))
    contracts = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts1 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts2 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts3 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts4 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts5 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts6 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts7 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts8 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts9 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts10 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts11 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts12 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts13 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts14 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts15 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts16 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts17 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts18 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts19 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts20 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts21 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts22 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts23 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts24 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts25 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts26 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts27 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts28 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts29 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts30 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts31 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts32 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts33 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts34 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts35 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts36 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts37 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts38 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts39 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts40 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts41 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts42 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts43 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts44 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts45 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts46 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts47 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts48 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts49 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    contracts50 = models.FileField(upload_to='contracts', blank=True, null=True, verbose_name=('contratos y licitaciones'))
    link = models.URLField(null=True, blank=True,verbose_name="Link")
    link2 = models.URLField(null=True, blank=True,verbose_name="Link2")
    link3 = models.URLField(null=True, blank=True,verbose_name="Link3")
    link4 = models.URLField(null=True, blank=True,verbose_name="Link4")
    link5 = models.URLField(null=True, blank=True,verbose_name="Link5")
    completate = models.BooleanField(default=False, blank=True, null=True, verbose_name=('obra completada'))
    newsletter = models.FileField(blank=True, null=True, upload_to='newsletter', verbose_name='fuentes')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.alias

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.alias)
        return super().save(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.alias)
        if self.pk is not None and self.completate != self.__class__.objects.get(pk=self.pk).completate and self.completate:
            # si completate ha cambiado de False a True, actualiza la fecha de término
            self.term2 = datetime.now().date()
        elif self.pk is not None and self.completate != self.__class__.objects.get(pk=self.pk).completate and not self.completate:
            # si completate ha cambiado de True a False, reinicia la fecha de término
            self.term2 = None
        super().save(*args, **kwargs)   


