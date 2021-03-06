# Generated by Django 3.1.2 on 2021-01-10 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0044_auto_20210109_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=200, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('date_added', models.DateField(null=True)),
                ('ammo', models.ManyToManyField(to='acme.Ammo')),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=200, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('ammo', models.ManyToManyField(to='acme.Ammo')),
            ],
        ),
        migrations.CreateModel(
            name='TurningOver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
                ('lot', models.ManyToManyField(to='acme.Lot')),
                ('toline', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.line')),
            ],
        ),
        migrations.AddField(
            model_name='line',
            name='lot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.lot'),
        ),
    ]
