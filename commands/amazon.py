name = "Amazon"
def execute():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from selenium.webdriver.common.keys import Keys
    import time
    import csv


    DRIVER_PATH = 'chromedriver.exe'


    browser = webdriver.Chrome(DRIVER_PATH)
    browser.get('https://www.amazon.ca')


    search_content = input ("What would you like to scrape?\n")
    search = browser.find_element_by_id('twotabsearchtextbox')

    search.send_keys(search_content)
    search.send_keys(Keys.RETURN)
    time.sleep(5)



    pages = 3
    search_split = search_content.split(' ')

    file_name = search_content + '_amazon_results.csv'
    f = open(file_name, 'w', newline='', encoding='utf-8')

    c = csv.writer(f)

    c.writerow(["Item Name", "Price"])

    for i in range(pages):
        html = browser.page_source
        
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all("div", {"class" : "sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col sg-col-4-of-20"})

        
        for item in items:
            
            name = item.find("span", {"class" : "a-size-base-plus a-color-base a-text-normal"}).get_text()
            
            if not any(word in name.lower() for word in search_split):
                continue

            price = item.find("span", {"class" : "a-offscreen"})
            if not price:
                continue
            
            price = price.get_text()
            c.writerow([name, price])
            
        try:
            next_page_ele = browser.find_element_by_xpath("//li[@class='a-last']")
            next_page_ele.find_element_by_tag_name("a").click()
            time.sleep(5)
            
        except:
            break

    f.close()
    browser.quit()