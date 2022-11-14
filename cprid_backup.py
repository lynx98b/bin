"""
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "lock database override"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "add user dbarker uid 0 homedir /home/dbarker"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "add rba user dbarker roles adminRole"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "set user dbarker gid 100 shell /bin/bash"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "set user dbarker password-hash \$1\$Q43O\/bAm\$761B7deKoXgloZdbcjDYq\/"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "save config" """

import logging
import os

def main():
    logging.basicConfig(filename='logbackups.log', level=logging.DEBUG,format='%(asctime)s  %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started logs ')

gbname='192.168.2.66'
list_exception_backup=['bpbqsg5520','bpyb800']
list_backup_every_month=['bpbqsg20','bpyb200','bpyb400']

def getall_GW():

    list=['192.168.2.55','10.15.22.30','192.168.2.247']

def check_job_bkb():
    logging.info(f'check job bkb --> {gbname} ')
    mycmand1=f'cprid_util - server {gbname} -verbose rexec - rcmd / bin / clish - c "show interfaces " '
    mycmand2 = f'cprid_util - server {gbname} -verbose rexec - rcmd / bin / clish - c "mgmt login user admin password 1234Alger++ " '

    print(mycmand1)
    print(mycmand2)
    cmd_check_bkp = 'crontab -l |grep  -i /backups'
def add_job_bkb():
    cmd_add_bkp =f'set backup - scheduled  name {gbname} of Schedule > recurrence'

def remove_bkps():
    print('remove')
def backup_files():
    backup_files_conf=''
    backup_routing=''
    backup_show_configuration=''

def sync_folders():
    try:
       cmd_transfer =' rsync - avu - -delete "/home/user/A" "/home/user/B"'

       os.system('ls -')
    except Exception as e :
       logging.error(f'error sync {e} ')


def logs():
    logging.warning('is when this event was logged.')


def notifs(num):
    if num ==0 :
        print('error 0 ')
    elif num == 1:
        print('error 1')
    else:
        print('error autre')

if __name__ == '__main__':
    main()
    check_job_bkb()

    logging.info('Finished logs')



