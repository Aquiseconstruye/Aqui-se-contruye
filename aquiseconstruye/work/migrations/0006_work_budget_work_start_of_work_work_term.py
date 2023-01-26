# Generated by Django 4.1.1 on 2023-01-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_alter_work_contracts_alter_work_contracts1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='budget',
            field=models.FloatField(blank=True, null=True, verbose_name='presupuesto'),
        ),
        migrations.AddField(
            model_name='work',
            name='start_of_work',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='inicio de obra'),
        ),
        migrations.AddField(
            model_name='work',
            name='term',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='plazo'),
        ),
    ]