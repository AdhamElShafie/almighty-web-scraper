from handlers import globalvars
import time

# print(__name__)
# if __name__ == '__main__':

globalvars.commands = {}
globalvars.event = {}
globalvars.initialize()


for handler in ['command_handler', 'event_handler']:
    lib = 'handlers.' + handler
    __import__(lib)


globalvars.ee.emit('ipgrab')
globalvars.ee.emit('ready')

inp = input('website?\n')

while inp.lower() != 'done':
    if inp in globalvars.commands.keys():
        globalvars.website = inp
        print('website set', inp, globalvars.website)
        globalvars.ee.emit('scrape')
    else:
        print("Sorry, I don't know how to scrape that one!")
    inp = input('website?\n')
# globals.website = inp
# for i in range(61):
#     print("? ", i)
#     time.sleep(1)


