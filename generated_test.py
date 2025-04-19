from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")
    username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    submit_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "submit")))
    username_field.send_keys("student")
    password_field.send_keys("Password123")
    submit_button.click()
    time.sleep(2)  # Allow time for page load after login
    if "Logged In Successfully" in driver.page_source or driver.current_url == "https://practicetestautomation.com/logged-in-successfully/":
        print("✅test")
    else:
        print("❌test")
except Exception as e:
    print("❌test")
finally:
    driver.quit()