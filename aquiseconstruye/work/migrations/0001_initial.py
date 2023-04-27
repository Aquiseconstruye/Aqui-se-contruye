# Generated by Django 4.1.1 on 2023-04-25 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsletter', models.FileField(blank=True, null=True, upload_to='newsletter', verbose_name='fuentes')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey', models.IntegerField(choices=[(1, 'Afecta mi translado'), (2, 'Afecta mi patrimonio'), (3, 'Afecta mis labores domesticos'), (4, 'Otro')], default=1, verbose_name='encuesta')),
                ('other', models.TextField(blank=True, null=True, verbose_name='Otra')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrafficLight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=300)),
                ('trafficlight', models.ImageField(blank=True, null=True, upload_to='trafficlight', verbose_name='semaforo')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Nombre de la obra')),
                ('slug', models.CharField(blank=True, db_index=True, max_length=100, null=True, unique=True)),
                ('address', models.CharField(default='test', max_length=500, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image9', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image10', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image11', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image12', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image13', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image14', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image15', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image16', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image17', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image18', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image19', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('image20', models.ImageField(blank=True, null=True, upload_to='galery/%Y-%m-%d/', verbose_name='galeria')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='precio')),
                ('budget', models.FloatField(blank=True, null=True, verbose_name='presupuesto')),
                ('term', models.DateTimeField(blank=True, null=True, verbose_name='plazo')),
                ('start_of_work', models.DateTimeField(blank=True, null=True, verbose_name='inicio de obra')),
                ('traffic_light', models.IntegerField(choices=[(1, 'Rojo'), (2, 'Amarillo'), (3, 'Verde')], default=2, verbose_name='semaforo')),
                ('official', models.CharField(blank=True, max_length=200, null=True, verbose_name='funcionario')),
                ('dependence', models.CharField(blank=True, max_length=500, null=True, verbose_name='dependencia')),
                ('constructor', models.CharField(blank=True, max_length=200, null=True, verbose_name='constructoras')),
                ('constructor1', models.CharField(blank=True, max_length=200, null=True, verbose_name='constructoras')),
                ('constructor2', models.CharField(blank=True, max_length=200, null=True, verbose_name='constructoras')),
                ('constructor3', models.CharField(blank=True, max_length=200, null=True, verbose_name='constructoras')),
                ('constructor4', models.CharField(blank=True, max_length=200, null=True, verbose_name='constructoras')),
                ('contracts', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts1', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts2', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts3', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts4', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts5', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts6', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts7', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts8', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts9', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts10', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts11', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts12', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts13', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts14', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts15', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts16', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts17', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts18', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts19', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts20', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts21', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts22', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts23', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts24', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts25', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts26', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts27', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts28', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts29', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts30', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts31', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts32', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts33', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts34', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts35', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts36', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts37', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts38', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts39', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts40', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts41', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts42', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts43', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts44', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts45', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts46', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts47', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts48', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts49', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('contracts50', models.FileField(blank=True, null=True, upload_to='contracts/%Y-%m-%d/', verbose_name='contratos y licitaciones')),
                ('other', models.TextField(blank=True, null=True, verbose_name='Otra')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('img_traffic_light', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semaforo', to='work.trafficlight')),
                ('newsletter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publicacion', to='work.newsletter')),
                ('survey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Encuesta', to='work.survey')),
            ],
        ),
    ]
