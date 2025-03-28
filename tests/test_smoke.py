import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_homePage(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Load the homepage
        driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        # Check homepage elements
        assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-logo img")))
        assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-title")))
        assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".centered-image")))
        assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".spotlight2")))

        # Go to Admin page
        driver.find_element(By.LINK_TEXT, "Admin").click()
        wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("themadman")
        driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        # Confirm error message shows
        assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".errorMessage")))

        # Directory Page
        driver.find_element(By.LINK_TEXT, "Directory").click()
        wait.until(EC.presence_of_element_located((By.ID, "directory-grid")))

        # Grid view
        driver.find_element(By.ID, "directory-grid").click()
        assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gold-member p:nth-child(2)")))

        # List view
        driver.find_element(By.ID, "directory-list").click()
        assert wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gold-member p:nth-child(2)")))

        # Join Page
        driver.find_element(By.LINK_TEXT, "Join").click()

        wait.until(EC.presence_of_element_located((By.NAME, "fname"))).send_keys("austin")
        driver.find_element(By.NAME, "lname").send_keys("davis")
        driver.find_element(By.NAME, "bizname").send_keys("financepal")
        driver.find_element(By.NAME, "biztitle").send_keys("software engineer")
        driver.find_element(By.NAME, "submit").click()

        wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("testemail@gmail.com")
        driver.find_element(By.NAME, "cellphone").send_keys("801-456-4356")
        driver.find_element(By.NAME, "submit").click()

        # Optional: Add final confirmation/assertion
        success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirmation")))
        assert "Thank you" in success_message.text
