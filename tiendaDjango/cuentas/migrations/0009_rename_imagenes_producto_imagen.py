# Generated by Django 5.0.4 on 2024-04-10 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0008_alter_producto_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='imagenes',
            new_name='imagen',
        ),
    ]
