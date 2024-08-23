from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

time.sleep(5)

def fill_forms():
    driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Vihaan")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Barupal")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="userEmail"]').send_keys("dineshkumar5apd@gmail.com")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="genterWrapper"]/div[2]/div[1]/label').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="userNumber"]').send_keys("6377781395")
    time.sleep(1)
    
    # Handle Date of Birth field
    date = driver.find_element(By.XPATH, '//*[@id="dateOfBirthInput"]')
    date.click()
    time.sleep(1)
    # Clear the date field using JavaScript
    driver.execute_script("arguments[0].value = '';", date)
    time.sleep(2)

    date.send_keys('02/12/2004')
    time.sleep(3)
    
    # Fill in the Subjects field using class names
    sub = driver.find_element(By.CSS_SELECTOR, '.subjects-auto-complete__value-container')
    sub.click()
    time.sleep(1)
    sub_input = driver.find_element(By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    sub_input.send_keys('Maths')
    time.sleep(2)
    sub_input.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    sub_input.send_keys(Keys.ENTER)
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[3]/label').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="currentAddress"]').send_keys('5apd(b), Srivijaynagar, Sriganganagar, Rajasthan')
    time.sleep(3)
    
    driver.find_element(By.XPATH, '//*[@id="state"]/div/div[1]/div[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="state"]/div/div[1]/div[1]').send_keys("Rajasthan")
    

    driver.find_element(By.XPATH, '//*[@id="city"]/div/div[1]/div[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="city"]/div/div[1]/div[1]').send_keys("Jaipur")
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="city"]/div/div[1]/div[1]').send_keys(Keys.ENTER)

fill_forms()
time.sleep(10)
driver.quit()
