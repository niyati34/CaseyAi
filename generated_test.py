from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

username = "student"
password = "kmklnl"

try:
    driver = webdriver.Chrome()  # Or whichever driver you prefer
    driver.get("https://login.marwadiuniversity.ac.in:553/")

    try:
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtuser")))
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtpass")))
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnLogin")))

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        try:
            WebDriverWait(driver, 10).until(EC.url_contains("mu.ac.in") or EC.title_contains("Dashboard") or EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Logout')]")))  # Example success indicators - adapt as needed for your specific site
            print("✅test")
        except TimeoutException:
            print("❌test")

    except (NoSuchElementException, TimeoutException):
        print("❌test")

finally:
    driver.quit()