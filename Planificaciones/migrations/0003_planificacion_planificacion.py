# Generated by Django 4.2.1 on 2023-06-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planificaciones', '0002_remove_planificacion_planificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='planificacion',
            name='planificacion',
            field=models.ImageField(blank=True, null=True, upload_to='planificaciones'),
        ),
    ]