# Generated by Django 3.1.2 on 2021-01-10 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0055_auto_20210110_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='ammo',
        ),
        migrations.RemoveField(
            model_name='line',
            name='line',
        ),
        migrations.CreateModel(
            name='AmmoLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('ammo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.ammo')),
                ('linename', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.linename')),
            ],
        ),
        migrations.AddField(
            model_name='line',
            name='ammoline',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.ammoline'),
        ),
    ]