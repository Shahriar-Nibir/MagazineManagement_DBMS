# Generated by Django 3.1.2 on 2021-01-10 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0046_auto_20210110_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='ammo',
        ),
        migrations.AddField(
            model_name='lot',
            name='ammo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.ammo'),
        ),
    ]
