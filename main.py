from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


print("Starting browser...")

driver.get("https://www.google.com")

input("Press Enter to close...")
driver.quit()
