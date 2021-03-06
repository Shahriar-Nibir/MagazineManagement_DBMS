# Generated by Django 3.1.2 on 2021-01-10 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0060_auto_20210110_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('demand', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.demand')),
                ('issue', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.issue')),
            ],
        ),
    ]
