# Generated by Django 4.1.1 on 2023-07-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0019_work_conclution'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='traffic_light_filter',
            field=models.CharField(blank=True, choices=[('Semáforo rojo', 'Rojo'), ('Semáforo amarillo', 'Amarillo'), ('Semáforo verde', 'Verde')], max_length=20, null=True, verbose_name='semaforo filtro'),
        ),
    ]
