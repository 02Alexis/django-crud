# Generated by Django 3.2.9 on 2022-02-03 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0027_alter_equipment_imagen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actividade',
            new_name='Actividades',
        ),
        migrations.RenameModel(
            old_name='Reporte_Actividade',
            new_name='Reporte_Actividades',
        ),
    ]
