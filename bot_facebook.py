from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

path = '/home/aster/bot_selenium_chrome_90/chromedriver'
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications" : 2})
options.add_argument("--start-maximized")
browser = webdriver.Chrome(path, options=options)


browser.get('https://www.facebook.com/')

email = browser.find_element_by_id('email')
password = browser.find_element_by_id('pass')
submit = browser.find_element_by_name('login')

email.send_keys('0668237072')
password.send_keys('3152418512_aA')
submit.click()
time.sleep(10)
browser.get('https://www.facebook.com/friends/list')
time.sleep(10)
page = browser.find_element_by_xpath("//div[@aria-label='Усі друзі']")
#page = browser.find_elements_by_css_selector("[aria-label=Усі друзі]")
page.send_keys(Keys.END)

#закриття браузера
####################################################
q = input('Введіть "y" для закриття браузера: \n' )
if q == 'y' or q == 'н': 
    browser.quit()
####################################################

