import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service('../Resources/msedgedriver.exe'))
driver.get("https://www.google.com")
#id
'''search_input=driver.find_element(By.ID,"APjFqb")
search_input.send_keys(("selenium"))
time.sleep(3)
search_input.clear()
'''

'''search_input=driver.find_element(By.NAME,"q")
search_input.send_keys(("locators"))
time.sleep(3)

'''
'''#Name
googlesearch_button=driver.find_element(By.NAME, "btnK")
googlesearch_button.click()
time.sleep(3)'''
'''
#classname
imfl_button=driver.find_element(By.CLASS_NAME,"RNmpXc")
imfl_button.click()
time.sleep(3)'''

'''#tag name
href_elements=driver.find_elements(By.TAG_NAME,"a")
for elmt in href_elements:
    print(f'{elmt.text} - {elmt.get_attribute("href")}')'''

'''#linktext
images_link=driver.find_element(By.LINK_TEXT,"Images")
images_link.click()
time.sleep(3)'''

'''#partial linktext
images_link=driver.find_element(By.PARTIAL_LINK_TEXT,"ma")
images_link.click()
time.sleep(3)'''

#css selectors
search_css=driver.find_element(By.CSS_SELECTOR,'div > textarea' )
search_css.send_keys('selenium')
time.sleep(3)
