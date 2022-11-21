"""  ##################################
     # Script Backup 2023  par DF5322 #
     # Domaine Corpo Hydro quebec     #    
     # Version 1.0                    #
     ################################## """


import logging
import os
import csv
import hashlib
from datetime import date

# path des fichiers + format de date ------------------------
today = date.today()
day = today.strftime("%d_%m_%Y")

format_data = "%d_%m_%y"
data_devices = '/app/PCS/bin/devices.csv'
path_dst_backup_checkpoint='/app/PCS/bin/backup_CP/'
path_dst_backup_showConf='/app/PCS/bin/backup_show_conf/'
path_dst_Log='/app/PCS/bin/logs/logbackups.log'
#------------------------------------------
#----------- LOG files parametres ---------
logging.basicConfig(filename=path_dst_Log, level=logging.DEBUG, format='%(asctime)s  %(levelname)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
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
def runMYcmd(cmd):# Excut commands checkpoint
    try:
        printv(f'commande a lancer {cmd}')
        f = os.popen(cmd)
        f=f.read()
        printv(f'resulta cmd ------------------------ >  :  {f}')        
        return f
    except Exception as er:
        printv(f'erreur  excution de la commade {er} ')

def main(): # pour test
 print('prog start')


def GW_version():
    global GAIA_embeded,Gaia,xxx
    GAIA_embeded=Gaia=xxx=False
    cmd_check_CP_version=f'cprid_util -server {current_GW} -verbose rexec -rcmd /bin/clish -c "lock database override"'
    cmd_check_CP_version=runMYcmd(cmd_check_CP_version)
    if  'R80.30' in cmd_check_CP_version:
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





def add_job_bkb(type):
    logging.info(f'Add Cron job bkb GW type {type}--> {current_GW} ')
    printv(f'Add Cron job bkb GW type {type}-->  {current_GW} ')
    if type=='CP':
     cmd_add_bkp_CP =f'set backup - scheduled  name {current_GW} of Schedule > recurrence'
     try:
         runMYcmd(cmd_add_bkp_CP)
     except Exception as e:
         logging.error(f'error cron tabs CP  {e} ')

    else:
        cmd_add_bkp_chow_conf='cat <(crontab -l) <(echo "1 2 3 4 5 scripty.sh") | crontab -'
        try:
          runMYcmd(cmd_add_bkp_chow_conf)
        except Exception as e:
          logging.error(f'error cron tabs show conf {e} ')

    cmd_clean_bkps = 'cat <(crontab -l) <(echo "1 2 3 4 5 clean.sh") | crontab -'


    runMYcmd(cmd_clean_bkps)
    logging.info(f'Add Cron job bkb GW chow_conf--> {current_GW} ')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////
def check_job_bkb():
        global Job_bkp_CP_exist,Job_bkp_show_config_exist
        Job_bkp_CP_exist=False
        Job_bkp_show_config_exist=False
        logging.info(f'check job bkb GW --> {current_GW} ')
        printv(f'check job bkb GW {current_GW}')

        cmd_check_bkp_CP =f'cprid_util -server {current_GW} -verbose rexec -rcmd /bin/bash -c "crontab -l |grep  -i bkp_daily"'
        cmd_check_bkp_chow_conf = 'crontab -l |grep  -i bkp_daily_show_conf'
        resulta_cmd_check_bkp_CP=(runMYcmd(cmd_check_bkp_CP))
        resulta_cmd_check_bkp_show_conf = (runMYcmd(cmd_check_bkp_chow_conf))

        if 'bkp_daily'  in resulta_cmd_check_bkp_CP:
            Job_bkp_CP_exist=True
            printv(f'bkb CP exist GW  --> {current_GW}  ')
            logging.info(f'  bkb CP exist GW  --> {current_GW} ')
        else:
             logging.warning(f'  bkb CP not exist !!!!  GW  --> {current_GW} ')
             add_job_bkb('CP')

        if 'bkp_daily_show_conf' in resulta_cmd_check_bkp_show_conf:
            Job_bkp_show_config_exist=True
            printv(f'bkb show conf  exist GW  --> {current_GW}  ')
            logging.info(f'  bkb show conf  exist GW  --> {current_GW} ')

        else:
            logging.warning(f'  bkb show conf not exist !!!!  GW  --> {current_GW} ')
            add_job_bkb('show_conf')


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||




#-------------------------------------------------------------------------------------------------
def trasnfer_BKP_to_manage():
    try:

       myfiles=os.system('ls -l |grep logs')
       result = hashlib.md5(((str(myfiles)).encode()))
       printv(result.hexdigest())

       printv('trasnfer_BKP_to_manage ')

       cmd_copy_cp_bkp = f'cprid_util -server {current_GW} -verbose rexec -rcmd /bin/bash -c "cp bakup{day}.gz  {path_dst_backup_checkpoint}  "'
       cmd_copy_cp_bkp = runMYcmd(cmd_copy_cp_bkp)

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
    trasnfer_BKP_to_manage()

    sync_folders()
    logging.info('Finished logs')



