from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

try:
    driver = webdriver.Chrome()  # Or whichever browser you prefer
    driver.get("https://practicetestautomation.com/practice-test-login/")

    try:
        username_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
        login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "submit")))

        username_field.send_keys("student")
        password_field.send_keys("Password123") # Corrected password
        login_button.click()

        try:
            WebDriverWait(driver, 10).until(EC.url_contains("logged-in-successfully"))
            success_indicators = ["logged-in-successfully", "Congratulations", "Welcome"] # Example indicators
            page_source = driver.page_source
            if any(indicator in page_source for indicator in success_indicators):
                print("✅test")
            else:
                print("❌test")

        except TimeoutException:
            print("❌test")

    except (TimeoutException, NoSuchElementException):
        print("❌test")


finally:
    driver.quit()