# Generated by Django 4.1.1 on 2023-07-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='appointment',
            field=models.TextField(default='I couldn’t see the Black Panther living on a side street in New York. I loved the idea of a superhero that lives in Africa', max_length=600, verbose_name='Cita'),
        ),
        migrations.AddField(
            model_name='investigation',
            name='by',
            field=models.CharField(default='Aqui se construye', max_length=500, verbose_name='Escrito por'),
        ),
        migrations.AddField(
            model_name='investigation',
            name='name_appointment',
            field=models.TextField(default='Stan Lee, Black Panther creator', max_length=600, verbose_name='Nombre de la cita'),
        ),
    ]