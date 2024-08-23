from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.google.com")
sleep(3)
driver.maximize_window()

def task():
    what = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    what.send_keys("whatsapp.web")
    what.send_keys(Keys.ENTER)
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()
task()
sleep(6)