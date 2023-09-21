# Generated by Django 4.1.1 on 2023-09-20 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigation', '0005_investigationhome'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigation',
            name='seccion6',
            field=models.TextField(blank=True, max_length=3500, null=True, verbose_name='seccion6'),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='appointment',
            field=models.TextField(blank=True, max_length=600, null=True, verbose_name='Cita'),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='name_appointment',
            field=models.TextField(blank=True, max_length=600, null=True, verbose_name='Nombre de la cita'),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='seccion1',
            field=models.TextField(blank=True, max_length=3500, null=True, verbose_name='seccion1'),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='seccion2',
            field=models.TextField(blank=True, max_length=3500, null=True, verbose_name='seccion2'),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='seccion3',
            field=models.TextField(blank=True, max_length=3500, null=True, verbose_name='seccion3'),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='seccion4',
            field=models.TextField(blank=True, max_length=3500, null=True, verbose_name='seccion4'),
        ),
        migrations.AlterField(
            model_name='investigation',
            name='seccion5',
            field=models.TextField(blank=True, max_length=3500, null=True, verbose_name='seccion5'),
        ),
    ]
