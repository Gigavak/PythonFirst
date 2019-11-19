import pytest
from selenium import webdriver
@pytest.fixture()
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome('/Users/roman/Downloads/chromedriver')
    request.instance.driver = driver
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()

    yield driver
    driver.close()

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_title(self):
        print("Verify title...")
        assert "Selenium Easy" in self.driver.title

    def test_content_text(self):
        print("Verify content on the page...")
        centerText = self.driver.find_element_by_css_selector('.tab-content .text-center').text
        assert "WELCOME TO SELENIUM EASY DEMO" == centerText