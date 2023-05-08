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
        #print(self.config)
        self.login(username)

    def login(self, username):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(10)
        self.driver.find_element(By.NAME, 'username').send_keys(self.config['login']['username'])
        self.driver.find_element(By.NAME, 'password').send_keys(self.config['login']['password'])
        self.driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
        time.sleep(5)

    def remove_followers(self, keep_followers_list=None):
        # Navigate to your followers list
        self.driver.get("https://www.instagram.com/" + self.config['login']['username'])
        time.sleep(5)
        self.driver.find_element("xpath", "//a[contains(@href,'/followers')]").click()
        time.sleep(5)
        # wait for page to load
        # Get all the followers
        self.driver.find_element("xpath", "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button").click()
        time.sleep(5)
        #follower = self.driver.find_element("xpath", "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]")
        #button = follower.find_element("xpath", "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[3]/div/div")
        #button = follower.driver.find_element(By.CSS_SELECTOR, "//div//button[div[text()='Remove']")
        #follower.click()
        #print(follower)
        
        #print(followers)
        # Remove the followers that are in the keep_followers_list
        # if keep_followers_list:
        #     followers = [f for f in followers if f.text.split("\n")[0] not in keep_followers_list]
        # # Unfollow the remaining followers
        # for follower in followers:
        #     # Get the follow button of the follower
        #     button = follower.find_element("xpath", "//button[text()='Remove']")
        #     button.click()
        #     # Click the "Unfollow" button on the unfollow confirmation popup
        #     self.driver.find_element("xpath","//button[text()='Remove']").click()
        #     # Wait for 2 seconds before unfollowing the next user
        #     time.sleep(2)
        print("done")

    def close(self):
        self.driver.close()

if __name__ == '__main__':
    instabot = Instabot('config/config.yml', sys.argv[1])
    keep_followers_list = ['francisco.moreira15', 'haley.lowenthal', '84nrogers', 'ellarudisill', 'khe_levy', 'chesniecheung', 'j1njee', 'nickyph34', 'billtrn_', 'williemears', 'mortn4sty', 'jason.hwong', 'sam.rubin99', 'priyaabakshi', 'genna.bishop', 'freddie_lemons', 'mala.krish', 'rayan.tzd', 'pono_demarzo', 'averyychen', '_xuanyi.wang', 'fernseph', 'sana.aladin']
    instabot.remove_followers(keep_followers_list)
    instabot.close()
