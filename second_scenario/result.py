import time
from selenium.webdriver.common.by import By


class SbisResultSecondScenarioPage:

    def __init__(self, browser):
        self.browser = browser

    def element_check_text(self, xpath):
        """Возвращает текст элементта"""
        element = self.browser.find_element(By.XPATH, xpath)
        time.sleep(5)
        return element.text

    def regional_partners(self, city):
        """Проверяет что блок с партнерами есть и регион соответствует"""
        element = self.browser.find_element(
            By.XPATH,
            '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]',
        )
        partner = self.browser.find_element(By.XPATH, '//*[@id="city-id-2"]')
        text = partner.text
        if element and city in text:
            return True
        return False

    def click(self, xpath):
        """Клик на элемент"""
        element = self.browser.find_element(By.XPATH, xpath)
        element.click()

    def link_check(self, region):
        """ВПроверяет наличие нужного региона в адресе страницы"""
        link = self.browser.current_url
        if region in link:

            return True
        return False

    def title_check(self, region):
        """Проверка изменения title"""
        title = self.browser.title

        if region in title:
            return True
        return False
