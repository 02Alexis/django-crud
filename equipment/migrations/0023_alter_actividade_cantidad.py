# Generated by Django 3.2.9 on 2022-01-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0022_auto_20220125_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividade',
            name='cantidad',
            field=models.FloatField(blank=True, null=True),
        ),
    ]