# from selenium import webdriver
# import pytest
# import time
#
# #CONSTANTS
# HOME_URL = "http://automationpractice.com"
#
#
#
# def test_open_home():
#     #start the browser
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#
#     # open the page
#     driver.get(HOME_URL)
#
# def test_search_web(driver):
#     # enter some keyword in the search box and click on search
#     search_box = driver.find_element_by_name("search_query")
#     search_box.send_keys('dress')
#     search_button = driver.find_element_by_name("submit_search")
#     search_button.click()
#
# def test_verify_products(driver):
#     time.sleep(3)
#     products = driver.find_element_by_css_selector("ul.product_list a.product-name")
#     # assert len(products)==0
#     print('search was successfully!')
#
# def test_close_browser(driver):
#     driver.quit()
# # use this command in the terminal and hit the enter: pytest -v -s te