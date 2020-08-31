from crontab import CronTab
import sys
import os
import getpass
import random


STUID = sys.argv[1]
STUID_PASSWORD = sys.argv[2]
CURRENT_DIR = os.getcwd()
CURRENT_USER = getpass.getuser()
print("Your STUID is ", STUID)
print("Your STUID_PASSWORD is ", STUID_PASSWORD)
print("Your CURRENT_DIR is ", CURRENT_DIR)
print("Your CURRENT_USER is ", CURRENT_USER)
MY_COMMOND = "python " + CURRENT_DIR + "/report.py" + " " + CURRENT_DIR + "/data_west.json" + " " + '\"' + STUID + '\"' + " " + '\"' + STUID_PASSWORD + '\"'
print(MY_COMMOND)
my_cron = CronTab(user=CURRENT_USER)
job = my_cron.new(command=MY_COMMOND)
job.setall( str(random.randint(1, 60)) + " "+ "7-22 * * *")
my_cron.write()