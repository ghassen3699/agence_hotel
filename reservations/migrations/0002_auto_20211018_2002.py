# Generated by Django 3.1.7 on 2021-10-18 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_de_debut',
            field=models.DateField(),
        ),
    ]