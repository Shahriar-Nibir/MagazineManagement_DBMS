# Generated by Django 3.1.2 on 2021-01-08 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0036_auto_20210108_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='issuer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.issuer'),
        ),
    ]