import os
import time

run_count = input("input run count: ") 
run_delay = input("input delay (s): ") 
run_user = raw_input("user: ") 
run_pwd = raw_input("password: ")

i = 0
while(i<int(run_count)):
	os.system("python mac_get.py " + run_user + ' ' + run_pwd)
	i = i + 1
	time.sleep(int(run_delay))
