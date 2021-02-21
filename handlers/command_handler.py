from . import globals
from os import listdir
import importlib
# import os
# print(os.path.abspath(os.getcwd()))

dir_path = "./commands/"

command_files = [f for f in listdir(dir_path) if f.endswith('.py')]

for file in command_files:
    file_dir = 'commands.' + file.split('.')[0].lower()
    cmd = importlib.import_module(file_dir)
    if cmd.name:
        globals.commands[cmd.name.lower()] = cmd
