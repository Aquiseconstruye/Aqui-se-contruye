# Generated by Django 4.1.1 on 2023-07-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0020_work_traffic_light_filter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='type_work',
            field=models.IntegerField(choices=[(1, 'Carretera'), (2, 'Alcantarilla'), (3, 'Tubería'), (4, 'Parque'), (5, 'Competidor'), (6, 'Agua'), (7, 'Edificio'), (8, 'Policía'), (9, 'Hospital'), (10, 'Cultura'), (11, 'Escuela'), (12, 'Familia'), (13, 'Industria'), (14, 'Femenino'), (15, 'Masculino'), (16, 'Animales'), (17, 'Deporte')], default=1, verbose_name='Tipo de obra'),
        ),
    ]