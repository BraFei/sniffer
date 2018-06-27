from django.urls import path
from .views import *
from django.contrib.auth.views import login, logout_then_login, logout
urlpatterns = [
	# path('login', user_login, name='login'),
	path('login', login, name='login'),
	path('logout', logout, name='logout'),
	path('logout-then-login', logout_then_login, name='logout_then_login'),
	path('sniffer_list', sniffer_list, name='sniffer_list'),
	path('sniffer_detail/<int:sniffer_id>', sniffer_detail, name='sniffer_detail'),
	path('sniffer_detail_delete/<int:sniffer_id>', sniffer_detail_delete, name='sniffer_detail_delete'),
	path('sniffer_equip_delete/<int:equip_id>', sniffer_equip_delete, name='sniffer_equip_delete'),
	path('sniffer_detail_delete_operate/<int:sniffer_id>', sniffer_detail_delete_operate, name='sniffer_detail_delete_operate'),
	path('equip_detail_delete_operate/<int:equip_id>', equip_detail_delete_operate, name='equip_detail_delete_operate'),
	path('master_id', master_id, name='master_id'),
	path('mac', mac, name='mac'),
	path('equip_range', equip_range, name='equip_range'),
	path('time_filter', time_filter, name='time_filter'),
	path('mac_filter/<int:mac>', mac_filter, name='mac_filter'),
	path('master_id_filter/<int:master_id>', master_id_filter, name='master_id_filter'),
	path('time_single_filter/<int:year>/<int:month>/<int:day>', time_single_filter, name='time_single_filter'),
	path('rssi_filter/<int:row_id>', rssi_filter, name='rssi_filter'),
	path('sniffer_equip_list', sniffer_equip_list, name='sniffer_equip_list'),
	path('sniffer_equip_detail/<int:id>', sniffer_equip_detail, name='sniffer_equip_detail'),
	path('sniffer_equip_add', sniffer_equip_add, name='sniffer_equip_add'),
	path('equip_name', equip_name, name='equip_name'),
]
