# Generated by Django 3.1.2 on 2021-01-08 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0035_auto_20210108_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.issue'),
        ),
        migrations.AddField(
            model_name='deposit',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.stock'),
        ),
    ]