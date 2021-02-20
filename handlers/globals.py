from pymitter import EventEmitter


def initialize():
    global ee
    ee = EventEmitter()