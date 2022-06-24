from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time

class InitSelenium:
    options = Options()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    options.add_argument('user-agent=' + user_agent)
    options.add_argument('disable-gpu')
    options.add_argument('log-level=3')
    options.add_argument('disable-logging')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--disable-blink-features=AutomationControlled')
    chromedriver_service = Service(chromedriver_autoinstaller.install())

    LOGIN_URL = 'https://discord.com/login'

    def __init__(self, my_id, my_password):
        self.my_id = my_id
        self.my_password = my_password

        self.driver = webdriver.Chrome(service=self.chromedriver_service, options=self.options)
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
          'source': """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

        self.driver.get(self.LOGIN_URL)

    def driver_login(self):
      while True:
        try:
          check = self.driver.execute_script('return document.querySelector(".mainLoginContainer-wHmAjP")')
          
          if check:
            input_id = self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[1]/div/div[2]/input')
            input_password = self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/div[2]/div/input')
            input_id.send_keys(self.my_id)
            input_password.send_keys(self.my_password)
            login_btn = self.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]')
            login_btn.click()
            return True
          else:
            continue

        except:
          time.sleep(0.2)

    def driver(self):
      return self.driver