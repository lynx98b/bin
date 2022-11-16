""" NOTES
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "lock database override"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "add user dbarker uid 0 homedir /home/dbarker"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "add rba user dbarker roles adminRole"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "set user dbarker gid 100 shell /bin/bash"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "set user dbarker password-hash \$1\$Q43O\/bAm\$761B7deKoXgloZdbcjDYq\/"
cprid_util -server 1.1.1.1 -verbose rexec -rcmd /bin/clish -c "save config" """



"""  ##################################
     # Script Backup 2023  par DF5322 #
     # Domaine Corpo Hydro quebec     #    
     # Version 1.0                    #
     ################################## """


import logging
import os


# path des fichiers------------------------
path_dst_backup_checkpoint='/otp/PCS/bin/'
path_dst_backup_showConf='/otp/PCS/bin/'
path_dst_Log='/otp/PCS/Log/'
#------------------------------------------


#----------- LOG files parametres ---------
logging.basicConfig(filename='logbackups.log', level=logging.DEBUG, format='%(asctime)s  %(levelname)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info('Started logs ')
#------------------------------------------


#------- liste exception-------------------
list_exception_backup=['bpbqsg5520','bpyb800','bpyb100','bpyb200']
list_backup_every_month=['bpbqsg20','bpyb200','bpyb400']
#------------------------------------------

global current_GW
gbname='192.168.2.66'

def main():

    print('Fonction main ')

def getall_GW(GW):

    list_GW_BKP=['192.168.2.55','10.15.22.30','192.168.2.247']
    current_GW=list_GW_BKP[GW]
    logging.info(f'Lecture IP GW de la liste --> {current_GW}')
    print(f'Lire les GW IP {current_GW} ')


def check_job_bkb(current_GW):
        logging.info(f'check job bkb --> {current_GW} ')
        mycmand1=f'cprid_util - server {current_GW} -verbose rexec - rcmd / bin / clish - c "show interfaces " '
        mycmand2 = f'cprid_util - server {current_GW} -verbose rexec - rcmd / bin / clish - c "mgmt login user admin password 1234Alger++ " '

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
    getall_GW(2)


    logging.info('Finished logs')



