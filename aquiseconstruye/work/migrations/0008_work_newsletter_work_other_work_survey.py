# Generated by Django 4.1.1 on 2023-01-20 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0007_alter_work_constructor_alter_work_constructor1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='newsletter',
            field=models.FileField(blank=True, null=True, upload_to='newsletter', verbose_name='Boletin'),
        ),
        migrations.AddField(
            model_name='work',
            name='other',
            field=models.TextField(blank=True, null=True, verbose_name='Otra'),
        ),
        migrations.AddField(
            model_name='work',
            name='survey',
            field=models.IntegerField(choices=[(1, 'Afecta mi translado'), (2, 'Afecta mi patrimonio'), (3, 'Afecta mis labores domesticos'), (4, 'Otro')], default=1, verbose_name='encuesta'),
        ),
    ]
