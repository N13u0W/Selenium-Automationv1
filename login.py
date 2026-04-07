from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open login page
driver.get("https://demo-webv1.vercel.app")

# Login
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.XPATH, "//button[text()='login']").click()

time.sleep(2)

#Dashboard
if "Welcome to Dashboard" in driver.page_source:
    print("Login Success")

    # Logout (only if login success)
    driver.find_element(By.XPATH, "//button[text()='Logout']").click()
    print("Logout Done")

else:
    print("Login Failed")


input("Press Enter to close...")
driver.quit()