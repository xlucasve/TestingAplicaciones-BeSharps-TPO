# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRegister():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_register(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1440, 816)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.LINK_TEXT, "Register here").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("algo@email.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("asd123")
    self.driver.find_element(By.ID, "cpassword").click()
    self.driver.find_element(By.ID, "cpassword").send_keys("asd123")
    self.driver.find_element(By.NAME, "firstName").click()
    self.driver.find_element(By.NAME, "firstName").send_keys("John")
    self.driver.find_element(By.NAME, "lastName").click()
    element = self.driver.find_element(By.NAME, "lastName")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "lastName").send_keys("McClane")
    self.driver.find_element(By.NAME, "address1").click()
    element = self.driver.find_element(By.NAME, "address1")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "address1").send_keys(" 400 W Robinson St, Orlando, FL 32801, United States")
    self.driver.find_element(By.NAME, "address2").click()
    element = self.driver.find_element(By.NAME, "address2")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "zipcode").click()
    self.driver.find_element(By.NAME, "zipcode").send_keys("32001")
    self.driver.find_element(By.NAME, "city").click()
    element = self.driver.find_element(By.NAME, "city")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "city").send_keys("Orlando")
    self.driver.find_element(By.NAME, "state").click()
    element = self.driver.find_element(By.NAME, "state")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "state").send_keys("Florida")
    self.driver.find_element(By.NAME, "country").click()
    element = self.driver.find_element(By.NAME, "country")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "country").send_keys("United States")
    self.driver.find_element(By.NAME, "phone").click()
    element = self.driver.find_element(By.NAME, "phone")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "phone").send_keys("+1 407-246-2121")
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(13) > input").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("algo")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("algo@email.com")
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("asd123")
    self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(3) > input").click()

    user_name = self.driver.find_element(By.CLASS_NAME, "dropbtn").text
    
    assert "John" in user_name