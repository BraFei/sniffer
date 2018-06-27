# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Sniffer(models.Model):
    row_id = models.AutoField(primary_key=True)
    id = models.CharField(max_length=100)
    mmac = models.CharField(max_length=100)
    rate = models.IntegerField(blank=True, null=True)
    wssid = models.CharField(max_length=100)
    wmac = models.CharField(max_length=100)
    date = models.DateTimeField()
    lat = models.CharField(max_length=100)
    lon = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class SnifferEquipment(models.Model):
    equip_name = models.CharField(max_length=20)
    mac = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.equip_name


class SnifferDetail(models.Model):
    row_id = models.AutoField(primary_key=True)
    master_id = models.IntegerField()
    time = models.DateTimeField()
    router = models.CharField(max_length=100)
    mac = models.CharField(max_length=100)
    rssi = models.CharField(max_length=100)
    rssi1 = models.CharField(max_length=100)
    rssi2 = models.CharField(max_length=100)
    rssi3 = models.CharField(max_length=100)
    rssi4 = models.CharField(max_length=100)
    range = models.FloatField(max_length=100)
    ts = models.CharField(max_length=100)
    tc = models.CharField(max_length=100)
    tmc = models.CharField(max_length=100)
    ds = models.CharField(max_length=100)
    essid0 = models.CharField(max_length=100)
    essid1 = models.CharField(max_length=100)
    essid2 = models.CharField(max_length=100)
    essid3 = models.CharField(max_length=100)
    essid4 = models.CharField(max_length=100)
    essid5 = models.CharField(max_length=100)
    essid6 = models.CharField(max_length=100)

    def __str__(self):
        return self.router
    
    class Meta:
        ordering = ['-time']


class Equipment(models.Model):
    equipment = models.CharField(max_length=255)

    def __str__(self):
        return self.equipment
