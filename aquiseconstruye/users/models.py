
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
from django.contrib.postgres.fields import ArrayField
from datetime import datetime
from rest_framework.authtoken.models import Token


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


class User(AbstractUser):
    username = models.CharField(max_length=140, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=140, blank=True, null=True)
    last_name = models.CharField(max_length=140, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    genders = models.IntegerField(default=1, choices=GENDER_CHOICES, verbose_name=('Genero'))
    institute = models.IntegerField(default=1, choices=INSTITUTE_CHOICES, verbose_name=('Instituto u Organizacion'))
    degree_of_studies = models.IntegerField(default=1, choices=DEGREE_OF_STUDIES_CHOICES, verbose_name=('Grado de estudios'))
    birthday = models.DateField(blank=True, null=True, verbose_name=('fecha de nacimiento'))
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)