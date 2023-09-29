# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from time import sleep
from Test_locators import locators
from Test_data import data
from Test_Billing_code import tes
import pytest
import subprocess

class Test_Logimax:
   @pytest.fixture
    
   
   def booting_function(self):
       self.driver =webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
   
   
   def test_Billing(self,booting_function):   
        self.driver.find_element(By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(20)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        subprocess.run(["python","test_bill_code.py"])
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Sales_Report).click()
        sleep(5)
        element = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Sales_Report).text
        expected_title = "Sales Report"
        actual_title = element
        assert expected_title == actual_title,f"Expected '{expected_title}' but got '{actual_title}'"
        print(f"Clickable Option = {expected_title}")
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Advance_Detailed_Report).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        branch.send_keys(data.Logi_Data().branch_name)
        branch.send_keys(Keys.RETURN)
        assert self.driver.title == "Logimax Technology | Admin"
        print(f"Selected Branch : {data.Logi_Data().branch_name}")
      
        sleep(5)
        
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Date_range).click()
      
        sleep(5)
        date_input = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Start_date)
        date_input.clear() 
        date_input.send_keys(data.Logi_Data().first_date)
        assert self.driver.title == "Logimax Technology | Admin"
        print(f"From date : {data.Logi_Data().first_date}")
      
        sleep(5)
        
        End_date_input = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().end_date)
        End_date_input.clear() 
        End_date_input.send_keys(data.Logi_Data().last_date)
        assert self.driver.title == "Logimax Technology | Admin"
        print(f"To date : {data.Logi_Data().last_date}")
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().apply).click()
        sleep(5)
        
      
        customer = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Mobile_No)
        sleep(5)
        customer.send_keys('9568')
        sleep(20)
        customer.send_keys(Keys.BACK_SPACE)
        sleep(30)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li")
        customer_name = '9568724563-PRAKASH'
        for element in se_ver:
            if element.text == customer_name:
                element.click()
                break
        assert self.driver.title == "Logimax Technology | Admin"    
        print(f'Customer Name & Mobile No: {customer_name}')   
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().search).click()
   
        Name = 'PRAKASH'
        
        mobile = '9568724563'
        
        Receipt_Amount = '2,60,000'
        
        utilized_Amount  = '35,891'
        
        Transfer = '5,000'
        
        balance_Amount = '2,19,109'
                
    
        sleep(5)
        table = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Name)
        
        a = []
        for i in table:
           v=i.text
           a.append(v)
           b = ' '.join(a)
        #print(a)  
        if Name in a :
              print(f"Customer Name :{Name}")
        else:
           print(f"Customer Name is visible : {a} which is not within the expected output")      
                    
              
        sleep(5)
        mobile_no = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().mobile)
        a = []
        for i in mobile_no:
           v=i.text
           a.append(v)
           b = ' '.join(a)
        #print(a)  
        if  mobile in b :
              print(f'Mobile Number : {mobile}')   
        else:
           print(f"Mobile Number is visible : {b} which is not within the expected output")      
                      
         
        amount = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Receipt_Amount)
        a = []
        for i in amount:
           v=i.text
           a.append(v)
           b = ' '.join(a)
        #print(a)  
        if Receipt_Amount in b :
              print(f'Receipt Amount : {Receipt_Amount}')    
        else:
           print(f"Receipt Amount is visible : {b} which is not within the expected output")      
                    
              
        utilized_value = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().utilized_Amount)
        a = []
        for i in utilized_value:
           v=i.text
           a.append(v)
           b = ' '.join(a)
        #print(a)  
        if utilized_Amount in b :
              print(f'utilized Amount : {utilized_Amount}')   
        else:
           print(f"utilized Amount : {b} which is not within the expected output")  
           
        Transfer_Amount = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Transfer_Amount)
        a = []
        for i in Transfer_Amount:
           v=i.text
           a.append(v)
           b = ' '.join(a)
        #print(a)  
        if Transfer in b :
              print(f'Transfer Amount : {Transfer}')   
        else:
           print(f"Transfer Amount : {b} which is not within the expected output")     
               
           
        balance_value = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Balance_Amount)
        a=[]
        for i in balance_value:
           v=i.text
           a.append(v)  
           b = ' '.join(a)
        if balance_Amount in b :
              print(f'balance Amount : {balance_Amount}')   
        else:
           print(f"balance Amount is visible : {b} which is not within the expected output")   
           
        bill_no = 'HO23-00650'
        bill_date = '22-09-2023'
        Amount = '35891.00'
        type ='Utilized'
        sleep(5)  
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().details).click()
        sleep(5)
        Table = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Row2)
       
        for i in Table:
            v=i.text
             
        split_str = v.split()
        

        output_str = f"{split_str[0]}, {split_str[1]}, {split_str[2]}, {split_str[3].replace(',', '')}, {split_str[4]}, {split_str[5]}"    
        print(f"-------Row No : 1   {output_str}--------")    
        
        if output_str.__contains__(bill_no):
           print(f"Bill No : {bill_no}")
        else:
           print("Bill No : which is not within the expected output")
        if output_str.__contains__(bill_date):
           print(f"Bill date : {bill_date}")
        else:
           print("Bill date : which is not within the expected output") 
        if output_str.__contains__(Amount):
           print(f"Amount : {Amount}")   
        else:
           print("Amount  : which is not within the expected output")
        if output_str.__contains__(type):
           print(f"Type : {type}")   
        else:
           print("Type  :  which is not within the expected output")   
        sleep(5)
       
       
        bill_no_2 = '00261'
        bill_date_2 = '22-09-2023'
        Amount_2 = '250000.00'
        type_2 = "Advance"
        Table = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Row3)
        for i in Table:
            v=i.text   
        split_str = v.split()
      
        output_str = f"{split_str[0]}, {split_str[1]}, {split_str[2]}, {split_str[3].replace(',', '')}, {split_str[4]}, {split_str[5]}"    
        print(f"-------Row No : 2   {output_str}--------")    
        
        if output_str.__contains__(bill_no_2):
           print(f"Bill No : {bill_no_2}")
        else:
           print("Bill No : which is not within the expected output")
        if output_str.__contains__(bill_date_2):
           print(f"Bill date : {bill_date_2}")
        else:
           print("Bill date : which is not within the expected output") 
        if output_str.__contains__(Amount_2):
           print(f"Amount : {Amount_2}")   
        else:
           print("Amount : which is not within the expected output")
        if output_str.__contains__(type_2):
           print(f"Type : {type_2}")   
        else:
           print("Type : which is not within the expected output")   
           
        bill_no_3 = '00262'
        bill_date_3 = '22-09-2023'
        Amount_3 = '10000.00'
        type_3 = "Advance"
        Table = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Row4)
        for i in Table:
            v=i.text   
        split_str = v.split()
        
      
        output_str = f"{split_str[0]}, {split_str[1]}, {split_str[2]}, {split_str[3].replace(',', '')}, {split_str[4]}, {split_str[5]}"    
        print(f"-------Row No : 3   {output_str}--------")   
        
        if output_str.__contains__(bill_no_3):
           print(f"Bill No : {bill_no_3}")
        else:
           print("Bill No : which is not within the expected output")
        if output_str.__contains__(bill_date_3):
           print(f"Bill date : {bill_date_3}")
        else:
           print("Bill date : which is not within the expected output") 
        if output_str.__contains__(Amount_3):
           print(f"Amount : {Amount_3}")   
        else:
           print("Amount : which is not within the expected output")
        if output_str.__contains__(type_3):
           print(f"Type : {type_3}")   
        else:
           print("Type : which is not within the expected output")         
           
        bill_no_4 = '00266'
        bill_date_4 = '27-09-2023'
        Amount_4 = '5000'
        type_4 = "Transfer"   
           
        Table = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Row5)
        for i in Table:
            v=i.text   
        split_str = v.split() 
      
        output_str = f"{split_str[0]}, {split_str[1]}, {split_str[2]}, {split_str[3].replace(',', '')}, {split_str[4]}, {split_str[5]}"    
        print(f"-------Row No : 4   {output_str}--------")   
        
        if output_str.__contains__(bill_no_4):
           print(f"Bill No : {bill_no_4}")
        else:
           print("Bill No : which is not within the expected output")
        if output_str.__contains__(bill_date_4):
           print(f"Bill date : {bill_date_4}")
        else:
           print("Bill date : which is not within the expected output") 
        if output_str.__contains__(Amount_4):
           print(f"Amount : {Amount_4}")   
        else:
           print("Amount : which is not within the expected output")
        if output_str.__contains__(type_4):
           print(f"Type : {type_4}")   
        else:
           print("Type : which is not within the expected output")   
           
        self.driver.refresh()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        branch.send_keys(data.Logi_Data().branch_name)
        branch.send_keys(Keys.RETURN)
        assert self.driver.title == "Logimax Technology | Admin"
        print(f"Selected Branch : {data.Logi_Data().branch_name}")
      
        sleep(5)
        
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Date_range).click()
      
        sleep(5)
        date_input = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Start_date)
        date_input.clear() 
        date_input.send_keys(data.Logi_Data().first_date)
        assert self.driver.title == "Logimax Technology | Admin"
        print(f"From date : {data.Logi_Data().first_date}")
      
        sleep(5)
        
        End_date_input = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().end_date)
        End_date_input.clear() 
        End_date_input.send_keys(data.Logi_Data().last_date)
        assert self.driver.title == "Logimax Technology | Admin"
        print(f"To date : {data.Logi_Data().last_date}")
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().apply).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().search).click()
        sleep(5)
        Receipt_calculation = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Total_Receipt_amount)
        #print(Receipt_calculation)
        Total_receipt = []
        Total_receipt_Amount=0
        
        for value in  Receipt_calculation:
           Total = value.text
           int_value = int(Total.replace(',', '').replace('.00', ''))
           Total_receipt.append(int_value)
           Total_receipt_Amount += int_value  # Add each value to the total
           
            
        print(f"Total Receipt : {Total_receipt}")
        print("Total_Receipt_Amount : ", Total_receipt_Amount)
        sleep(5)
        Receipt = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Total_Receipt).text
        Receipt_value = int(Receipt.replace(',','').replace('.00', ''))
       # print(Receipt_value)
        if Receipt_value ==Total_receipt_Amount:
           print('Total Receipt Amount Calculation verify successfully')
        else:
           print(f"Receipt Amount : {Receipt_value} which is not within the expected output")  
           
        sleep(5)
        utilized_calculation = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Total_utilized_amount)
        #print(Receipt_calculation)
        Total_utilized = []
        Total_utilized_Amount=0
        
        for value in  utilized_calculation:
           Total = value.text
           int_value = int(Total.replace(',', '').replace('.00', ''))
           Total_utilized.append(int_value)
           Total_utilized_Amount += int_value  # Add each value to the total
           
            
        print(f"Total utilized : {Total_utilized}")
        print("Total_utilized_Amount : ", Total_utilized_Amount)
        sleep(5)
        utilized = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Total_utilized).text
        utilized_value = int(utilized.replace(',','').replace('.00', ''))
       # print(utilized_value)
        if utilized_value  == Total_utilized_Amount:
           print('Total utilized Amount Calculation verify successfully')
        else:
           print(f"utilized Amount : {utilized_value} which is not within the expected output")  
           
           
        sleep(5)
        Transfer_calculation = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Total_transfer_amount)
        #print(Receipt_calculation)
        Total_Transfer = []
        Total_transfer_Amount = 0
        
        for value in  Transfer_calculation:
            Total = value.text
            int_value = int(Total.replace(',', '').replace('.00', ''))
            Total_Transfer.append(int_value)
            Total_transfer_Amount += int_value  # Add each value to the total
            
            
        print(f"Total Receipt : {Total_Transfer}")
        print("Total_Transfer_Amount : ", Total_transfer_Amount)
        sleep(5)
        Transfer = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Total_transfer).text
        Transfer_value = int(Transfer.replace(',','').replace('.00', ''))
       # print(Transfer_value)
        if Total_transfer_Amount == Transfer_value:
           print('Total Transfer Amount Calculation verify successfully')
        else:
           print(f"Transfer Amount : {Transfer_value} which is not within the expected output")              
        
        
        sleep(5)
        Balance_calculation = self.driver.find_elements(by=By.XPATH,value=locators.Logi_Locators().Total_balance_amount)
        #print(Receipt_calculation)
        Total_Balance = []
        Total_Balance_Amount =0
        
        for value in  Balance_calculation:
            Total = value.text
            int_value = int(Total.replace(',', '').replace('.00', ''))
            Total_Balance.append(int_value)     
            Total_Balance_Amount += int_value  # Add each value to the total
           
            
        print(f"Total  Balance : {Total_Balance}")
        print("Total_Balance_Amount : ", Total_Balance_Amount)
        sleep(5)
        Balance = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Total_balance).text
        Balance_value = int(Balance.replace(',','').replace('.00', ''))
        #print(Balance_value)
        if Balance_value == Total_Balance_Amount:
           print('Total Balance Amount Calculation verify successfully')
        else:
           print(f"Balance Amount : {Balance_value} which is not within the expected output")              
        
        
        
        
        