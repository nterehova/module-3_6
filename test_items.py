import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_exists(browser):
    browser.get(link)
    button_add_to_basket = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")
    #проверяем что найден ровно один элемент добавления в корзину
    assert len(button_add_to_basket) == 1, "Button is not found"
    
