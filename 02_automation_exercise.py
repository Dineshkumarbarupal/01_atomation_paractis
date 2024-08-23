from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
sleep(2)
driver.maximize_window()
sleep(2)

def form_fill():
   driver.find_element(By.XPATH, '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[2]/input').send_keys("vihaan barupal") 
   sleep(2)
   last_name = driver.find_element(By.XPATH,  '//*[@id="post-body-3077692503353518311"]/div[1]/div/div/h2[2]/div[1]/div/div[5]/input')
   if not last_name.is_selected():
      last_name.send_keys("barupal")  
   sleep(2)
   redio_button = WebDriverWait(driver,10).until(
    Ec.element_to_be_clickable((By.XPATH, '//*[@id="sex-0"]'))
   )
   redio_button.click()
   sleep(2)
   year_experiense = WebDriverWait(driver,10).until(
      Ec.element_to_be_clickable((By.XPATH, '//*[@id="exp-0"]'))
   )
   year_experiense.click()
   sleep(2)
   date = WebDriverWait(driver,10).until(
      Ec.presence_of_element_located((By.XPATH, '//*[@id="datepicker"]'))
   )
   date.send_keys("02/12/2024")
   sleep(2)
   driver.find_element(By.ID, 'profession-1').click()
   sleep(2)
   automation_tools = WebDriverWait(driver,10).until(
      Ec.element_to_be_clickable((By.ID, 'tool-2'))
   ) 
   automation_tools.click()
   sleep(2)
   driver.find_element(By.XPATH, '//*[@id="continents"]').send_keys("Asia")
form_fill()
sleep(20)
