# Generated by Django 3.1.7 on 2021-10-18 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_auto_20211014_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='numero_teliphone',
            new_name='numero_telephone',
        ),
    ]
