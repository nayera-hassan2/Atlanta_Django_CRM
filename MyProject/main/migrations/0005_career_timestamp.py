# Generated by Django 5.0 on 2024-01-03 12:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_career'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
