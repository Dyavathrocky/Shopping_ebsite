# Generated by Django 3.1 on 2021-12-04 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_avilbale',
            new_name='is_avilable',
        ),
    ]