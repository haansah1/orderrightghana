# Generated by Django 5.1.6 on 2025-04-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderrightapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
