from pymitter import EventEmitter

def initialize():
    global ee
    ee = EventEmitter()
    global req_proxy_list
    req_proxy_list = []