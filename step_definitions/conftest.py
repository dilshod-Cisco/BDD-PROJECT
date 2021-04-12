import pytest
from selenium import webdriver
import time

# CONSTANTS
HOME_URL = "http://automationpractice.com/"

# Fixture
@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    time.sleep(3)

    print('browser opened')
    yield driver
    print('browser closing....')
    driver.quit()



