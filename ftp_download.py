import sys
import ftplib
import os
from ftplib import FTP
from ftp_conn import ftp_conn_main
from pathlib import Path

sys.setrecursionlimit(10000)

ftp = ftp_conn_main()

def downloadFiles(path,destination):
#path & destination are str of the form "/dir/folder/something/"
#path should be the abs path to the root FOLDER of the file tree to download
    try:
        ftp.cwd(path)
        #clone path to destination
        os.chdir(destination)
        os.mkdir(destination[0:len(destination)-1]+path)
        print (destination[0:len(destination)-1]+path+" built")
    except OSError:
        #folder already exists at destination
        pass
    except ftplib.error_perm:
        #invalid entry (ensure input form: "/dir/folder/something/")
        print ("error: could not change to "+path)
        sys.exit("ending session")

    #list children:
    filelist=ftp.nlst()
    
    for file in filelist:
        try:
            #this will check if file is folder:
            ftp.cwd(path+file+"/")
            #if so, explore it:
            downloadFiles(path+file+"/",destination)
        except ftplib.error_perm:
            #not a folder with accessible content
            #download & return
            #os.chdir(destination[0:len(destination)-1]+path)
            #possibly need a permission exception catch:
            with open(os.path.join(destination,file),"wb") as f:
                print (file + "Downloading...")
                ftp.retrbinary("RETR "+file, f.write)
            print (file + " downloaded")
    return

#source="/ftproot/folder_i_want/"
source = "/user_backups/2022-12-07/"
dest = "C:/Users/Les Charfes/My Drive/BIZKIMIA/script/bkp_checker/bkp"

print(dest)
downloadFiles(source,dest)

