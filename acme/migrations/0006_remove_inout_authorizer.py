# Generated by Django 3.1.2 on 2021-01-04 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0005_inout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inout',
            name='authorizer',
        ),
    ]
