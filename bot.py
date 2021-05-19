from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options


ua = UserAgent()

opts = Options()
opts.add_argument("user-agent=" + ua.google)
print(ua.google)
path = '/home/aster/bot_selenium_chrome_90/chromedriver'
browser = webdriver.Chrome(path, options=opts)
browser.get('https://accounts.google.com/')
login = browser.find_element_by_id('identifierId').send_keys('haha')

passw = ''

Thread.sleep(5000)
browser.quit()
