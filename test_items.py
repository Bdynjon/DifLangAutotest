from selenium.webdriver.common.by import By


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(url)
    # получаем список элементов соответствующих селектору
    list_of_shit = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    # если список пуст (что равносильно false), выдаст исключение
    assert list_of_shit, "'Add to basket' button not found"
