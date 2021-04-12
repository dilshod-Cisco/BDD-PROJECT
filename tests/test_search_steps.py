from selenium import webdriver
import pytest
import time
from pytest_bdd import * #'scenarios, given, when, then, parsers'

# CONSTANTS
HOME_URL = "http://automationpractice.com/"

# Scenarios (search.feature /file down below)
scenarios(".../features/search.feature")

# Fixture

@given("the store home page is displayed")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(HOME_URL)
    yield
    driver.quit()
@when("the user search for dress")
def test_search_web(browser):
    #element locators
    search_box = browser.find_element_by_name("search_query")
    search_button = browser.find_element_by_name("submit_search")

    search_box.send_keys("dress")
    search_button.click()
    print('done')
@then("at least one product is listed")
def test_verify_products_list(browser):
    # elements from the result
    products = browser.find_elements_by_css_selector(".center_column .product")
    assert len(products) >= 1
    print('search result verified')

