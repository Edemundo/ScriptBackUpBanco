import os
import time
import datetime
import pipes

DB_HOST = '10.20.3.6'
DB_USER = 'victordesgm'
DB_USER_PASSWORD = 'covs123'
DB_NAME = 'dw_covs'
BACKUP_PATH = 'C:/Users/x506821/Documents/Projetos/ScriptBackupDW/BackupDWLocal'

# Getting current DateTime to create the separate backup folder like "20180817-123433".
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_PATH + '/' + DATETIME

# Checking if backup folder already exists or not. If not exists will create it.
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)

# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
print ("checking for databases names file.")
print ("Starting backup of database " + DB_NAME)

# Starting actual database backup process.
db = DB_NAME
dumpcmd = "mysqldump --column-statistics=0 -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
os.system(dumpcmd)

print ("")
print ("Backup script completed")
print ("Your backups have been created in '" + TODAYBACKUPPATH + "' directory")
