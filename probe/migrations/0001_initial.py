# Generated by Django 2.0 on 2018-05-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sniffer',
            fields=[
                ('row_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(max_length=100)),
                ('mmac', models.CharField(max_length=100)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('wssid', models.CharField(max_length=100)),
                ('wmac', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('lat', models.CharField(max_length=100)),
                ('lon', models.CharField(max_length=100)),
                ('addr', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SnifferDetail',
            fields=[
                ('row_id', models.AutoField(primary_key=True, serialize=False)),
                ('master_id', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('router', models.CharField(max_length=100)),
                ('mac', models.CharField(max_length=100)),
                ('rssi', models.CharField(max_length=100)),
                ('rssi1', models.CharField(max_length=100)),
                ('rssi2', models.CharField(max_length=100)),
                ('rssi3', models.CharField(max_length=100)),
                ('rssi4', models.CharField(max_length=100)),
                ('range', models.CharField(max_length=100)),
                ('ts', models.CharField(max_length=100)),
                ('tc', models.CharField(max_length=100)),
                ('tmc', models.CharField(max_length=100)),
                ('ds', models.CharField(max_length=100)),
                ('essid0', models.CharField(max_length=100)),
                ('essid1', models.CharField(max_length=100)),
                ('essid2', models.CharField(max_length=100)),
                ('essid3', models.CharField(max_length=100)),
                ('essid4', models.CharField(max_length=100)),
                ('essid5', models.CharField(max_length=100)),
                ('essid6', models.CharField(max_length=100)),
            ],
        ),
    ]
