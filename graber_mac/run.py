import os
import time
import getpass

try:
	input = raw_input
except NameError:
	pass

run_count = input("input run count: ") 
run_delay = input("input delay (s): ") 
run_user = input("user: ") 
run_pwd = getpass.getpass(prompt='Password: ')

i = 0
while(i<int(run_count)):
	os.system("python mac_get.py " + run_user + ' ' + run_pwd)
	i = i + 1
	time.sleep(int(run_delay))
