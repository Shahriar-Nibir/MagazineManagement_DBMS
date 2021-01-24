# Generated by Django 3.1.2 on 2021-01-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0018_remove_stock_deficiency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issuer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('no', models.CharField(max_length=200, null=True)),
                ('coy', models.CharField(max_length=200, null=True)),
                ('rk', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
