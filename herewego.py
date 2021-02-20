from handlers import globals

globals.commands = {}
globals.event = {}
globals.initialize()

for handler in ['command_handler', 'event_handler']:
    lib = 'handlers.' + handler
    __import__(lib)


globals.ee.emit('ready')

inp = input('website?\n')

globals.website = inp
globals.ee.emit('scrape')
