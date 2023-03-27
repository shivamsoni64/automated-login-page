import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

user = "student"
passs = "Password123"
invalide = "asdasd"
class LoginTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Users\TechInfini\Desktop\python\chromedriver.exe")
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        
    #def tearDown(self):
    #    self.driver.quit()
        
    def test_valid_credentials(self):
        time.sleep(1)
        username_input = self.driver.find_element(By.XPATH,'//*[@id="username"]')
        password_input = self.driver.find_element(By.XPATH,'//*[@id="password"]')
        time.sleep(1)
        username_input.send_keys(user)
        self.driver.execute_script("window.scrollTo(0, 200)")
        password_input.send_keys(passs)
        time.sleep(1)
        submit_button =self.driver.find_element(By.XPATH,'//*[@id="submit"]')
        submit_button.click()
        time.sleep(1)
        print(self.driver.current_url)
        error_message = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/section/div/div/article/div[2]/p[1]/strong')
        message= error_message.text
        print(message)
        
        self.assertTrue("https://practicetestautomation.com/logged-in-successfully/" in self.driver.current_url.lower())
        time.sleep(1)
        #driver.current_url == "https://practicetestautomation.com/logged-in-successfully/"
        
    def test_invalid_username(self):
        time.sleep(1)
        username_input = self.driver.find_element(By.XPATH,'//*[@id="username"]')
        password_input = self.driver.find_element(By.XPATH,'//*[@id="password"]')
        time.sleep(1)
        username_input.send_keys(invalide)
        self.driver.execute_script("window.scrollTo(0, 200)")
        password_input.send_keys(passs)
        submit_button =self.driver.find_element(By.XPATH,'//*[@id="submit"]')
        time.sleep(1)
        submit_button.click()
        time.sleep(1)
        error_message = self.driver.find_element(By.XPATH,'//*[@id="error"]')
        message= error_message.text
        print(message)
        time.sleep(1) 
        print(self.driver.current_url)
        #self.assertIn("Your username is invalid!", error_message.text.lower())
        
    def test_invalid_password(self):
        time.sleep(1)
        username_input = self.driver.find_element(By.XPATH,'//*[@id="username"]')
        password_input = self.driver.find_element(By.XPATH,'//*[@id="password"]')
        username_input.send_keys(user)
        self.driver.execute_script("window.scrollTo(0, 200)")
        password_input.send_keys(invalide)
        time.sleep(1)
        submit_button =self.driver.find_element(By.XPATH,'//*[@id="submit"]')
        submit_button.click()
        time.sleep(1)
        error_message = self.driver.find_element(By.XPATH,'//*[@id="error"]')
        message= error_message.text
        print(message)
        print(self.driver.current_url)
       # self.assertIn("Your username is invalid!", error_message.text.lower())
        
    def test_empty_fields(self):
        submit_button = self.driver.find_element(By.XPATH,'//*[@id="submit"]')
        submit_button.click()
        self.driver.execute_script("window.scrollTo(0, 200)")
        print(self.driver.current_url)
        error_message = self.driver.find_element(By.XPATH,'//*[@id="error"]')
       # self.assertIn("username and password are required", error_message.text.lower())
        message= error_message.text
        print(message)
        
        time.sleep(3) 
        #driver.find_element(By.XPATH,'//*[@id="submit"]').click()
if __name__ == "__main__":
    unittest.main()