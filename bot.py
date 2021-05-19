from selenium import webdriver

path = '/home/aster/bot_selenium_chrome_90/chromedriver'
browser = webdriver.Chrome(path)
browser.get('http://google.com')
