# Generated by Django 4.2.1 on 2023-06-15 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atletas', '0010_alter_atleta_fran_time_alter_atleta_grace_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atleta',
            old_name='fran_time',
            new_name='fran',
        ),
        migrations.RenameField(
            model_name='atleta',
            old_name='grace_time',
            new_name='grace',
        ),
        migrations.RenameField(
            model_name='atleta',
            old_name='murph_time',
            new_name='murph',
        ),
    ]
