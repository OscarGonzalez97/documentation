# Generated by Django 3.2.18 on 2023-06-13 23:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documentation', '0004_postman_postmanfunctionality_video_videotype'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Fecha'),
        ),
    ]
