import schedule
import time

def job():
    print "Hello Srishail!!"

schedule.every(5).seconds.do(job)
while 1:
    schedule.run_pending()
    time.sleep(1)