# Generated by Django 4.1.1 on 2022-10-20 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_codigo_mantenimiento_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taller',
            old_name='codigo',
            new_name='id',
        ),
    ]
