from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class SbisResultFirstScenarioPage:

    def __init__(self, browser):
        self.browser = browser

    def element_check(self, xpath):
        """Поиск элемента"""
        try:
            self.browser.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    def click(self, xpath):
        """Клик на элемент"""
        element = self.browser.find_element(By.XPATH, xpath)

        actions = ActionChains(self.browser)
        actions.move_to_element(element)
        self.browser.execute_script("arguments[0].click();", element)

    def link_check(self):
        """Возвращает адрес текущей страницы"""

        link = self.browser.current_url
        return link

    def checking_parameters(self, x, y):
        """Проверяет, что параметры 'width' и 'height' одинаковы для всех элементов из списка"""
        elements = self.browser.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image new_lazy loaded')
        for element in elements:
            if element('width') != x and element('height') != y:
                return False
        return True
