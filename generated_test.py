import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def test_login(self):
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            password_field = self.driver.find_element(By.ID, "password")
            submit_button = self.driver.find_element(By.ID, "submit")

            username_field.send_keys("student")
            password_field.send_keys("Password123")
            submit_button.click()

            WebDriverWait(self.driver, 10).until(
                EC.url_contains("logged-in-successfully")
            )
            
            print("✅test")

        except Exception as e:
            print("❌test")
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()