# Generated by Django 3.2.18 on 2023-05-18 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigurationFileName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration_file', models.CharField(max_length=250, verbose_name='Nombre de archivo de configuracion')),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=50, verbose_name='Numero de version')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('summary', models.TextField(verbose_name='Resumen')),
            ],
        ),
        migrations.CreateModel(
            name='VersionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.TextField(blank=True, null=True, verbose_name='Titulo de imagen')),
                ('image_description', models.TextField(blank=True, null=True, verbose_name='Texto de imagen')),
                ('image', models.ImageField(upload_to='', verbose_name='Image')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='documentation.version')),
            ],
        ),
        migrations.CreateModel(
            name='VersionFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='', verbose_name='Archivo')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='documentation.version')),
            ],
        ),
        migrations.CreateModel(
            name='VersionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_text', models.TextField(verbose_name='Texto de detalle')),
                ('bold', models.BooleanField(default=False, verbose_name='Negrita')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', related_query_name='version', to='documentation.version')),
            ],
        ),
        migrations.CreateModel(
            name='VersionConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration', models.TextField(verbose_name='Cambio en configuracion')),
                ('file_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='documentation.configurationfilename')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='documentation.version')),
            ],
        ),
        migrations.CreateModel(
            name='VersionComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.CharField(max_length=200, verbose_name='Version de componente')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='components', to='documentation.version')),
            ],
        ),
    ]
