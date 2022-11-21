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
import csv


# path des fichiers------------------------
data_devices = 'devices.csv'
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
p=True
#---------verbos print-----------
def printv(vl_to_prt):
 if p == True:
  print(vl_to_prt)
 else: 
    print('mode silent')
# --------------------------------
def runMYcmd(cmd):
    try:
        printv(f'commande a lancer {cmd}')
        f = os.popen(cmd)
        f=f.read()
        printv(f'resulta {f}')
        return f
    except Exception as er:
        printv(f'erreur  excution de la commade {er} ')

def main():
 print('prog start')





def GW_version():
    global GAIA_embeded,Gaia,xxx
    GAIA_embeded=Gaia=xxx=False
    cmd_check_CP_version=f'cprid_util -server {current_GW} -verbose rexec -rcmd /bin/clish -c "show version-software"'
    runMYcmd(cmd_check_CP_version)
    if cmd_check_CP_version in 'GAIA_embeded':
        printv(f'version {current_GW} is GAIA_embeeded')
        logging.info(f'version {current_GW} is GAIA_embeded')
        GAIA_embeded = True
    elif cmd_check_CP_version=='GAIA':
        printv (f'version {current_GW} is GAIA')
        logging.info(f'version {current_GW} is GAIA')
        Gaia=True
    else :
        printv(f'version {current_GW} is xxx')
        logging.info(f'version {current_GW} is xxx')
        xxx = True





def add_job_bkb():
    logging.info(f'Add Cron job bkb GW --> {current_GW} ')
    printv(f'Add Cron job bkb GW {current_GW} ')
    cmd_add_bkp_CP =f'set backup - scheduled  name {current_GW} of Schedule > recurrence'
    cmd_add_bkp_chow_conf='cat <(crontab -l) <(echo "1 2 3 4 5 scripty.sh") | crontab -'
    cmd_clean_bkps = 'cat <(crontab -l) <(echo "1 2 3 4 5 clean.sh") | crontab -'
    try :
        runMYcmd(cmd_add_bkp_CP)
        runMYcmd(cmd_add_bkp_chow_conf)
        runMYcmd(cmd_clean_bkps)
        logging.info(f'Add Cron job bkb GW chow_conf--> {current_GW} ')
    except Exception as e:
        logging.error(f'error cron tabs  {e} ')

def check_job_bkb():
        global Job_bkp_exist
        Job_bkp_exist=False
        logging.info(f'check job bkb GW --> {current_GW} ')
        printv(f'check job bkb GW {current_GW} ')


        cmd_check_bkp = 'crontab -l |grep  -i backup'
        runMYcmd(cmd_check_bkp)
        resulta_cmd_check_bkp_CP='0 5 * * 1 tar -zcf /var/backups/home.tgz /home/'
        resulta_cmd_check_bkp_show_conf = '0 5 * * 1 tar -zcf /var/backups_show_cnfig/home.tgz /home/'
        if resulta_cmd_check_bkp_CP =='0 5 * * 1 tar -zcef /var/backups/home.tgz /home/' and resulta_cmd_check_bkp_show_conf =='0 5 * * 1 tar -zcf /var/backups_show_cnfig/home.tgz /home/':
            Job_bkp_exist=True
        else:
             Job_bkp_exist=False
             logging.warning(f'Job bkb GW not exist GW  --> {current_GW} ')
             add_job_bkb()



def remove_bkps():
    if Job_bkp_exist == True:
      printv('remove old Backup ')
      logging.info(f' remove old Backup GW  --> {current_GW} ')
    else:
      printv('remove old Backup ')
      logging.warning(f' no Backup to remove GW --> {current_GW} ')




#-------------------------------------------------------------------------------------------------
def trasnfer_BKP_to_manage():
    try:
       cmd_transfer =' rsync - avu - -delete "/home/user/A" "/home/user/B"'
       os.system('ls -l')
       printv('trasnfer_BKP_to_manage ')
       logging.info(f' trasnfer_BKP_to_manage from GW --> {current_GW} ')
    except Exception as e :
       logging.error(f'error trasnfer_BKP_to_manage  {e} ')




def sync_folders():
    try:
       cmd_transfer =' rsync - avu - -delete "/home/user/A" "/home/user/B"'

       os.system('date')
       printv('Sync_Folders to second server  ')
       logging.info(f' Sync_Folders to second server')
    except Exception as e :
       logging.error(f'error sync {e} ')
#------------------------------------------------------------------------------------------------
def notifs(num):
    if num ==0 :
        printv('error 0 ')
    elif num == 1:
        printv('error 1')
    else:
        printv('error autre')



if __name__ == '__main__':
    global current_GW
    try:
        logging.info(f'try open file csv devices  ')
        with open(data_devices) as csvfile:
            csvReader = csv.reader(csvfile, delimiter=';')
            for row in csvReader:
                printv(row[0])
                current_GW=(row[0])
                GW_version()


        printv('Fonction main ')
    except Exception as er:
        printv(f'erreur  excution de la fcontion main  {er} ')
        logging.error(f'main : can not find file --> {er}')

    check_job_bkb()
    remove_bkps()
    trasnfer_BKP_to_manage()

    sync_folders()
    logging.info('Finished logs')



