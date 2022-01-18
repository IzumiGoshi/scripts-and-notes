#!/usr/bin/python3 

from subprocess import check_output, Popen
import sys
import re


def exist_pop(key, pop_list):
	if key in pop_list:
		ind = pop_list.index(key)
		return pop_list.pop(ind)
	else:
		return None
		

best = exist_pop('-b', sys.argv)
res = sys.argv[1]
url = sys.argv[2]

formats = check_output(['yt-dlp', '-F', url]).decode('utf-8').split('\n')
res_pattern = '\d+x\d+'
size_pattern = '\d+\.?\d+[M,G]iB'
size_digits = '\d+\.?\d+'
option_pattern = '\d+'

def GiB_to_Mib(GiB):  # takes a string like 245.8GiB
	if 'GiB' not in GiB:
		return GiB
	GiB = GiB.split('GiB')[0]
	GiB = float(GiB)
	GiB = GiB * 1000
	GiB = str(GiB) + 'MiB'
	return GiB

def get_option_height_size(line):
	option = re.findall(option_pattern, line)
	res = re.findall(res_pattern, line)
	size = re.findall(size_pattern, line)
	if not all([option, res, size]):
		return None
	option = option[0]
	res = res[0]
	size = size[0]
	height = res.split('x')[1]
	size =	GiB_to_Mib(size)
	size = re.findall(size_digits, size)[0]
	size = float(size)
	
	return (option, height, size, line)
	
OPTION = 0
HEIGHT = 1
SIZE = 2
LINE = 3
matching = [get_option_height_size(f) for f in formats]
matching = [m for m in matching if m] # filter out extra info from the output of yt-dlp -F
matching = [m for m in matching if m[HEIGHT] == res]

matching = sorted(matching, key=lambda m: m[SIZE])

if best: 
	selection = matching[-1]
else:
	selection = matching[0]


cmd = ['nohup', 'mpv', '--ytdl-format=' + selection[OPTION] + '+bestaudio', url, '&']
Popen(cmd)




