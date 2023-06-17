from random import randint
import sys
import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class Instabot:
    def __init__(self, config_path, username):
        with open(config_path) as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)
        self.driver = webdriver.Chrome(service=Service(self.config['driver_path']))
        #chrome = webdriver.Chrome(options=chrome_options) 
        #print(self.config)
        self.login(username)

    def login(self, username):
        PROXY = "IpOfTheProxy:PORT" 
        options = webdriver.ChromeOptions() 
        options.add_argument("--proxy-server=%s" % PROXY) 
        options.add_argument("--headless")
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        # Adding argument to disable the AutomationControlled flag 
        options.add_argument("--disable-blink-features=AutomationControlled") 
        # Exclude the collection of enable-automation switches 
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
        # Turn-off userAutomationExtension 
        options.add_experimental_option("useAutomationExtension", False) 
        # Setting the driver path and requesting a page 
        driver = webdriver.Chrome(options=options) 
        # Changing the property of the navigator value for webdriver to undefined 
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'username').send_keys(self.config['login']['username'])
        self.driver.find_element(By.NAME, 'password').send_keys(self.config['login']['password'])
        self.driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
        time.sleep(5)

    def remove_followers(self, keep_followers_list=None):
        # Navigate to your followers list
        self.driver.get("https://www.instagram.com/" + self.config['login']['username'])
        time.sleep(5)
        self.driver.find_element("xpath", "//a[contains(@href,'/followers')]").click()
        time.sleep(10)
        fBody  = self.driver.find_element("xpath", "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]") 
        for i in range(1,110):
            time.sleep(randint(5,7))
            follower_name = self.driver.find_element("xpath", f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div").text
            if follower_name not in keep_followers_list:
                 follower = self.driver.find_element("xpath", f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]")
                 removebutton0 = follower.find_element("xpath", f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{i}]/div/div/div/div[3]/div/div")
                 time.sleep(randint(7, 27))
                 removebutton0.click()
                 time.sleep(randint(4, 25))
                 removebutton1 = self.driver.find_element("xpath", "/html/body/div[2]/div/div/div[3]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]")
                 removebutton1.click()
                 time.sleep(randint(3, 7))
            if i % 5 == 0:
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                time.sleep(randint(5, 10))
            
    def remove_following(self, keep_followers_list=None):
        self.driver.get("https://www.instagram.com/" + self.config['login']['username'])
        time.sleep(5)
        self.driver.find_element("xpath", "//a[contains(@href,'/following')]").click()
        time.sleep(10)
        fBody  = self.driver.find_element("xpath", "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]") 
        for i in range(1,582):
            time.sleep(randint(5,7))
            follower_name = self.driver.find_element("xpath", f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[2]/div/div/span[1]/span/div/div/div/a/span/div").text
            if follower_name not in keep_followers_list:
                 follower = self.driver.find_element("xpath", f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]")
                 removebutton0 = follower.find_element("xpath", f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]/div/div/div/div[3]/div/button")
                 time.sleep(randint(7, 27))
                 removebutton0.click()
                 time.sleep(randint(4, 25))
                 removebutton1 = self.driver.find_element("xpath", "/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[1]")
                 removebutton1.click()
                 time.sleep(randint(3, 7))
            if i % 5 == 0:
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                time.sleep(randint(5, 10))

    def close(self):
        self.driver.close()

if __name__ == '__main__':
    instabot = Instabot('config/config.yml', sys.argv[1])
    keep_followers_list = []
    instabot.remove_following(keep_followers_list)
    instabot.close()