# Generated by Django 3.1.2 on 2021-01-10 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acme', '0057_auto_20210110_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turningover',
            name='toline',
        ),
        migrations.AddField(
            model_name='turningover',
            name='linename1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='acme.linename'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]