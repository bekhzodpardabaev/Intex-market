# Generated by Django 4.0.6 on 2022-07-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_client_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
