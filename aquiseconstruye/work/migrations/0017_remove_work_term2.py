# Generated by Django 4.1.1 on 2023-07-20 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0016_work_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='term2',
        ),
    ]
