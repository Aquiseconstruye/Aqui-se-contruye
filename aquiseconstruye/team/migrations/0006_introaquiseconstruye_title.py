# Generated by Django 4.1.1 on 2023-07-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_metodologic_remove_introaquiseconstruye_metodologic'),
    ]

    operations = [
        migrations.AddField(
            model_name='introaquiseconstruye',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='quienes somos'),
        ),
    ]
