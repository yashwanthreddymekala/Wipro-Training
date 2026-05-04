from asyncio import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.microsoft import EdgeChromiumDriverManager

browser=input('what browser do you want to use?')

match (browser.lower()):
    case 'chrome':
        driver=webdriver.Chrome(service=Service('../Resources/chromedriver.exe'))
    case 'edge':
        driver=webdriver.Edge(service=Service('../Resources/msedgedriver.exe'))
    case _:
        print('unknown browser-Not available')
        driver = webdriver.Edge(service=Service('../Resources/msedgedriver.exe'))





#(service=Service(EdgeChromiumDriverManager().install())))
driver.get("https://www.google.com")

pagetitle=driver.title

if pagetitle=='Google':
    print('Google Homepage loaded-pass')
else:
    print('Google homepage not loaded-Fail')
    
sleep(3)

driver.quit()


