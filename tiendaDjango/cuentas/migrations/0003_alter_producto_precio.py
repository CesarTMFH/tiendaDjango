# Generated by Django 5.0.4 on 2024-04-09 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_alter_producto_imagenes_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
