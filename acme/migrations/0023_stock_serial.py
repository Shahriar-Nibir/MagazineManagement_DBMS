# Generated by Django 3.1.2 on 2021-01-07 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0022_stock_deficiency'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='serial',
            field=models.IntegerField(null=True),
        ),
    ]