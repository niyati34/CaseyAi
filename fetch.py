import argparse
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import subprocess
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')  # ✅ Force UTF-8 output

# ✅ Accept inputs dynamically
parser = argparse.ArgumentParser(description="Automated login test using Selenium.")
parser.add_argument("--url", required=True, help="Website URL to test login.")
parser.add_argument("--username", required=True, help="Login username.")
parser.add_argument("--password", required=True, help="Login password.")
args = parser.parse_args()

# 🔹 Dynamic User Credentials
url = args.url
username = args.username
password = args.password

# 🔹 Configure Gemini AI
genai.configure(api_key="AIzaSyBo7AFXOGqvKLQ5CZ0w9J67QK0T_8SR43A")  # 🔴 Update with a valid API key
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# ✅ Custom Driver Setup with Fallback to Headless
def setup_driver():
    def try_driver(headless=False):
        try:
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
            driver.get(url)
            return driver
        except Exception as e:
            print(f"❌ Driver setup failed (headless={headless}): {e}")
            return None

    # Try normal mode first, then fallback to headless
    driver = try_driver(headless=False)
    if not driver:
        print("🔁 Retrying in headless mode...")
        driver = try_driver(headless=True)

    return driver

# 🚀 Initialize WebDriver
driver = setup_driver()
if not driver:
    print("❌ WebDriver initialization failed completely. Exiting.")
    sys.exit(1)

wait = WebDriverWait(driver, 10)

# 🔍 **Extract Input Fields**
print("\n🔹 Extracting Input Fields:")
input_fields_data = []
input_fields = driver.find_elements(By.TAG_NAME, "input")

for field in input_fields:
    name = field.get_attribute("name")
    id_ = field.get_attribute("id")
    type_ = field.get_attribute("type")
    placeholder = field.get_attribute("aria-label") or field.get_attribute("placeholder")
    input_fields_data.append(f"Type: {type_}, Name: {name}, ID: {id_}, Placeholder: {placeholder}")

input_fields_str = "\n".join(input_fields_data)
print(input_fields_str)

# 🔍 **Extract Submit Button (Handles All Cases)**
print("\n🔹 Extracting Submit Button:")
submit_button_data = ""

try:
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    btn_text = submit_button.text.strip() or "(No text found)"
    btn_class = submit_button.get_attribute("class")
    submit_button_data = f"✅ Found using XPath → Button Text: {btn_text}, Class: {btn_class}"
    print(submit_button_data)

except:
    print("⚠️ Submit button not found using XPath! Trying alternative methods...")
    try:
        submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit")))
        btn_text = submit_button.text.strip() or submit_button.get_attribute("value") or "(No text found)"
        btn_class = submit_button.get_attribute("class")
        submit_button_data = f"✅ Found using ID → Button Text: {btn_text}, Class: {btn_class}"
        print(submit_button_data)
    except:
        try:
            submit_button = wait.until(EC.presence_of_element_located((By.NAME, "btnLogin")))
            btn_text = submit_button.text.strip() or submit_button.get_attribute("value") or "(No text found)"
            btn_class = submit_button.get_attribute("class")
            submit_button_data = f"✅ Found using Name → Button Text: {btn_text}, Class: {btn_class}"
            print(submit_button_data)
        except:
            try:
                submit_button = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit']")))
                btn_text = submit_button.get_attribute("value") or "(No text found)"
                btn_class = submit_button.get_attribute("class")
                submit_button_data = f"✅ Found using Input Type → Button Text: {btn_text}, Class: {btn_class}"
                print(submit_button_data)
            except:
                try:
                    submit_button = wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
                    btn_text = submit_button.text.strip() or "(No text found)"
                    btn_class = submit_button.get_attribute("class")
                    submit_button_data = f"✅ Found using Generic Button Tag → Button Text: {btn_text}, Class: {btn_class}"
                    print(submit_button_data)
                except Exception as e:
                    submit_button_data = f"❌ Submit button not found! Error: {e}"
                    print(submit_button_data)

# 🛑 Close Browser
driver.quit()

# 🔹 Prepare Prompt for Gemini AI
prompt = f"""
🔹 Extracting Input Fields:
{input_fields_str}

🔹 Extracting Submit Button:
{submit_button_data}

Can you generate a Selenium test case for logging in using the extracted input fields and submit button?

- Open the website ({url}).

- Enter the provided username: {username}.
- Enter the provided password: {password}.
- Click the login button.
- Verify if the login is successful by checking the page URL or keywords for( log in is succsessfull) the page source.
- for sucsessfull indicators like generaate it as website type try multiple combinations
- Do NOT include explanations, comments, or additional text outside the Python code.
- conclude whether passed ✅test or not ❌

like The test case should:
- Open the website ({url}).
- Locate the username & password fields using ID or Name.
- Enter the provided username: {username}.
- Enter the provided password: {password}.
- Click the login button.
- Verify if the login is successful by checking the page URL or keywords in the page source.
- The script should handle missing elements gracefully.
- Import all necessary Selenium libraries.
- for sucsessfull indicators generaate it as website type try multiple combinations
- Do NOT include explanations, comments, or additional text outside the Python code.
At the end of the script, include this line:

    test_result = "✅"  # if test passed

or

    test_result = "❌"  # if test failed

This is required so we can track the result in another script.
- Don't include any extra print or explanation

"""
response = model.generate_content(prompt)
generated_code = response.text
generated_code = re.sub(r"```(?:python)?", "", generated_code).replace("```", "").strip()



try:
    exec_globals = {}
    exec(generated_code, exec_globals)
    result = exec_globals.get("test_result", "❌")  # default to failure if not set
    if result == "✅":
        sys.exit(0)
    else:
        sys.exit(1)
except Exception as e:
    sys.exit(1)
