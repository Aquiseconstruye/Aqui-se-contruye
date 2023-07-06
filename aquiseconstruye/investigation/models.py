from django.db import models
from datetime import datetime
# Create your models here.


class   Investigation(models.Model):
    title = models.CharField(max_length=300, verbose_name=('Titulo'))
    image = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image1 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image2 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image3 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    image4 = models.ImageField(upload_to='inv', blank=True, null=True, verbose_name=('galeria'))
    introduccion = models.TextField(max_length=1500, verbose_name='introducción')
    seccion1 = models.TextField(max_length=3500, default='“I couldn’t see the Black Panther living on a side street in New York,” Lee explained in a Marvel interview. ”I loved the idea of a superhero that lives in Africa.”', verbose_name='seccion1')
    seccion2 = models.TextField(max_length=3500, default='It’s that background that makes T’Challa, aka the Black Panther, unique; he’s not only black, he’s African. His ties to the continent and culture grant him a rich and complex mythology that his American counterparts do not have.', verbose_name='seccion2')
    seccion3 = models.TextField(max_length=3500, default='Afrocentrism defines every part of his character, beginning with his name. There’s the literal definition. Black panthers, the great cats native to Africa, serve as a motif for T’Challa’s superhero persona. Then there’s the fictional definition', verbose_name='seccion3')
    seccion4 = models.TextField(max_length=3500, default='The Black Panther is a title given to each chieftain of the Panther Clan of Wakanda, the nation that T’Challa rules.<br><br> In the new Black Panther feature film, Afrocentrism and Afrofuturism – the interpretation of African traditions into', verbose_name='seccion4')
    seccion5 = models.TextField(max_length=3500, default='their futuristic possibilities – combine to create an aesthetic never before seen in the Marvel Cinematic Universe.<br><br> With the Black Panther in theaters, we examine how Afrocentrism and Afrofuturism inform Wakanda, its leader, and it citizens.', verbose_name='seccion5')
    by = models.CharField(max_length=500,default='Aqui se construye',verbose_name=('Escrito por')  )
    appointment = models.TextField(max_length=600,default='I couldn’t see the Black Panther living on a side street in New York. I loved the idea of a superhero that lives in Africa', verbose_name=('Cita'))
    name_appointment = models.TextField(max_length=600,default='Stan Lee, Black Panther creator', verbose_name=('Nombre de la cita'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)