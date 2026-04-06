from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

print("Starting test...")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://demo-webv1.vercel.app/")

time.sleep(2)

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")
driver.find_element(By.TAG_NAME, "button").click()

time.sleep(2)

message = driver.find_element(By.ID, "message").text
print("Result:", message)

input("Press Enter to close...")
driver.quit()