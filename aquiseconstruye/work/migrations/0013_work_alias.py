# Generated by Django 4.1.1 on 2023-07-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0012_work_type_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='alias',
            field=models.CharField(default='test', max_length=100, verbose_name='Alias de la obra'),
        ),
    ]
