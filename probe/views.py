# coding=utf-8
import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import SnifferDetail, SnifferEquipment
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import MasterIDForms, MacForms, RangeForms, TimeForms, SnifferEquipForm, EquipNameForm
# from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import re


def get_sniffer_detail_list_common_data(request, blogs_all_list):
	paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
	page_num = request.GET.get('page', 1)  # 获取url的页面参数（GET请求）
	print(page_num)
	try:
		page_of_blogs = paginator.get_page(page_num)
	except PageNotAnInteger:
		page_of_blogs = paginator.get_page(1)
	except EmptyPage:
		page_of_blogs = paginator.page(paginator.num_pages-1)
	current_page_num = page_of_blogs.number  # 获取当前页码
	# 获取当前页码前后各2页的页码范围
	page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + list(
		range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
	# 加上省略页码标记
	if page_range[0] - 1 >= 2:
		page_range.insert(0, '...')
	if paginator.num_pages - page_range[-1] >= 2:
		page_range.append('...')
	# 加上首页和尾页
	if page_range[0] != 1:
		page_range.insert(0, 1)
	if page_range[-1] != paginator.num_pages:
		page_range.append(paginator.num_pages)
	context = {}
	context['sniffer_details'] = page_of_blogs.object_list
	print(context['sniffer_details'])
	context['page_of_sniffer_details'] = page_of_blogs
	print(page_of_blogs.previous_page_number)
	context['page_range'] = page_range
	return context


# Create your views here.
@login_required
def sniffer_list(req):
	sniffer_details = SnifferDetail.objects.all()
	context = get_sniffer_detail_list_common_data(req, sniffer_details)
	sniffer_path = req.get_full_path()
	context['sniffer_path'] = sniffer_path
	return render(req, 'probe/sniffer_list.html', context)


@login_required
def sniffer_detail(req, sniffer_id):
	sniffer_details = get_object_or_404(SnifferDetail, row_id=sniffer_id)
	context = {}
	context['sniffer_details'] = sniffer_details
	return render(req, 'probe/sniffer_detail.html', context)


@login_required
def sniffer_detail_delete(req, sniffer_id):
	sniffer_details = get_object_or_404(SnifferDetail, row_id=sniffer_id)
	context = {}
	context['sniffer_details'] = sniffer_details
	return render(req, 'probe/sniffer_detail_delete.html', context)


@login_required
def sniffer_equip_delete(req, equip_id):
	sniffer_details = get_object_or_404(SnifferEquipment, id=equip_id)
	context = {}
	context['sniffer_details'] = sniffer_details
	return render(req, 'probe/equip_detail_delete.html', context)


@login_required
def equip_detail_delete_operate(req, equip_id):
		sniffer_details = get_object_or_404(SnifferEquipment, id=equip_id)
		sniffer_details.delete()
		return HttpResponseRedirect('/sniffer_equip_list')


@login_required
def sniffer_detail_delete_operate(req, sniffer_id):
		sniffer_details = get_object_or_404(SnifferDetail, row_id=sniffer_id)
		sniffer_details.delete()
		return HttpResponseRedirect('/sniffer_list')


# 按照设备名称
@login_required
def equip_name(req):
	'''
			if req.method == "POST":
		content = EquipNameForm(req.POST)
		if content.is_valid():
			equip_name = content.cleaned_data['equip_name']
			equip = get_object_or_404(SnifferEquipment, equip_name=equip_name)
			if equip is None:
				content = EquipNameForm()
				return render(req, 'probe/filter.html', {'content': content})
			else:
				equip_mac = equip.mac
				sniffer_list = SnifferDetail.objects.filter(mac=equip_mac)
				context = get_sniffer_detail_list_common_data(req, sniffer_list)
				message = '嗅探针设备名称为：%s 收集到的数据' % equip_name
				context['message'] = message
				context['q'] = equip_name
				return render(req, 'probe/sniffer_filter_list.html', context)
		else:
			content = EquipNameForm()
			return render(req, 'probe/filter.html', {'content': content})
	else:
		try:
			equip_name = req.GET.get('q', False)
			equip = get_object_or_404(SnifferEquipment, equip_name=equip_name)
			if equip is None:
				content = EquipNameForm()
				return render(req, 'probe/filter.html', {'content': content})
			else:
				equip_name_list = SnifferDetail.objects.filter(mac=equip.mac)
				context = get_sniffer_detail_list_common_data(req, equip_name_list)
				message = '嗅探针设备名称为：%s 收集到的数据' % equip_name
				context['message'] = message
				context['q'] = equip_name
				return render(req, 'probe/sniffer_filter_list.html', context)
		except:
			return HttpResponseRedirect('/sniffer_list')
	'''
	try:
		if req.method == 'GET':
			equip_name = req.GET.get('equip-name')
			print(equip_name)
			if equip_name is not None:
				equip = get_object_or_404(SnifferEquipment, equip_name=equip_name)
				if equip is None:
					return render(req, 'probe/sniffer_filter_list.html')
				else:
					sniffer_list = SnifferDetail.objects.filter(mac=equip.mac)
					context = get_sniffer_detail_list_common_data(req, sniffer_list)
					message = '探针为：%s 收集到的数据' % equip_name
					context['message'] = message
					context['q'] = equip_name
				return render(req, 'probe/sniffer_filter_list.html', context)
			else:
				try:
					equip_name = req.GET.get('q', False)
					if equip_name is not None:
						equip = get_object_or_404(SnifferEquipment, equip_name=equip_name)
						sniffer_list = SnifferDetail.objects.filter(mac=equip.mac)
						context = get_sniffer_detail_list_common_data(req, sniffer_list)
						message = '探针为：%s 收集到的数据' % equip_name
						context['message'] = message
						context['q'] =equip_name
						return render(req, 'probe/sniffer_filter_list.html', context)
				except :
					return HttpResponseRedirect('/sniffer_list')
	except:
		return render(req, 'probe/sniffer_filter_list.html')


# 按照嗅探针设备号
@login_required
def master_id(req):
	try:
		if req.method == 'GET':
			master_id = req.GET.get('master_id')
			print(master_id)
			if master_id is not None:
				master_id_list = SnifferDetail.objects.filter(master_id=master_id)
				context = get_sniffer_detail_list_common_data(req, master_id_list)
				message = '设备号为：%s 收集到的数据' % master_id
				context['message'] = message
				context['q'] = master_id
				return render(req, 'probe/sniffer_filter_list.html', context)
			else:
				try:
					print(master_id)
					master_id = req.GET.get('q', False)
					master_id_list = SnifferDetail.objects.filter(master_id=master_id)
					context = get_sniffer_detail_list_common_data(req, master_id_list)
					message = '设备号为：%s 收集到的数据' % master_id
					context['message'] = message
					context['q'] = master_id
					return render(req, 'probe/sniffer_filter_list.html', context)
				except :
					return HttpResponseRedirect('/sniffer_list')
	except:
		return render(req, 'probe/sniffer_filter_list.html')
	

@login_required
def mac(req):
	if req.method == 'GET':
		mac = req.GET.get('mac')
		if mac is not None:
			print(mac)
			mac_list = SnifferDetail.objects.filter(mac=mac)
			# mac_list = SnifferDetail.objects.all()
			context = get_sniffer_detail_list_common_data(req, mac_list)
			message = '设备mac为：%s 收集到的数据' % mac
			context['message'] = message
			context['q'] = mac
			return render(req, 'probe/sniffer_filter_list.html', context)
		else:
			try:
				print(mac)
				mac = req.GET.get('q', False)
				mac_list = SnifferDetail.objects.filter(mac=mac)
				context = get_sniffer_detail_list_common_data(req, mac_list)
				message = '设备mac为：%s 收集到的数据' % mac
				context['message'] = message
				context['q'] = mac
				return render(req, 'probe/sniffer_filter_list.html', context)
			except :
				return HttpResponseRedirect('/sniffer_list')
	

@login_required
def equip_range(req):
	message = '友情提示：请输入像：1.0， 3.00， 4,5之类的带有小数点的数值'
	if req.method == 'POST':
		content = RangeForms(req.POST)
		if content.is_valid():
			min_range = content.cleaned_data['min_range']
			max_range = content.cleaned_data['max_range']
			# 首先判定输入的是不是数值
			value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
			result_min = value.match(min_range)
			result_max = value.match(max_range)
			if result_max and result_min:
				if float(min_range) <= float(max_range):
					range_list = SnifferDetail.objects.filter(range__gt=min_range, range__lt=max_range)
					context = get_sniffer_detail_list_common_data(req, range_list)
					message = '在距离为 %s到%s 这一范围内收集的数据' % (min_range, max_range)
					context['message'] = message
					context['q1'] = min_range
					context['q2'] = max_range
					print(context['q1'])
					print(context['q2'])
					return render(req, 'probe/sniffer_range_filter_list.html', context)
				else:
					return render(req, 'probe/filter.html', {'content': content, 'error_2': True, 'message': message})
			else:
				return render(req, 'probe/filter.html', {'content': content, 'error_1': True, 'message': message})
		else:
			return render(req, 'probe/filter.html', {'content': content, 'message': message})
	else:
		try:
			print('GET')
			q1 = req.GET.get('q1', False)
			print(type(q1))
			q2 = req.GET.get('q2', False)
			page = req.GET.get('page', False)
			print('q1的值为%s' % q1)
			print('q1的类型:%s' % type(q1))
			print(q2)
			if q1 is False:
				print(False)
			else:
				print(True)
			if q1 is False:
				print('q1 %s' % q1)
				content = RangeForms()
				return render(req, 'probe/filter.html', {'content': content, 'message': message})
			else:
				print('page的值为%s' % page)
				range_list = SnifferDetail.objects.filter(range__gt=q1, range__lt=q2)
				context = get_sniffer_detail_list_common_data(req, range_list)
				message = '在距离为 %s到%s 这一范围内收集到的数据' % (q1, q2)
				context['message'] = message
				context['q1'] = q1
				context['q2'] = q2
				print('第二次')
				print('q1的值为%s' % q1)
				print(q2)
				return render(req, 'probe/sniffer_range_filter_list.html', context)
		except:
			return render(req, 'probe/sniffer_range_filter_list.html', context)


@login_required
def sniffer_equip_list(req):
	context = {}
	context['sniffer_equip_list'] = SnifferEquipment.objects.all()
	return render(req, 'probe/sniffer_equip_list.html', context)


@login_required
def sniffer_equip_add(req):
	if req.method == 'POST':
		cont = SnifferEquipForm(req.POST)
		if cont.is_valid():
			equip_name = cont.cleaned_data['equip_name']
			mac = cont.cleaned_data['mac']
			address = cont.cleaned_data['address']
			description = cont.cleaned_data['description']
			AA = SnifferEquipment.objects.filter(equip_name=equip_name, mac=mac)
			if AA:
				content = SnifferEquipForm()
				return render(req, 'probe/sniffer_equipment_form.html', {'content': content})
			else:
				SnifferEquipment.objects.get_or_create(
					equip_name=equip_name,
					mac=mac,
					address=address,
					description=description
				)
				context = {}
				context['sniffer_equip_list'] = SnifferEquipment.objects.all()
				return render(req, 'probe/sniffer_equip_list.html', context)
		else:
			content = SnifferEquipForm()
			return render(req, 'probe/sniffer_equipment_form.html', {'content': content})
	else:
		content = SnifferEquipForm()
		return render(req, 'probe/sniffer_equipment_form.html', {'content': content})


@login_required
def sniffer_equip_detail(req, id):
	context = {}
	equip_detail = get_object_or_404(SnifferEquipment, id=id)
	context['equip_detail'] = equip_detail
	return render(req, 'probe/sniffer_equip_detail.html', context)
	
	
@login_required
def time_filter(req):
	message_req = '输入的时间格式按照 2018-05-30 15:22:58样式填写'
	if req.method == 'POST':
		content = TimeForms(req.POST)
		if content.is_valid():
			min_time = content.cleaned_data['min_time']
			max_time = content.cleaned_data['max_time']
			range_time = SnifferDetail.objects.filter(time__gt=min_time, time__lt=max_time)
			context = {}
			context['sniffer_details'] = range_time
			message = '从%s到%s这段时间内收集到的数据' % (
			min_time.strftime('%Y-%m-%d %H:%M:%S'), max_time.strftime('%Y-%m-%d %H:%M:%S'))
			context['message'] = message
			return render(req, 'probe/sniffer_filter_list.html', context)
		else:
			return render(req, 'probe/filter.html', {'content': content, 'message_req': message_req})
	else:
		content = TimeForms()
		return render(req, 'probe/filter.html', {'content': content, 'message_req': message_req})


@login_required
def master_id_filter(req, master_id):
	master_id_list = SnifferDetail.objects.filter(master_id=master_id)
	context = get_sniffer_detail_list_common_data(req, master_id_list)
	return HttpResponseRedirect(reverse('sniffer_list'), context)


@login_required
def mac_filter(req, mac):
	mac_list = SnifferDetail.objects.filter(mac=mac)
	context = get_sniffer_detail_list_common_data(req, mac_list)
	return render(req, 'probe/sniffer_list.html', context)


@login_required
def time_single_filter(req, year, month, day):
	time_list = SnifferDetail.objects.filter(time__year=year, time__month=month, time__day=day)
	context = get_sniffer_detail_list_common_data(req, time_list)
	return render(req, 'probe/sniffer_list.html', context)


@login_required
def rssi_filter(req, row_id):
	rssi_type = get_object_or_404(SnifferDetail, row_id=row_id).rssi
	rssi_list = SnifferDetail.objects.filter(rssi=rssi_type)
	context = get_sniffer_detail_list_common_data(req, rssi_list)
	return render(req, 'probe/sniffer_list.html', context)
