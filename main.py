from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from initselenium import InitSelenium
import time
import json
import random

with open('./config.json', 'r') as f:
  config_data = json.load(f)
  my_id = config_data['my_id']
  my_password = config_data['my_password']
  CHANNEL_URL = config_data['CHANNEL_URL']
  chat_delay = config_data['chat_delay']
  words = config_data['words']
  f.close()

def words(now_time, pre_word):
  for word in words:

    if word == pre_word:
      new_words = []

      for new_word in words:
        if new_word != word:
          new_words.append(new_word)
      return new_words

  return words

if __name__ == '__main__':
  s = InitSelenium(my_id, my_password)

  if s.driver_login():
    input('After hcaptcha press a key to continue')
  
  s.driver.get(CHANNEL_URL)
  connet_success = s.driver.execute_script('return document.readyState')

  while str(connet_success) != 'complete':
    s.driver.get(CHANNEL_URL)
    time.sleep(1)

  channel_loading = False  

  while not channel_loading: 
    try:
      input_box = s.driver.find_element(By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div[2]/main/form/div/div/div/div[1]/div/div[3]/div/div[2]')
      channel_loading = True
    except:
      time.sleep(1)

  chat_count = 1
  random_word = ''

  while True:
    words_list = words(current_m, random_word)
    random_int = random.randint(0, len(words_list)-1)
    random_word = words_list[random_int]

    try:
      input_box.send_keys(random_word)
      input_box.send_keys(Keys.RETURN)
    except:
      continue

    print(f'now chat count:{chat_count}')
    chat_count+=1
    time.sleep(chat_delay)
  

  


