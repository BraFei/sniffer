# Generated by Django 2.0 on 2018-06-03 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('probe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snifferdetail',
            name='range',
            field=models.FloatField(max_length=100),
        ),
    ]
