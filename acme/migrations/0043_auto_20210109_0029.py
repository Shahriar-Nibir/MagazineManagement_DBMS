# Generated by Django 3.1.2 on 2021-01-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0042_auto_20210109_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='deficiency',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
