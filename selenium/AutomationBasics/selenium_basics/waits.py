import time


from selenium.webdriver.support.expected_conditions import element_to_be_clickable


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge(service=Service('../Resources/msedgedriver.exe'))
driver.get("https://www.google.com")

'''driver.implicitly_wait(5)

search_input=driver.find_element(By.NAME,"q")
search_input.send_keys(("locators"))
googlesearch_button=driver.find_element(By.NAME, "btnK")
googlesearch_button.click()'''

wait=WebDriverWait(driver, 10)

search_box=wait.until(EC.visibility_of_element_located(By.NAME, "q"))
search_box.send_keys('explicit wait')

google_search_button=wait.until(element_to_be_clickable(By.NAME,'btnK'))
google_search_button.click()
