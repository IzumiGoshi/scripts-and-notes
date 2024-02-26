from subprocess import check_output
from subprocess import Popen
import json
import time 
import re
import os
import traceback

def ps():
	ps_output = check_output('ps aux', shell=True).decode('utf-8')
	ps_output = ps_output.split('\n')
	names = ps_output.pop(0)
	names = names.split()

	ps_dicts = []
	for po in ps_output:
		po = po.split()
		if len(po) > 11:
			po[10] = ' '.join(po[10:])
		ps_dicts.append(dict(zip(names, po)))
	return ps_dicts


def check_run_count(command, ps_list): # checks against as it appears, and lowercase ver.
	count = 0
	for proc in ps_list:
		proc_cmd = proc.get('COMMAND')
		if not proc_cmd: continue
		if re.findall(command, proc_cmd) or re.findall(command, proc_cmd.lower()):
			count = count + 1
	return count


def summon(launch_cmd, cur_work_dir):
	try:
		Popen(launch_cmd.split(), start_new_session=True, cwd=cur_work_dir)
		print('uwu?')	
	except Exception as e:
		print(e)
		print(traceback.format_exc())


FULL_PATH = '/home/saba/Programming/haishin_bako'
STARTSH_PATH = FULL_PATH + '/start.sh'
LAUNCH_CMD = '(cd {} && exec {})'.format(FULL_PATH, STARTSH_PATH)
# haishin_bako:app
count = check_run_count(r'haishin_bako\:app', ps())
if count == 0:
    os.system(LAUNCH_CMD)
