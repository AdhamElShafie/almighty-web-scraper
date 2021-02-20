from . import globals
from os import listdir
from functools import partial

dir_path = "./events/"

def load_dir(dir):
    command_files = [f for f in listdir(dir_path + dir) if f.endswith('.py')]

    for file in command_files:
        file_name = file.split('.')[0]
        file_dir = 'events.' + dir + '.' + file_name
        
        globals.ee.on(file_name, partial(__import__, file_dir))



for dir in ['client', 'user']:
    load_dir(dir)
