from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SbisGoSearchPage:
    URL = 'https://sbis.ru/'
    SEARCH_INPUT = (By.XPATH, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, xpath):
        search_input = self.browser.find_element(By.XPATH, xpath)
        self.browser.implicitly_wait(10)
        search_input.click()
