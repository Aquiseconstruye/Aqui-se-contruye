
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime



INSTITUTE_CHOICES = ((1,'Instituto'),
                    (2,'Organisación'),
                    (3,'Ningunio'))


DEGREE_OF_STUDIES_CHOICES = ((1,'Primaria'),
                    (2,'Secundaria'),
                    (3,'Preparatoria'),
                    (4,'Universidad'),
					(5,'Maestria'),
					(6,'Postgrado'))

GENDER_CHOICES = ((1,'Femenino'),
                    (2,'Masculino'),
                    (3,'Prefiero no decirlo'))



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='user-icon.png')
	genders = models.IntegerField(default=1, choices=GENDER_CHOICES, verbose_name=('Genero'))
	institute = models.IntegerField(default=1, choices=INSTITUTE_CHOICES, verbose_name=('Instituto u Organizacion'))
	name = models.CharField(max_length=300, verbose_name=('Nombre'))
	degree_of_studies = models.IntegerField(default=1, choices=DEGREE_OF_STUDIES_CHOICES, verbose_name=('Grado de estudios'))
	birthday = models.DateField(blank=True, null=True, verbose_name=('fecha de nacimiento'))
	




class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'



class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]