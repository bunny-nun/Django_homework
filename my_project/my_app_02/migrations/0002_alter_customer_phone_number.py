# Generated by Django 5.0.6 on 2024-06-09 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app_02', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
