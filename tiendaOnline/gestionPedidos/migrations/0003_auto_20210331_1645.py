# Generated by Django 2.2.19 on 2021-03-31 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_auto_20210331_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='direccion',
            field=models.CharField(max_length=50, verbose_name='La direccion'),
        ),
    ]
