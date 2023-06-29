import time
from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_add_to_basket_button(browser):
    browser.get(link)
    # изменить параметр на 30 сек
    time.sleep(7)
    find_button = browser.find_element(By.XPATH, "//form[@id='add_to_basket_form']//button")
    text = find_button.text
    assert len(text) > 0, 'Не найдена кнопка добавления в корзину'





