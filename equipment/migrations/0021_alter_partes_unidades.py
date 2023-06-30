# Generated by Django 3.2.9 on 2022-01-25 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0020_actividade_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partes',
            name='Unidades',
            field=models.CharField(choices=[('---', '---'), ('CENTIMETROS', 'centimetros'), ('GRAMOS', 'gramos'), ('LITROS', 'litros'), ('METROS', 'metros'), ('UNIDADES', 'unidades')], default='---', max_length=20),
        ),
    ]
