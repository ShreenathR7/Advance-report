from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.keys import Keys
from Test_data import data
from Test_locators import locators
from time import sleep
import pytest

class login:
     @pytest.fixture
    
   
     def booting_function(self):
       self.driver =webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
     def issuse(self,booting_function):   
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(20)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().billing).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().issue).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_issuse).click()
    
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Select_branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        branch.send_keys(data.Logi_Data().branch_name)
        branch.send_keys(Keys.RETURN)
        assert self.driver.title == "Logimax Technology | Admin"
        print(f"Selected Branch : {data.Logi_Data().branch_name}")
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Refund).click()
        sleep(5)
        customer = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().name)
        sleep(5)
        customer.send_keys('9568')
        sleep(20)
        customer.send_keys(Keys.BACK_SPACE)
        sleep(30)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li")
        customer_name = 'PRAKASH-9568724563'
        for element in se_ver:
            if element.text == customer_name:
                element.click()
                break
        assert self.driver.title == "Logimax Technology | Admin"    
        print(f'Customer Name & Mobile No: {customer_name}')   
        
        sleep(5)
        Issuse_Balance_Amount = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Advance_Amount)
        #print(Receipt_calculation)
        Issuse_Total_Balance = []
        Issuse_Total_Balance_Amount =0
        
        for value in  Issuse_Balance_Amount:
            Total = value.text
            int_value = int(Total.replace(',', '').replace('.00', ''))
            Issuse_Total_Balance.append(int_value)
            Issuse_Total_Balance_Amount += int_value  # Add each value to the total
           
            
        print(f"Total  Balance : {Issuse_Total_Balance}")
        print("Total_Balance_Amount : ", Issuse_Total_Balance_Amount)
        sleep(5)
        excepted_balance_amount = 219109
        if excepted_balance_amount == Issuse_Total_Balance_Amount:
           print('Total Balance Amount Calculation verify successfully')
        else:
           print(f"Balance Amount : {Issuse_Total_Balance_Amount} which is not within the expected output")              
        
