# Generated by Django 4.0.2 on 2022-02-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0035_auto_20220215_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parts',
            name='subsistema',
            field=models.CharField(choices=[('ELECTRICO', 'electrico'), ('HIDRAULICO', 'hidraulico'), ('NEUMATICO', 'neumatico'), ('CONTROL', 'control'), ('MECÁNICO', 'mecánico')], default='ELECTRICO', max_length=20),
        ),
    ]
