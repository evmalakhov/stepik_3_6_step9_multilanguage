import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 


#link = "http://selenium1py.pythonanywhere.com/"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    
    #browser.find_element_by_css_selector("#add_to_basket_form > button")

    #add_basket_button = WebDriverWait(browser, 30).until(
    #        EC.visibility_of_element_located ((By.CSS_SELECTOR, "#add_to_basket_form__ > button"))
    #    )

    add_basket_buttons = browser.find_elements_by_css_selector("#add_to_basket_form > button")

    #if (not add_basket_buttons or len(add_basket_buttons) < 1):
    if (not add_basket_buttons):
        print("\n Button is found !!! ",  add_basket_buttons )
    else:
        print("\n Button is found : ", len(add_basket_buttons) )

    assert add_basket_buttons, "no ADD BACKET button"


    time.sleep(10)



# <button type="submit" class="btn btn-lg btn-primary btn-add-to-basket" value="Добавить в корзину" data-loading-text="Добавление...">Добавить в корзину</button>
#add_to_basket_form > button
# //*[@id="add_to_basket_form"]/button
