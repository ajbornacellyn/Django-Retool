# Generated by Django 4.1.1 on 2022-10-09 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mantenimiento',
            old_name='codigo',
            new_name='id',
        ),
    ]
