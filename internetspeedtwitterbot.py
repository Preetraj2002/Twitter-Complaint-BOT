import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options=Options()
options.add_experimental_option("detach",True)
options.add_argument("start-maximized")


chrome_driver_path="C:\\Users\\USER\\Desktop\\my_python\\chromedriver.exe"
website_URL='https://speedtest.net'

driver=webdriver.Chrome(service_log_path=chrome_driver_path,options=options)

# TWITTER_ID=
# TWITTER_PASSWORD=


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up=10
        self.down=150

    def get_internet_speed(self):
        driver.get(website_URL)
        time.sleep(5)
        print("Site opened Successfully")
        accept=driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
        accept.click()
        go=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        time.sleep(60)
        print("Printing the speeds")
        self.down=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up=driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print("Down="+self.down)
        print("Up="+self.up)
        driver.close()

    def tweet_at_provider(self):
        driver.get('https://twitter.com')
        time.sleep(5)






