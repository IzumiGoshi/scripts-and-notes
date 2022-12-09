#!/usr/bin/python3 

from subprocess import check_output, Popen
import sys
import re



if '-h' in sys.argv or '--help' in sys.argv:
	print('run with:   mpvtube youtube.com/XYZ max_height')
	print('you can also add fps (30/60) and a max file size (MiB) in that order')
	sys.exit()

arg_names = ['url', 'height', 'fps', 'size']
args = sys.argv[1:]
args = [int(arg) if arg.isdigit() else arg for arg in args]
args = dict(list(zip(arg_names, args)))

print(args)


formats = check_output(['yt-dlp', '-F', args['url']]).decode('utf-8').split('\n')

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

def get_video_info(line):
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

	line_split = line.split()
	fps = 0
	if '30' in line_split: fps = 30
	if '60' in line_split: fps = 60
	
	codec = ''
	for ls in line_split:
		if ls.startswith('avc1'): codec = 'avc1'
		if ls.startswith('vp9'): codec = 'vp9'
	
	
	height = int(height)
	size = float(size)

	return { 'option': option, 'height': height, 'size': size, 'line': line, 'fps': fps, 'codec': codec }


matching = []

for f in formats:
	info = get_video_info(f)
	if not info: continue
	if info['codec'] != 'avc1': continue
	if 'height' in args and info['height'] > args['height']: continue
	if 'fps' in args and info['fps'] != args['fps']: continue
	if 'size' in args and info['size'] > float(args['size']): continue
	matching.append(info)

matching = sorted(matching, key=lambda m: m['size'])

if len(matching) == 0:
	print('ERROR! No matching videos found.')
	sys.exit()

print('choosing....')

selection = matching[-1]
print(selection)

cmd = ['mpv', '--ytdl-format=' + selection['option'] + '+bestaudio', args['url']]
print(' '.join(cmd))
Popen(cmd)



