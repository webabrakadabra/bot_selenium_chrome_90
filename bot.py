from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#chrome_options = Options()
#chrome_options.add_argument('--headless')
path = '/home/aster/bot_selenium_chrome_90/chromedriver'
browser = webdriver.Chrome(path)
browser.get('http://google.com')
