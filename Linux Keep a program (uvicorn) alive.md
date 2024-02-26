### How to avoid 

### Use cron
*/1 * * * * python3 /home/saba/Programming/haishin_bako/summon.py &

### The key is to use use cd and exec in this way, with parenthesis! 

FULL_PATH = '/home/saba/Programming/haishin_bako'
STARTSH_PATH = FULL_PATH + '/start.sh'
LAUNCH_CMD = '(cd {} && exec {})'.format(FULL_PATH, STARTSH_PATH)

See summon.py for full program that checks if a program is running
  then ressurects it with the launch cmd above
