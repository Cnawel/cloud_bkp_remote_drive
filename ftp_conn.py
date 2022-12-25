#ftp_connect.py
# Script de conexión a FTP, listado de archivos, propiedades de archivos
# funciones: conectar a ftp, listar archivos, propiedades (tamaño, permisos, fecha creacion, fecha ultima mod)

from ftplib import FTP
import configparser
import os


## Get directory path
dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = dir_path + "./config.txt"

# Init configParser and read file
config = configparser.ConfigParser()
config.read(file_path)

#print(config.sections())

#conecto a archivo config.txt y paso parametros a variables
ftp_host = config.get('login', 'ftp_host').strip()
ftp_user = config.get('login', 'ftp_user')
ftp_pass  = config.get('login', 'ftp_pass')

ftp_directory = '/domains/'

#print(type(ftp_host), type(ftp_pass), type(ftp_user))


#ftp = ftplib.FTP('')
def ftp_conn_main():
    ftp_conn = FTP(ftp_host)

    # # # LOGS
    print(f"Connected to FTP server ", ftp_host)

    ftp_conn.getwelcome()

    ftp_conn.login(user = ftp_user, passwd = ftp_pass, acct = '')

    return ftp_conn
    # # # LOG print(f"Login successfull with username = ", ftp_user)
    # # # '230 Login successful.'

    #print(direc_content)
    # # type(direc_content)
    #ftp_conn.close()

# ftp = ftp_conn_main()
# # changing directory
# ftp.cwd('user_backups')  
# ftp.retrlines('LIST')



