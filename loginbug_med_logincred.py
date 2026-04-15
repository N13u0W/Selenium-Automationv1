from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


options =Options()

options.add_argument("user-data-dir=C:/ChromeTestProfile")  # Change to your desired path

# Setup driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
options=options
)


# Open your local HTML file (CHANGE PATH)
driver.get("https://mini-bug-tracker-v1.vercel.app/")

time.sleep(2)

# Input data
driver.find_element(By.ID, "title").send_keys("Login Bug")
driver.find_element(By.ID, "description").send_keys("Login credentials not working")

# Select severity
severity_dropdown = Select(driver.find_element(By.ID, "severity"))
severity_dropdown.select_by_visible_text("Medium")

# Click Add Bug button
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

# Verify bug added (check table)
table = driver.find_element(By.ID, "bugTable").text

if "Login Bug" in table:
    print("✅ Bug successfully added!")
else:
    print("❌ Bug not added!")

# Keep browser open
input("Press Enter to close...")
driver.quit()