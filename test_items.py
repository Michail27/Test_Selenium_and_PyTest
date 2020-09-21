import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest(browser):
    browser.get(link)
    time.sleep(10)
    bu = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert bu != "NoSuchElementException", '!!!НЕ НАШЕЛ!!!'