# Generated by Django 3.2.9 on 2021-12-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0008_alter_actividade_partes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividade',
            name='tiempo_Extimado',
            field=models.FloatField(),
        ),
    ]
