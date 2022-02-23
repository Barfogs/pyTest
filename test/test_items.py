from selenium.webdriver.common.by import By
import time
def test_button(browser):
    browser.implicitly_wait(5)
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket"), "Кнопка корзины отсутствует"
