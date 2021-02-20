from handlers import globals
from os import listdir
from functools import partial

msg = globals.website

if not msg or msg == '':
    print("No input given")

cmd = msg.lower()

command = globals.commands.get(cmd)

if command:
    command.execute()