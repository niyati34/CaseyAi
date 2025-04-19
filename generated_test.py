from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

try:
    driver = webdriver.Chrome()  # Or whichever browser you prefer
    driver.get("https://practicetestautomation.com/practice-test-login/")

    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "submit"))
        )

        username_field.send_keys("student")
        password_field.send_keys("Password123")
        submit_button.click()

        try:
            WebDriverWait(driver, 10).until(
                lambda driver: "Logged In Successfully" in driver.page_source or
                              driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"
            )
            print("✅test")
        except TimeoutException:
            print("❌test")


    except (NoSuchElementException, TimeoutException):
        print("❌test")

finally:
    driver.quit()