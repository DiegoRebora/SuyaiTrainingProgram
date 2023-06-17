# Generated by Django 4.2.1 on 2023-06-17 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atletas', '0014_alter_score_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('numero_semana', models.IntegerField()),
                ('imagen_planificacion', models.ImageField(upload_to='planificaciones/')),
                ('comentario', models.CharField(max_length=255)),
            ],
        ),
    ]
