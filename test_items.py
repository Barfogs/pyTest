from selenium.webdriver.common.by import By
def test_find_button(browser):
    browser.implicitly_wait(5)
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket"), "Кнопка корзины отсутствует"
