# Generated by Django 3.1.2 on 2021-01-05 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0013_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='deficiency',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]