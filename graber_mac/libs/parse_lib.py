import re
import os
import subprocess
import traceback
import telnetlib
import time

def parse_mac_huawei_ma5800(s):
	ret = []

	for l in s.split('\n'):
		if ('dynamic' in l and ('gpon' in l or 'eth' in l)):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))>=4):
				s['vlan'] = l.split(' ')[-1]
				s['mac'] = l.split(' ')[3]
				s['age'] = '0'
				if('eth' in l):
					s['port'] = 'eth-' + l.split('dynamic ')[1].split(' ')[1] + l.split('dynamic ')[1].split(' ')[2]
				if('gpon' in l):
					s['port'] = 'gpon-' + l.split('dynamic ')[1].split(' ')[1] + l.split('dynamic ')[1].split(' ')[2]
				
				ret.append(s)

	return ret


def parse_mac_eltex_ma4000(s):
	ret = []

	for l in s.split('\n'):
		if (re.search("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}", l.lower())):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))>=4):
				s['vlan'] = l.split(' ')[1]
				s['mac'] = l.split(' ')[2]
				s['age'] = '0'
				
				s['port'] = l.split(s['mac'] + ' ')[1].replace(' ', '-')
				
				ret.append(s)

	return ret


def parse_mac_eltex_mes_3300(s):
	ret = []

	for l in s.split('\n'):
		if ('dynamic' in l and re.search("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}", l.lower())):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==4):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[2]
				ret.append(s)

	return ret


def parse_mac_eltex_mes_2300(s):
	ret = []

	for l in s.split('\n'):
		if ('dynamic' in l and re.search("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}", l.lower())):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==4):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[2]
				ret.append(s)

	return ret


def parse_mac_eltex_mes_3100(s):
	ret = []

	for l in s.split('\n'):
		if ('dynamic' in l and re.search("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}", l.lower())):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==4):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[2]
				ret.append(s)

	return ret

def parse_mac_eltex_mes_3500(s):
	ret = []

	for l in s.split('\n'):
		if ('dynamic' in l and re.search("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}", l.lower())):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==4):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[2]
				ret.append(s)

	return ret


def parse_mac_cisco_ws_3500(s):
	ret = []

	for l in s.split('\n'):
		if ('DYNAMIC' in l):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==4):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[3]
				ret.append(s)

	return ret

def parse_mac_cisco_ws_3700(s):
	ret = []

	for l in s.split('\n'):
		if ('DYNAMIC' in l):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==4):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[3]
				ret.append(s)

	return ret



def parse_mac_cisco_me_3600(s):
	ret = []

	for l in s.split('\n'):
		if ('DYNAMIC' in l):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==4):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[3]
				ret.append(s)

	return ret


def parse_mac_cisco_ws_2900(s):
	ret = []

	for l in s.split('\n'):
		if ('DYNAMIC' in l):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==4):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[3]
				ret.append(s)

	return ret

def parse_mac_cisco_me_3400(s):
	ret = []

	for l in s.split('\n'):
		if ('DYNAMIC' in l):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==4):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[3]
				ret.append(s)

	return ret


def parse_mac_juniper_ex_4500(s):
	ret = []

	for l in s.split('\n'):
		if(' Learn ' in l):
			s = {}
			l = ' '.join(l.split())
			if(len(l.split(' '))==5):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = l.split(' ')[3]
				if(':' in s['age']):
					age = 60 * int(s['age'].split(':')[0]) + int(s['age'].split(':')[1])
					s['age'] = str( age )
				s['port'] = l.split(' ')[4]
				ret.append(s)

	return ret

def parse_mac_juniper_qfx_5100(s):
	ret = []

	for l in s.split('\n'):
		if re.search("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}", l.lower()):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==5):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[4]
				ret.append(s)

	return ret
	
def parse_mac_juniper_ex_9200(s):
	ret = []

	for l in s.split('\n'):
		if re.search("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}", l.lower()):
			s = {}
			l = ' '.join(l.split()).strip()
			if(len(l.split(' '))==5):
				s['vlan'] = l.split(' ')[0]
				s['mac'] = l.split(' ')[1]
				s['age'] = '0'
				s['port'] = l.split(' ')[4]
				ret.append(s)

	return ret

def parse_mac_juniper_acx_2100(s):
	ret = []
	bd = ''
	
	for l in s.split('\n'):
		l = ' '.join(l.split()).strip()
		
		if('Bridging domain : ' in l):
			bd = l.split(' ')[3].replace(',', '')
	
		if re.search("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}", l.lower()):
			s = {}			
			if(len(l.split(' '))==3):
				s['vlan'] = bd
				s['mac'] = l.split(' ')[0]
				s['age'] = '0'
				s['port'] = l.split(' ')[2]
				ret.append(s)

	return ret

	
def dump_result(p_f_name, p_s):

	f= open(p_f_name,"w")
	f.write(p_s)
	f.close() 
