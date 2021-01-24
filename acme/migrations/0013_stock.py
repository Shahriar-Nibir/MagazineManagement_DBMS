# Generated by Django 3.1.2 on 2021-01-05 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0012_auto_20210105_1244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coy', models.CharField(max_length=200, null=True)),
                ('auth', models.IntegerField(max_length=20, null=True)),
                ('amount', models.IntegerField(max_length=20, null=True)),
                ('ammo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acme.ammo')),
            ],
        ),
    ]
