import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime as sdt
import datetime


def do():
    for i in range(10):
        print(i)
        time.sleep(1)


print('OO ME ME ME')

sched = BackgroundScheduler()
    
interval = 30

deltasec = datetime.timedelta(seconds=29)

dt = sdt.now()

dt = dt - deltasec

sched.add_job(do, 'interval', seconds=interval, start_date=dt)
sched.start()
