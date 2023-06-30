# Generated by Django 3.2.9 on 2022-02-10 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0032_auto_20220208_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='partsquantity',
            name='equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment'),
        ),
        migrations.AlterField(
            model_name='parts',
            name='equipo',
            field=models.ManyToManyField(blank=True, null=True, to='equipment.Equipment'),
        ),
    ]