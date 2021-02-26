from apscheduler.schedulers.background import BackgroundScheduler
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from handlers import globalvars


def ipgrab():
    print("started extraction ip")
    globalvars.req_proxy_list = req_proxy.get_proxy_list()
    print("done")

minutes = 5
interval = 60 * minutes

print("loading")
req_proxy = RequestProxy()
globalvars.req_proxy_list = req_proxy.get_proxy_list()
print("done initial load")
sched = BackgroundScheduler()
sched.add_job(ipgrab, 'interval', seconds=interval)
sched.start()
print("made it here")
