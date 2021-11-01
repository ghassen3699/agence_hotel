# Generated by Django 3.1.7 on 2021-10-14 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='numero_teliphone',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='compte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='genre',
            field=models.CharField(choices=[('HOMME', 'Homme'), ('FEMME', 'Femme')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='nom',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='prenom',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
