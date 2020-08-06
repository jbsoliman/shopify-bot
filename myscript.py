import requests
import json
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


#TODO
# FIGURE OUT HOW TO SEND KEYS IN PAYMENT
# OPTIMIZE CHECKOUT FOR TIME
# FIGURE OUT URL RETRIEVER FOR JJJJOUND NB'S 


producturl = 'https://shop.havenshop.com/collections/footwear/products/nike-killshot-og-sp-sail-gym-red'
def buyProduct():
    driver = webdriver.Chrome(executable_path=r'C:\Users\Jason\Desktop\chromedriver.exe')
    


    #navigates to product URL
    driver.get(producturl)
    
    #time.sleep(2)

    #gets rid of popup
    #driver.find_element_by_xpath('//div[@id="ltkpopup-close-button"]').click()
    #time.sleep(.5)
    #time.sleep(.1)
    #clicks a size
    driver.find_element_by_xpath('//label[@data-value="10.5US"]').click()
    #time.sleep(.1)

    #clicks add to cart
    driver.find_element_by_xpath('//button[@id="AddToCart"]').click()
    time.sleep(.1)

    #navigates to check out
    driver.get('https://shop.havenshop.com/cart')
    
    #clicks check out button
    checkout = driver.find_element_by_xpath('//input[@name="checkout"]')
    driver.execute_script("arguments[0].click();", checkout)
    
    #wait for page to load (LOOK INTO OPTIMIZING THIS)
    time.sleep(3)

    #enter email
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('jsolimaan@gmail.com')

    #enter First Name
    driver.find_element_by_xpath('//input[@data-autocomplete-field="first_name"]').send_keys('Jason')

    #enter Last Name
    driver.find_element_by_xpath('//input[@data-autocomplete-field="last_name"]').send_keys('Soliman')

    time.sleep(.1)
    #enter Address
    driver.find_element_by_xpath('//input[@data-autocomplete-field="address1"]').send_keys('743 Miller Ave')

    #enter City
    driver.find_element_by_xpath('//input[@data-autocomplete-field="city"]').send_keys('Coquitlam')

    #enter Postal Code
    driver.find_element_by_xpath('//input[@data-autocomplete-field="zip"]').send_keys('V3J 4K4')

    #enter Phone
    driver.find_element_by_xpath('//input[@data-autocomplete-field="phone"]').send_keys('6044403329')

    #click "continue to shipping"
    driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    
    #wait for page to load (LOOK INTO OPTIMIZING THIS)
    time.sleep(3)
    #click "Canada Post Expedited" shipping option
    driver.find_element_by_xpath('//input[@aria-label="Canada Post Expedited (2-7 Business Days). $15.00"]').click()

    #click "Continue to Payment" 
    driver.find_element_by_xpath('//button[@id="continue_button"]').click()
    
    #wait for page to load (LOOK INTO OPTIMIZING THIS)
    time.sleep(4)


    #switch to iframe for Payment info
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
    #enter card Number (CHANGE VALUES BEFORE LIVE)
    payment = driver.find_element_by_xpath('//input[@id="number"]')
    payment.send_keys('3400')
    payment.send_keys('000000')
    payment.send_keys('00009')

    #CHANGE VALUES BEFORE LIVE
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB  + 'Jason Soliman' + Keys.TAB + ' 12 21' + Keys.TAB + ' 1234' + Keys.ENTER)
    #DO NOT ACTIVATE BELOW LINE UNTIL YOU REALLY READY
    #actions.perform()
    
    
    #!!!!!!!!!!!!click Pay Now DONT DACTUALLY DO THISSSSSSSS!!!!!!!!!!!!!!!!

    time.sleep(1000)

def main():
    buyProduct()


if __name__ == "__main__":
    main()