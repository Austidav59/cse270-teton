import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1280, 800)
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_homePage(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        WebDriverWait(self.driver, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
        
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-logo img")))
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-title")))
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-news > .centered-image")))
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".spotlight1 > .centered-image")))
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".spotlight2 > .centered-image")))
        
        self.driver.find_element(By.LINK_TEXT, "Admin").click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "username"))).send_keys("testuser")
        self.driver.find_element(By.ID, "password").send_keys("themadman")
        self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
        
        assert WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".errorMessage")))
        
        self.driver.find_element(By.LINK_TEXT, "Directory").click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "directory-grid"))).click()
        assert WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")))
        
        self.driver.find_element(By.ID, "directory-list").click()
        assert WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")))
        
        self.driver.find_element(By.LINK_TEXT, "Join").click()
        fname_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "fname")))
        fname_field.send_keys("austin")
        self.driver.find_element(By.NAME, "lname").send_keys("davis")
        self.driver.find_element(By.NAME, "bizname").send_keys("financepal")
        self.driver.find_element(By.NAME, "biztitle").send_keys("software engineer")
        self.driver.find_element(By.NAME, "submit").click()
        
        email_field = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "email")))
        email_field.send_keys("testemail@gmail.com")
        self.driver.find_element(By.NAME, "cellphone").send_keys("801-456-4356")
        self.driver.find_element(By.NAME, "submit").click()
