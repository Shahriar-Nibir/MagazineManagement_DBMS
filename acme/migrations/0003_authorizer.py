# Generated by Django 3.1.2 on 2021-01-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0002_ammo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('rk', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
