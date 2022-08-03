import os
import copy
import subprocess
import traceback
import time
import sys
import datetime
import re

sys.path.append('./libs')
import lib as lib
import parse_lib as parse_lib

dev_list = lib.get_result('ip-list.txt', False)

g_user = sys.argv[1]
g_pwd = sys.argv[2]

for d in dev_list:
	print(d)
	cmd_out = ''
	o_file_name = 'mac-' + d['name']

	if (d['vendor']=='eltex'):
		if('mes3100' in d['model'] or 'mes3500' in d['model'] or 'mes2300' in d['model'] or 'mes3300' in d['model']):
			cmd_out = lib.run_cmd_telnet_eltex(d['ip'], g_user, g_pwd, 'show mac address-table dynamic')
		if('ma4000' in d['model'] ):
			cmd_out = lib.run_cmd_telnet_eltex_ma4000(d['ip'], g_user, g_pwd, 'show mac all')

	if (d['vendor']=='huawei'):
		if('ma5800' in d['model'] ):
			cmd_out = lib.run_cmd_telnet_huawei_ma5800(d['ip'], g_user, g_pwd, 'display mac-address all | no-more')

        
	if (d['vendor']=='juniper'):
		if('ex4500' in d['model'] or 'ex4550' in d['model'] or 'qfx5100' in d['model'] or 'ex9200' in d['model']):
			cmd_out = lib.run_cmd_telnet_juniper(d['ip'], g_user, g_pwd, 'show ethernet-switching table')
		if('acx2100' in d['model']):
			cmd_out = lib.run_cmd_telnet_juniper(d['ip'], g_user, g_pwd, 'show bridge mac-table')

	if (d['vendor']=='cisco'):
		if('ws2900' in d['model']):
			cmd_out = lib.run_cmd_telnet_cisco(d['ip'], g_user, g_pwd, 'show mac address-table dynamic')
		if('me3400' in d['model']):
			cmd_out = lib.run_cmd_telnet_cisco(d['ip'], g_user, g_pwd, 'show mac address-table dynamic')
		if('me3600' in d['model']):
			cmd_out = lib.run_cmd_telnet_cisco(d['ip'], g_user, g_pwd, 'show mac address-table dynamic')
		if('ws3500' in d['model']):
			cmd_out = lib.run_cmd_telnet_cisco(d['ip'], g_user, g_pwd, 'show mac address-table dynamic')
		if('ws3700' in d['model']):
			cmd_out = lib.run_cmd_telnet_cisco(d['ip'], g_user, g_pwd, 'show mac address-table dynamic')


	if(cmd_out==''):
		print('no data')
		sys.exit()
	now = datetime.datetime.now()
	parse_lib.dump_result('output_raw/' + o_file_name +  '_' + str(now.hour) + '_' + str(now.minute) + '.txt', cmd_out)
	
	l_mac = None       
	if(d['vendor']=='eltex'):
		if ('mes3100' in d['model']):
			l_mac = parse_lib.parse_mac_eltex_mes_3100(cmd_out)			
		if ('mes3500' in d['model']):
			l_mac = parse_lib.parse_mac_eltex_mes_3500(cmd_out)
		if ('mes2300' in d['model']):
			l_mac = parse_lib.parse_mac_eltex_mes_2300(cmd_out)
		if ('mes3300' in d['model']):
			l_mac = parse_lib.parse_mac_eltex_mes_3300(cmd_out)
		if ('ma4000' in d['model']):
			l_mac = parse_lib.parse_mac_eltex_ma4000(cmd_out)

	if(d['vendor']=='huawei'):
		if ('ma5800' in d['model']):
			l_mac = parse_lib.parse_mac_huawei_ma5800(cmd_out)

	if(d['vendor']=='juniper'):
		if ('ex4500' in d['model']):
			l_mac = parse_lib.parse_mac_juniper_ex_4500(cmd_out)
		if ('ex4550' in d['model']):
			l_mac = parse_lib.parse_mac_juniper_ex_4500(cmd_out)
		if ('qfx5100' in d['model']):
			l_mac = parse_lib.parse_mac_juniper_qfx_5100(cmd_out)
		if ('ex9200' in d['model']):
			l_mac = parse_lib.parse_mac_juniper_ex_9200(cmd_out)
		if ('acx2100' in d['model']):
			l_mac = parse_lib.parse_mac_juniper_acx_2100(cmd_out)

	if(d['vendor']=='cisco'):
		if('ws2900' in d['model']):
			l_mac = parse_lib.parse_mac_cisco_ws_2900(cmd_out)
		if('me3400' in d['model']):
			l_mac = parse_lib.parse_mac_cisco_me_3400(cmd_out)
		if('me3600' in d['model']):
			l_mac = parse_lib.parse_mac_cisco_me_3600(cmd_out)
		if('ws3500' in d['model']):
			l_mac = parse_lib.parse_mac_cisco_ws_3500(cmd_out)
		if('ws3700' in d['model']):
			l_mac = parse_lib.parse_mac_cisco_ws_3700(cmd_out)
			
	if(l_mac is not None):
		lib.print_result('output/' + o_file_name +  '_' + str(now.hour) + '_' + str(now.minute) + '.csv', [], l_mac, False)
