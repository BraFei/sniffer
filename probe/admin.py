from django.contrib import admin
from .models import Sniffer, SnifferDetail, Equipment
# Register your models here.


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
	list_display = ('equipment',)


@admin.register(Sniffer)
class SnifferAdmin(admin.ModelAdmin):
	list_display = ('id',  'mmac',  'rate', 'wssid', 'wmac',  'date', 'lat', 'lon',  'addr')


@admin.register(SnifferDetail)
class SnifferDetail(admin.ModelAdmin):
	list_display = ['row_id', 'master_id', 'time', 'router', 'mac', 'rssi', 'rssi1', 'rssi2', 'rssi3', 'rssi4', 'range',
					'ts', 'tc', 'tmc', 'ds', 'essid0', 'essid1', 'essid2', 'essid3', 'essid4', 'essid5', 'essid6']