# Generated by Django 3.2.18 on 2023-06-20 20:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


def insert_items(apps, schema_editor):
    modelo = apps.get_model('documentation', 'StoredProcedureHTTPType')
    modelo.objects.create(type_name='Oracle')
    modelo.objects.create(type_name='SQL Server')


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0006_databasescript_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoredProcedureHTTPType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=300, verbose_name='Tipo de SP HTTP')),
            ],
            options={
                'verbose_name_plural': 'SP HTTP - Tipos de SP',
            },
        ),
        migrations.CreateModel(
            name='StoredProcedureHTTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Numero de version')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('file', models.FileField(upload_to='', verbose_name='Archivo')),
                ('readme', models.TextField(verbose_name='Readme')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sps', to='documentation.storedprocedurehttptype')),
            ],
            options={
                'verbose_name_plural': 'SP HTTP - SP HTTP',
            },
        ),
        migrations.RunPython(insert_items),
    ]
