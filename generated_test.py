from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

username = "92200103139"
password = "tree981@"

try:
    driver = webdriver.Chrome()  # Or whichever driver you're using
    driver.get("https://login.marwadiuniversity.ac.in:553/")

    try:
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtuser")))
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtpass")))
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnLogin")))
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        try:
            WebDriverWait(driver, 10).until(EC.url_contains("muonline.marwadiuniversity.ac.in")) # Example success URL
            print("✅test") 
        except TimeoutException:
           if "Dashboard" in driver.page_source or "Logout" in driver.page_source or "Welcome" in driver.page_source: # Example success keywords
             print("✅test")
           else:
             print("❌test")

    except (TimeoutException, NoSuchElementException):
        print("❌test")


finally:
    driver.quit()