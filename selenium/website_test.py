# #!/usr/bin/env python
import sys
import os
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s - %(message)s')

def log(message):
    logging.info(message)

def setup(headlessmode):
    if headlessmode == 'True' :
       options = ChromeOptions()
       options.add_argument("--headless") 
       driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome()
    
    return driver


# Start the browser and login with standard_user
def login (user, password,driver):
    log("Navigating to the demo page to login.")
    log("Logging in as standard user")
    driver.find_element_by_css_selector("div[id=login_button_container] > div > form > #user-name").send_keys(user);
    driver.find_element_by_css_selector("div[id=login_button_container] > div > form > #password").send_keys(password);
    driver.find_element_by_css_selector("div[id=login_button_container] > div > form > #login-button").click();
    
    
    product_label_text = driver.find_element_by_css_selector(".product_label").text
    log('After Login in Product page, Found Product Label Text {}'.format(product_label_text))
    if not product_label_text:
       log("Error Login not successful")
       raise ValueError('Unsuccessful Login')
    else:
        log("Logging successful for standard user")

def get_total_cart_items_count(driver):
    # Check if the total cart count element exists and return the count
    count = 0
    try: 
       count = driver.find_element_by_css_selector(".fa-layers-counter").text;
       return count
    except NoSuchElementException:
       return -1

def additem_to_cart(driver):
    log("Adding One Item to Cart")
    driver.find_element_by_css_selector("div[class=inventory_list] > div[class=inventory_item]:nth-child(1) .btn_primary").click();
    log("Successfully added first item to Cart")

    log("Adding Second Item to Cart")
    driver.find_element_by_css_selector("div[class=inventory_list] > div[class=inventory_item]:nth-child(2) .btn_primary").click();
    log("Successfully added Second item to Cart")

    driver.find_element_by_css_selector("div[class=shopping_cart_container] > .shopping_cart_link").click();
    cart_quantity = get_total_cart_items_count(driver);
    if not cart_quantity or int(cart_quantity) != 2:
       log("Error Items not added to Cart successfully")
       raise ValueError('Items not added to Cart')
    else:
       log('Successfully added items to Cart, Total Cart Items {}'.format(cart_quantity))

def removeitem_from_cart(driver):
    log("Removing Items from Cart")
    button1 = driver.find_element_by_css_selector("div[class=cart_list] > div[class=cart_item]:nth-child(3) .btn_secondary.cart_button");
    button1.click();
    cart_quantity_after_one_item_removed = get_total_cart_items_count(driver);
    log("Cart Quantity after removing one item {}".format(cart_quantity_after_one_item_removed))
    if int(cart_quantity_after_one_item_removed) == 2:
       log('Unable to remove first item')
       raise ValueError('Unable to remove item')

    button2 = driver.find_element_by_css_selector("div[class=cart_list] > div[class=cart_item]:nth-child(4) .btn_secondary.cart_button");
    button2.click();
    cart_quantity_after_second_item_removed = get_total_cart_items_count(driver);

    if int(cart_quantity_after_second_item_removed) != -1:
      log('Unable to remove Second item')
      raise ValueError('Unable to remove item')  
    log("Successfully removed second item from Cart")

def main():
    log ('Starting the browser...')
    if len(sys.argv[1]) > 1:
        headlessmode = sys.argv[1]
    else:
        headlessmode = False;

    driver = setup(headlessmode)
    driver.get('https://www.saucedemo.com/')
    log('Browser started successfully Headless mode set as {}'.format(headlessmode))

    try:
        login("standard_user","secret_sauce",driver)
        additem_to_cart(driver)
        removeitem_from_cart(driver)
    except Exception:
        driver.quit()
        log("Selenium Test failed")


if __name__ == "__main__":
    main();