# coding = utf-8
from django import forms
from django.forms import fields


class SnifferEquipForm(forms.Form):
	equip_name = forms.CharField(label='设备名称')
	mac = forms.CharField(label='设备MAC')
	address = forms.CharField(label='位置信息', required=False)
	description = forms.CharField(label='描述', required=False)


class LoginForm(forms.Form):
	username = forms.CharField(label='用户名')
	password = forms.CharField(label='密  码', widget=forms.PasswordInput)


class EquipNameForm(forms.Form):
	equip_name = forms.CharField(label='设备名称')
	
	
class MasterIDForms(forms.Form):
	master_id = forms.IntegerField(label='嗅探针设备号')
	
	
class MacForms(forms.Form):
	mac = forms.CharField(label='设备mac地址')
	

class RangeForms(forms.Form):
	min_range = forms.CharField(label='最小距离')
	max_range = forms.CharField(label='最大距离')
	
	
class TimeForms(forms.Form):
	min_time = forms.DateTimeField(label='起始时间')
	max_time = forms.DateTimeField(label='截止时间')

	
	