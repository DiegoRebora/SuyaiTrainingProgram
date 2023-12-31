# Generated by Django 4.2.1 on 2023-06-02 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atletas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atleta',
            name='RM_backsquat',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='RM_bench',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='RM_clean',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='RM_cleanandjerk',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='RM_deadlift',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='RM_jerk',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='atleta',
            name='RM_snatch',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
