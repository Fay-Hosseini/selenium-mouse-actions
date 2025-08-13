import time

import pytest


from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    time.sleep(5)
    driver.quit()
