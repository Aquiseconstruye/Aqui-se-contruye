# Generated by Django 4.1.1 on 2023-05-13 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_work_link_work_link2_work_link3_work_link4_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='no_contract',
            field=models.CharField(default='test', max_length=300, verbose_name='Numero de contrato'),
        ),
        migrations.AddField(
            model_name='work',
            name='no_work',
            field=models.CharField(default='test', max_length=300, verbose_name='Numero de la obra'),
        ),
    ]
