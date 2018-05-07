import schedule
import os
import time

#Remove uploaded files
def remove():
    os.system('rm static/tmp/*')

schedule.every(30).minutes.do(remove)

while True:
    schedule.run_pending()
    time.sleep(1)
