import requests
import json
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




#TODO
# OPTIMIZE CHECKOUT FOR TIME
# FIGURE OUT URL RETRIEVER FOR JJJJOUND NB'S 




#CHANGE VARIABLES WHEN NEEDED
producturl = 'https://shop.havenshop.com/collections/footwear/products/nike-killshot-og-sp-sail-gym-red'
chromeDriverPath = r'C:\Users\Peter\Desktop\chromedriver.exe'
size = '10.5US'
email_input = 'petersherman@google.com'
first_name_input = 'P'
last_name_input = 'Sherman'
address_input = '42 Wallaby Way'
city_input = 'Sydney'
zip_input = 'NSW2 774'
phone_input = '123456789'
card_input_1 = '3400'
card_input_2 = '000000'
card_input_3 = '00009'
product_url = ''
product_filter = 'nike'

def fetchURL(driver):
    driver.get('https://shop.havenshop.com/collections/new-arrivals')
    file1 = open("MyFile.txt","w") 
    elems =  driver.find_elements_by_xpath('//section[@id="shop-products"]/a[@href]')
    count = 0
    for elem in elems:
        href = elem.get_attribute('href')
        
        if href is not None and product_filter in href:
            file1.write(href + '\n')
            i = '[' + str(count) + '] '
            print(i + href) 
        count += 1
            

    while True:
        try:
            index_of_product = int(input("Enter Index of desired Product: \n"))
        except ValueError:
            print("Please enter a proper integer")
            continue
        else:
            break
    
    new_product_url = elems[index_of_product].get_attribute('href')
    file1.close() 
    return (new_product_url)


def buyProduct(driver,product_url):
    
    #navigates to product URL
    driver.get(product_url)
    
    #time.sleep(2)

    #gets rid of popup
    #driver.find_element_by_xpath('//div[@id="ltkpopup-close-button"]').click()
    #time.sleep(.5)
    #time.sleep(.1)
    #clicks a size
    driver.find_element_by_xpath(f'//label[@data-value="{size}"]').click()
    #time.sleep(.2)

    #clicks add to cart
    driver.find_element_by_xpath('//button[@id="AddToCart"]').click()
    time.sleep(.3)

    #navigates to check out
    driver.get('https://shop.havenshop.com/cart')
    
    #clicks check out button
    checkout = driver.find_element_by_xpath('//input[@name="checkout"]')
    driver.execute_script("arguments[0].click();", checkout)
    
    
    #wait for page to load (should be optimized)
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Email"]')))

    #enter email
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(email_input)

    #enter First Name
    driver.find_element_by_xpath('//input[@data-autocomplete-field="first_name"]').send_keys(first_name_input)

    #enter Last Name
    driver.find_element_by_xpath('//input[@data-autocomplete-field="last_name"]').send_keys(last_name_input)

    time.sleep(.1)
    #enter Address
    driver.find_element_by_xpath('//input[@data-autocomplete-field="address1"]').send_keys(address_input)

    #enter City
    driver.find_element_by_xpath('//input[@data-autocomplete-field="city"]').send_keys(city_input)

    #enter Postal Code
    driver.find_element_by_xpath('//input[@data-autocomplete-field="zip"]').send_keys(zip_input)

    #enter Phone
    driver.find_element_by_xpath('//input[@data-autocomplete-field="phone"]').send_keys(phone_input)

    #click "continue to shipping"
    driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    
    #wait for page to load (should be optimized)
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH,'//input[@aria-label="Canada Post Expedited (2-7 Business Days). $15.00"]')))
    #click "Canada Post Expedited" shipping option
    driver.find_element_by_xpath('//input[@aria-label="Canada Post Expedited (2-7 Business Days). $15.00"]').click()

    #click "Continue to Payment" 
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH,'//button[@id="continue_button"]')))

    driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    
    #wait for page to load (should be optimized now)
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH,'//input[@data-trekkie-id="same_billing_address_field"]')))


    #switch to iframe for Payment info
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
    #enter card Number (CHANGE VALUES BEFORE LIVE)
    payment = driver.find_element_by_xpath('//input[@id="number"]')
    payment.send_keys(card_input_1)
    payment.send_keys(card_input_2)
    payment.send_keys(card_input_3)

    #CHANGE VALUES BEFORE LIVE
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)  
    actions.pause(.1)
    actions.send_keys('Peter Sherman') 
    actions.send_keys(Keys.TAB)
    actions.pause(.1)

    actions.send_keys(' 1221')
    actions.send_keys(Keys.TAB)
    actions.pause(.2)
   
    actions.send_keys(' 1234')
    
 
    
    
    #actions.send_keys(Keys.ENTER)

    #DO NOT ACTIVATE ABOVE LINE UNTIL YOU REALLY READY
    actions.perform()
    
    
    time.sleep(1000)

def main():
    driver = webdriver.Chrome(executable_path=chromeDriverPath)
    buyProduct(driver,fetchURL(driver))


if __name__ == "__main__":
    main()
