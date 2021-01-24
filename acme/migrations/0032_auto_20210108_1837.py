# Generated by Django 3.1.2 on 2021-01-08 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acme', '0031_auto_20210108_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorizer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
