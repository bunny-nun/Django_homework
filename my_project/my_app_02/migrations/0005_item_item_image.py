# Generated by Django 5.0.6 on 2024-06-24 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app_02', '0004_customer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='my_app_02/static/my_app_02/images/question.png', upload_to=''),
        ),
    ]