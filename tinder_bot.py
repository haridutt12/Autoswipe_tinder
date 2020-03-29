from selenium import webdriver
from time import sleep
from secrets import username, password
import random
# from selenium.webdriver.chrome.options import Options

class TinderBot():
    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # self.driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        try:
            option_btm = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            print("1 was called")
            option_btm.click()
        except Exception:
            try:
                fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            except Exception:
                fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button/span[2]')
            fb_btn.click()

        self.driver.implicitly_wait(20)

        try:
            print("2 was called")
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        except Exception:
            fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
            print("3 was called")

        fb_btn.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        pop_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        pop_1.click()

        pop_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div')
        pop_2.click()

        pop_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
        pop_3.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dis_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dis_btn.click()

    def auto_swipe(self):
        print("i was executed")
        while True:
            try:
                r = random.randint(1,4)
                sleep(r)
                threshold = random.random()
                if threshold > 0.5:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
sleep(5)
bot.auto_swipe()

# bot.like()
