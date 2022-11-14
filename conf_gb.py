# !/usr/bin/python3
#!/bin/bash
#source /etc/profile.d/CP.sh
# 2022 08 27 | | Script help my Linux Jobs checkpoint 1.2

from colorama import init, Fore
import pandas as pd
import hashlib
from netmiko import ConnectHandler
import ipaddress
import getpass
import sys

# ----------------- declaration variable ------------
global Mon_fichier_JSON, GREEN, RESET, RED, BLUE
connection_to_GB = False
net_connect = 'no data'
json_path = '/app/PCS/bin/'
GREEN = Fore.GREEN  # code couleur
RESET = Fore.RESET
RED = Fore.LIGHTRED_EX
BLUE = Fore.LIGHTCYAN_EX
Mon_fichier_JSON = pd.read_json(json_path + 'json_data.json')


# ----------------- FINdeclaration variable ---------


def versions():  # display les versoin gaia qui existe dans le json file  pour voir si c'est compatible
    liste_versions_gb = ['checkpoin Gaia Embeded versions :']  # tire d'affichage resulata
    for numero_test_cmd in range(Mon_fichier_JSON.shape[0]):  # lecture les Object lignes Json file
        for version_md5 in range(len(Mon_fichier_JSON['md5'][numero_test_cmd])):
            for data_dict_compr_json_md5 in Mon_fichier_JSON['md5'][numero_test_cmd][version_md5].keys():
                liste_versions_gb.append(data_dict_compr_json_md5)
    liste_versions_gb = list(dict.fromkeys(liste_versions_gb))
    for list_v in liste_versions_gb:
        print(list_v)


# DEBUT validateur de format de IP
def validateur_format_IP(MYIP):
    global valideIP
    try:
        ipaddress.ip_address(MYIP)
        print('start connection')
        print('=================\n')
        valideIP = True
    except ValueError:
        print(F"IP address '{MYIP}' not valid please check IP format\n")
        valideIP = False


# FIN  validateur de format de IP ----------------------------------------


# DEBUT ------------------- Initiation de Connection -------------------------
def connection_GB_HQ_fonc():
    global connection_to_GB, net_connect
    for i in range(1, 4):
        if connection_to_GB == False:
            print('----------------------------------\n')
            print(f" *** Tentaives : {i}/3  *** \n ")
            input_IP = input("IP du GB: ")
            username_GB = input("User: ")
            p = getpass.getpass()
            print('----------------------------------\n\n')
            input_IP = "192.168.2.66"
            username_GB = "admin"
            password_GB = "1234Alger++"

            mycheckpoint = {
                "device_type": "checkpoint_gaia",
                "ip": input_IP,
                "username": username_GB,
                "password": password_GB
            }
            validateur_format_IP(input_IP)
            if valideIP == True:
                try:
                    net_connect = ConnectHandler(**mycheckpoint)
                    connection_to_GB = True
                except Exception as e:
                    print(e)
                #except:
                 #   print(f"{RED} Attention  !!!!       check your IP or User or Password      !!!{RESET}")


# FIN  ------------------- Initiation de Connection -------------------------


#  DEBUT  --------------------------------------lire le fichier json et excuté les comande clish
def lancement_cmd_checkpoint():
    if connection_to_GB == True:
        list_rsulta_vert=[]
        list_rsulta_rouge=[]
        nbr_true = 0
        nbr_false = 0

        for numero_test_cmd in range(Mon_fichier_JSON.shape[0]):  # lecture les Object ligne Json
            match = False

            checkpoint_cmd = (Mon_fichier_JSON['cmd'][numero_test_cmd])
            Titre_etapes_cmd = (Mon_fichier_JSON['name'][numero_test_cmd])
            print(f"{RESET}% Etapes:  {Titre_etapes_cmd} {RESET} %")
            output = net_connect.send_command(checkpoint_cmd)
            print(output)
            md5_vlue = hashlib.md5(output.encode()).hexdigest()

            longeur_mymd5 = len(Mon_fichier_JSON['md5'][numero_test_cmd])

            for version_md5 in range(longeur_mymd5):

                for data_dict_compr_json_md5 in Mon_fichier_JSON['md5'][numero_test_cmd][version_md5].values():
                    if md5_vlue == data_dict_compr_json_md5:  # Validateur de MD5 a partir du resulta et compar avec Json
                        match = True

            if match == True:
                print(f"{GREEN}{md5_vlue} -----------> Match \U0001f600   {RESET}")
                nbr_true += 1
                list_rsulta_vert.append({Titre_etapes_cmd})
            else:
                print(f"{RED}{md5_vlue} ---> No Match Value \U0001F620 !!! {RESET}")
                nbr_false += 1
                list_rsulta_rouge.append({Titre_etapes_cmd})

            print(f"{RESET}Fin Etapes : {Titre_etapes_cmd} {RESET}")
            print(f"{BLUE}___________________________________________\n{RESET}")

        net_connect.disconnect()

        #print(f"| Total Réussi : {GREEN}{nbr_true} : {list_rsulta_vert} {RESET} |\n| Total Echec {RED} : {nbr_false} : {list_rsulta_rouge}{RESET} |")
        print(f"| Conforme HQ  : {GREEN}{nbr_true} ")
        print(*list_rsulta_vert,sep="\n")
        print(f"|{RESET} Non Conforme HQ : {RED} {nbr_false}")
        print(*list_rsulta_rouge, sep="\n")



    #  FIN -------------------------------Lire le fichier json et excuté les comande clish-----------------------------


def backup():
    print('please Wait')

    print('2')
    output = net_connect.send_command('backup automatic-mode')
    print(output)
    print('2')


def start(A):
    if A == '-d':
        print('display compatible version :')
        versions()
        sys.exit()


    elif A == '-b':
        try:
            print('start Backup config GB \n ')
            connection_GB_HQ_fonc()
            backup()
            net_connect.disconnect()
        except:
            sys.exit()

    elif A == '-v':
        try:
            print('start Backup config GB \n ')
            connection_GB_HQ_fonc()
            lancement_cmd_checkpoint()
            net_connect.disconnect()
        except:
            sys.exit()

    elif A == '-c':
        try:
            print('start validation config GB \n')
            connection_GB_HQ_fonc()
            print('start configuration')
            net_connect.disconnect()
        except:
            sys.exit()
    else:
        print(' scriptname.py [-d]      -Dispaly version of config supported ')
        print('               [-v]      -Run validation configuration FW  ')
        print('               [-c]      -start la configuration du FW  ')
        print('               [-b]      -Backup configuration du GB  ')
        sys.exit()


if __name__ == "__main__":  # simple loop de 3 tentative
    global A
    try:

        A = (sys.argv[1])
        start(A)

    except IndexError:
        start('ddd')
        sys.exit()
