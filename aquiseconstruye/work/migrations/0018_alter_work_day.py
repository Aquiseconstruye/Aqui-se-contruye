# Generated by Django 4.1.1 on 2023-07-20 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0017_remove_work_term2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='day',
            field=models.IntegerField(blank=True, null=True, verbose_name='Dias En los que concluyo'),
        ),
    ]
