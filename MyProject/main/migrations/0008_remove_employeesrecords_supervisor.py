# Generated by Django 5.0 on 2024-01-04 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_employeesrecords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeesrecords',
            name='supervisor',
        ),
    ]
