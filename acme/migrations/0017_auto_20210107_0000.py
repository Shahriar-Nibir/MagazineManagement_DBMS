# Generated by Django 3.1.2 on 2021-01-06 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0016_stock_deficiency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='auth',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='deficiency',
            field=models.IntegerField(null=True),
        ),
    ]
