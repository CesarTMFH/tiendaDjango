# Generated by Django 5.0.4 on 2024-04-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0007_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]