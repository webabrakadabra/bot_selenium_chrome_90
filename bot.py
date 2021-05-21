from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

path = '/home/aster/bot_selenium_chrome_90/chromedriver'
browser = webdriver.Chrome(path)
browser.get('https://accounts.google.com/servicelogin')

if 'cookies' in os.listdir():
    for cookies in pickle.load(open('cookies', 'rb')):
        browser.add_cookie(cookies)
    time.sleep(5)
    browser.refresh()


#ua = UserAgent()
#opts = Options()
#opts.add_argument('user-agent=' + ua.google)
else:
    emailElem = browser.find_element_by_id('identifierId').send_keys('tabl26438')
    btn_elem = browser.find_element_by_id('identifierNext').click()

    passwordLogin=WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='password']")))
    passwordLogin.send_keys('tabl26438_11111')
    btn_elem = browser.find_element_by_id('passwordNext').click()



    passw = ''

    #cookie
    pickle.dump(browser.get_cookies(), open("cookies", "wb"))

q = input('Введіть "y" для закриття браузера: \n' )

if q == 'y' or q == 'н': 
    browser.quit()

browser.quit()
