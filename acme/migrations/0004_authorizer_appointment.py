# Generated by Django 3.1.2 on 2021-01-04 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0003_authorizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorizer',
            name='appointment',
            field=models.CharField(choices=[('CO', 'CO'), ('QM', 'QM'), ('KOTENCO', 'KOTENCO')], max_length=200, null=True),
        ),
    ]
