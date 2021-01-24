# Generated by Django 3.1.2 on 2021-01-04 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0004_authorizer_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='InOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=200)),
                ('in_time', models.TimeField()),
                ('number', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('rk', models.CharField(max_length=200, null=True)),
                ('coy', models.CharField(max_length=200, null=True)),
                ('reason', models.CharField(max_length=200, null=True)),
                ('out_time', models.TimeField()),
                ('authorizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acme.authorizer')),
            ],
        ),
    ]