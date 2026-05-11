import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest_check as check

@pytest.fixture(scope='function')
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get('https://www.google.com/')
    yield driver
    driver.quit()

def test_ghpload(driver):
    page_title=driver.title
    assert page_title=='Google', 'Google homepage not,loaded'


def test_imagepageload(driver):
    driver.find_element(By.LINK_TEXT,'Images').click()
    page_title=driver.title
    assert page_title=='Google Images','Google homepage not loaded'

def test_bussinesslink(driver):
    driver.find_element(By.LINK_TEXT,'Business').click()
    wait=WebDriverWait(driver,5)
    wait.until(EC.title_contains('Business'))
    #assert 'Business' in driver.title, 'Business page not loaded-Title check'
    #assert 'business' in driver.current_url, 'business page not loaded -URL check'
    check.is_in('Business', driver.title,'Business page not loaded-Title check')
    check.is_in("business",driver.current_url,"Business page not loaded-URL check")