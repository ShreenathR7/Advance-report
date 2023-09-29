# locators.py - File where all The HTML Locators are Kept
class Logi_Locators:
    username_inputBox = 'username'

    password_inputBox = 'password'
     
    signButton ='(//*[@id="submit_login"])'
    
    side_bar = '//a[@class="sidebar-toggle"]'
  
    #Sales_Report = "//span[text()='Sales Report']/preceding-sibling::i[@class='fa fa-area-chart text-orange']"
    
    Sales_Report = "//span[text()='Sales Report']"
    
    Advance_Detailed_Report  = "//span[text()='Advance Detailed Report']/preceding-sibling::i[@class='fa fa-circle-o']"
    
    text_box = '(//*[@role="textbox"])'
    
    branch = '//li[@class="select2-selection__choice"]'
    
    Date_range = "rpt_date_picker"
    
    Start_date = "daterangepicker_start"
    
    end_date = 'daterangepicker_end'
    
    apply = '//button[@class="applyBtn btn btn-small btn-sm btn-success"]'
    
    search = "advance_total_search"
    
    Mobile_No = "Mob_search"
    
    Name = '//table[@id="advance_total_list"]/tbody/tr/td[1]'
    
    mobile = '//table[@id="advance_total_list"]/tbody/tr/td[2]'
    
    Receipt_Amount = '//table[@id="advance_total_list"]/tbody/tr/td[3]'
    
    utilized_Amount = '//table[@id="advance_total_list"]/tbody/tr/td[4]'
    
    Transfer_Amount = '//table[@id="advance_total_list"]/tbody/tr/td[6]'
    
    Balance_Amount = '//table[@id="advance_total_list"]/tbody/tr/td[7]'    
    
    details = '//i[@class="fa fa-chevron-circle-down text-teal"]'
    
    Row2 = '//table[@class="table table-responsive table-bordered text-center table-sm"]/tbody/tr[2]'
    
    Row3 = '//table[@class="table table-responsive table-bordered text-center table-sm"]/tbody/tr[3]'
     
    Row4 = '//table[@class="table table-responsive table-bordered text-center table-sm"]/tbody/tr[4]'
    
    Row5 = '//table[@class="table table-responsive table-bordered text-center table-sm"]/tbody/tr[5]'
    
    Total_Receipt_amount = '//table[@id="advance_total_list"]/tbody/tr/td[3]'
    
    Total_Receipt = '//tr[@style="font-weight:bold; color: red"]/td[3]'
    
    Total_utilized_amount = '//table[@id="advance_total_list"]/tbody/tr/td[4]'
    
    Total_utilized = '//tr[@style="font-weight:bold; color: red"]/td[4]'
    
    Total_transfer_amount = '//table[@id="advance_total_list"]/tbody/tr/td[6]'
    
    Total_transfer = '//tr[@style="font-weight:bold; color: red"]/td[6]'
    
    Total_balance_amount = '//table[@id="advance_total_list"]/tbody/tr/td[7]'
    
    Total_balance = '//tr[@style="font-weight:bold; color: red"]/td[7]'
    


    billing = "//span[text()='Billing']"
    
    issue = "//span[text()='Issue']/preceding-sibling::i[@class='fa fa-circle-o']"
    
    add_issuse = "add_billing"
    
    Select_branch = '(//*[@role="presentation"])[2]'
    
    Refund = "issue_type3"
    
    name = "name"
    
    Advance_Amount = '//table[@id="refund_list"]/tbody/tr/td[3]'
    