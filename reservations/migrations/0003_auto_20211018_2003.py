# Generated by Django 3.1.7 on 2021-10-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20211018_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='nombre_des_jours',
            field=models.PositiveIntegerField(null=True),
        ),
    ]