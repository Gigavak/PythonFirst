from selenium import webdriver
from webdriver_manager.driver import ChromeDriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome('/Users/roman/Downloads/chromedriver')
driver.get('https://python.org')
