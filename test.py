from multiprocessing import Process
import time

def doWork():
    while True:
        print ("working....")
        time.sleep(10)



if __name__ == "__main__":
    p = Process(target=doWork)
    p.start()

    while True:
        time.sleep(60)