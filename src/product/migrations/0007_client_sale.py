# Generated by Django 4.0.6 on 2022-07-27 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_client_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='sale',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
