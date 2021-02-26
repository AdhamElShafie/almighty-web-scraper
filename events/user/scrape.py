from handlers import globalvars
import traceback

def scrape():
    try:
        msg = globalvars.website
        print('h1')
        cmd = msg.lower()

        command = globalvars.commands.get(cmd)
        print('h2')
        if command:
            print('h3')
            command.execute()
    except:
        print("No input given")
        traceback.print_exc()
    

