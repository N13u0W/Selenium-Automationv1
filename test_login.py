from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

#run with python -m pytest -v 

#success login test case
def test_login_success(driver):

    # file
    driver.get("https://demo-webv1.vercel.app/")

    # Input data
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")

    time.sleep(10)

    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Dashboard')]"))
    )

    assert "Welcome to Dashboard" in driver.page_source

    time.sleep(10)

    #invalid login test case
def test_login_failed(driver):

    # file
    driver.get("https://demo-webv1.vercel.app/")

    # Input data
    driver.find_element(By.ID, "username").send_keys("notadmin")
    driver.find_element(By.ID, "password").send_keys("4321")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    assert "Invalid credentials!" in driver.page_source

    time.sleep(10)

    #empty login test case
def test_login_empty(driver):

    # file
    driver.get("https://demo-webv1.vercel.app/")

    # Input data

    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    assert "Please enter username and password!" in driver.page_source

    time.sleep(10)

    #username only test case
def test_login_missing_credentials1(driver):

    # file
    driver.get("https://demo-webv1.vercel.app/")

    # Input data
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    assert "Please enter password!" in driver.page_source

    time.sleep(10)

    #password only test case
def test_login_missing_credentials2(driver):

    # file
    driver.get("https://demo-webv1.vercel.app/")

    # Input data
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    assert "Please enter username!" in driver.page_source

    time.sleep(10)

    #success login+logout test case
def test_loginlogout_success(driver):

    # file
    driver.get("https://demo-webv1.vercel.app/")

    # Input data
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    time.sleep(10)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Dashboard')]"))
    )

    assert "Welcome to Dashboard" in driver.page_source
    # Logout
    driver.find_element(By.XPATH, "//button[text()='Logout']").click()

    time .sleep(10)  

    driver.quit()           