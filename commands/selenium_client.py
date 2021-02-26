import abc, random
from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import os
# print(os.getcwd())



# 
#   OK SO IDK WHY THIS IMPORT STOPPED WORKING ALL OF A SUDDEN BUT ANYWAY
#   NEED TO WORK ON DECIDING WHERE THE DRIVER CREATION HAPPENS: HERE OR CHILD CLASS
#   THEN NEED TO FIGURE OUT HOW TO DO THIS STUFF CONCURRENTLY FOR TIME
#   THEN NEED TO RE-IMPLEMENT THE FUNCTIONS HERE IN CHILD CLASSES FOR SCRAPING
# 



from handlers import globalvars


class SeleniumClient(ABC):

    DRIVER_PATH = 'chromedriver.exe'

    SOURCE_URL : str

    NUM_PAGES : int

    NUM_ITEMS : int


    options = Options()
    options.headless = True
    
    browser = webdriver.Chrome(DRIVER_PATH, options=options)
    browser.set_page_load_timeout(3)


    def load_page(self):
        while True:
            PROXY = globalvars.req_proxy_list[random.randint(0, len(globalvars.req_proxy_list)-1)].get_address()
            try:
                webdriver.DesiredCapabilities.CHROME['proxy']={
                    "httpProxy":PROXY,
                    "ftpProxy":PROXY,
                    "sslProxy":PROXY,
                    
                    "proxyType":"MANUAL",
                }
                

                self.browser.get(self.SOURCE_URL)
                break
            except:
                if PROXY in globalvars.req_proxy_list:
                    globalvars.req_proxy_list.remove(PROXY)
                pass

    @abstractmethod
    def search(self):
        raise NotImplementedError('WHAT LOOKING FOR?')

    @abstractmethod
    def write_to_file(self, fname):
        raise NotImplementedError('WHERE PUT RESULT?')

    @abstractmethod
    def execute(self):
        raise NotImplementedError('BRUH...HOW YOU GONNA RUN THIS?')