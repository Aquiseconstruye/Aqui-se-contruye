# Generated by Django 4.1.1 on 2023-09-20 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigation', '0004_investigation_image5_investigation_image6_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestigationHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Titulo')),
                ('introduccion', models.TextField(max_length=1500, verbose_name='introducción')),
            ],
        ),
    ]