# Generated by Django 3.1.2 on 2021-01-07 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0024_auto_20210107_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='deficiency',
        ),
    ]
