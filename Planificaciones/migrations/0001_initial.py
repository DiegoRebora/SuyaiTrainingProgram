# Generated by Django 4.2.1 on 2023-06-02 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semana', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('fecha_inicio', models.DateField()),
                ('coach', models.CharField(max_length=255)),
                ('planificacion', models.ImageField(blank=True, null=True, upload_to='planificaciones')),
                ('comentario', models.TextField(blank=True)),
            ],
        ),
    ]
