# Generated by Django 4.1.1 on 2022-12-09 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_survey_created_at_survey_updated_at_work_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='address',
            field=models.CharField(default='test', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
