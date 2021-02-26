name = "Amazon"

def extract_float(price):
    n_price = price.replace(',','')
    return float(n_price[1:])

def my_sorted(map_to_use):
    item_map = map_to_use
    item_map = sorted(item_map.items(), key=lambda x: extract_float(x[1][1]))
    item_map = dict((x,y) for x,y in item_map)
    return item_map

def execute():
    import logging
    from selenium.webdriver.remote.remote_connection import LOGGER
    LOGGER.setLevel(logging.WARNING)
    
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from selenium.common.exceptions import TimeoutException

    from bs4 import BeautifulSoup
    from selenium.webdriver.common.keys import Keys
    import csv, random, time
    from handlers import globalvars

    DRIVER_PATH = 'chromedriver.exe'
    SOURCE_URL = 'https://www.amazon.ca'
    NUM_PAGES = 4
    NUM_ITEMS = 100

    

    # if an error occurs where elemtn cannot be found then
    # can't run headless due to captcha
    # try to capture element name for captcha to practice
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(DRIVER_PATH, options=options)
    browser.set_page_load_timeout(3)


    while True:
        PROXY = globalvars.req_proxy_list[random.randint(0, len(globalvars.req_proxy_list)-1)].get_address()
        try:
            webdriver.DesiredCapabilities.CHROME['proxy']={
                "httpProxy":PROXY,
                "ftpProxy":PROXY,
                "sslProxy":PROXY,
                
                "proxyType":"MANUAL",
            }
            

            browser.get(SOURCE_URL)
            break
        except:
            if PROXY in globalvars.req_proxy_list:
                globalvars.req_proxy_list.remove(PROXY)
            pass

    


    # search_content = input ("What would you like to scrape?\n")
    search_content = 'scooter'

    browser.save_screenshot("sc.png")
    search = browser.find_element_by_tag_name("div")

    try:
        search = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
    except TimeoutException:
        print("oh oh..where it go?")
        return


    search.send_keys(search_content)
    search.send_keys(Keys.RETURN)
    

    search_split = search_content.split(' ')


    file_name = search_content + '_amazon_results.csv'
    f = open(file_name, 'w+', newline='', encoding='utf-8')

    c = csv.writer(f)

    c.writerow(["Item Name", "Price", "URL"])

    item_map = {}
    i = 0

    while i < NUM_PAGES and len(item_map) < NUM_ITEMS:
        html = browser.page_source
        
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all("div", {"class" : "sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20"})
        
        for item in items:
            
            name = item.find("span", {"class" : "a-size-base-plus a-color-base a-text-normal"})
            
            
            if not any(word in name.get_text().lower() for word in search_split):
                continue

            link = name.parent
            name = name.get_text()

            if link.name == 'a':
                link = link['href']
                link = SOURCE_URL + link
            
            price = item.find("span", {"class" : "a-offscreen"})
            if not price:
                continue
            
            price = price.get_text()

            item_map[id(link)] = [name, price, link]

            if len(item_map) >= NUM_ITEMS:
                break
        
        i += 1

        try:
            next_page_ele = browser.find_element_by_xpath("//li[@class='a-last']")
            next_page_ele.find_element_by_tag_name("a").click()
        except:
            break

    
    

    for ele in my_sorted(item_map):
        c.writerow(item_map[ele])

    f.close()
    browser.quit()



