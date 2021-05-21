from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

path = '/home/aster/bot_selenium_chrome_90/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get("https://accounts.google.com/servicelogin")
emailElem = driver.find_element_by_id('identifierId').send_keys('tabl26438')
btn_elem = driver.find_element_by_id('identifierNext').click()

''' працює '''
#passwordLogin=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".whsOnd.zHQkBf[name='password']")))
#passwordLogin.send_keys('tabl26438_11111')

''' не працює '''
#passwordLogin=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.NAME,"password")))
#passwordLogin.send_keys('tabl26438_11111')

''' працює '''
passwordLogin=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='password']")))
passwordLogin.send_keys('tabl26438_11111')

btn_elem = driver.find_element_by_id('passwordNext').click()


