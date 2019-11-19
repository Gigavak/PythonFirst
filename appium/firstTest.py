from appium import webdriver


desired_caps = {
    "deviceName": "Pixel",
    "platformName": "Android",
    "version" : "10",
    "realDevice": True,
    "browserName": "chrome",
    "automationName": "uiautomator2"
}

driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", desired_caps)
driver.get('https://www.google.com')
driver.quit()