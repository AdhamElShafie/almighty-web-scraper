from handlers import globalvars
from os import listdir
from functools import partial
import importlib


dir_path = "./events/"

def user_func_run(file_dir):
    func = getattr(importlib.import_module(file_dir), "scrape")
    func()

def load_dir(dir):
    command_files = [f for f in listdir(dir_path + dir) if f.endswith('.py')]

    for file in command_files:
        file_name = file.split('.')[0]
        file_dir = 'events.' + dir + '.' + file_name
        if dir == 'user':
            globalvars.ee.on(file_name, partial(user_func_run, file_dir))
        else:
            globalvars.ee.on(file_name, partial(__import__, file_dir))



for dir in ['client', 'user']:
    load_dir(dir)
