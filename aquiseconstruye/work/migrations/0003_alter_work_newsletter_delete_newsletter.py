# Generated by Django 4.1.1 on 2023-04-26 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_work_completate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='newsletter',
            field=models.FileField(blank=True, null=True, upload_to='newsletter', verbose_name='fuentes'),
        ),
        migrations.DeleteModel(
            name='Newsletter',
        ),
    ]
