# Generated by Django 4.2.1 on 2023-06-02 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Atleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField()),
                ('categoria', models.CharField(blank=True, max_length=20, null=True)),
                ('apodo', models.CharField(blank=True, max_length=20, null=True)),
                ('Fran', models.DurationField(blank=True, null=True)),
                ('Grace', models.DurationField(blank=True, null=True)),
                ('Isabel', models.DurationField(blank=True, null=True)),
                ('Murph', models.DurationField(blank=True, null=True)),
                ('RM_backsquat', models.IntegerField(blank=True, null=True)),
                ('RM_deadlift', models.IntegerField(blank=True, null=True)),
                ('RM_bench', models.IntegerField(blank=True, null=True)),
                ('RM_snatch', models.IntegerField(blank=True, null=True)),
                ('RM_clean', models.IntegerField(blank=True, null=True)),
                ('RM_jerk', models.IntegerField(blank=True, null=True)),
                ('RM_cleanandjerk', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
