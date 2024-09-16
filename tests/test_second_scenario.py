import pytest
from search import SbisGoSearchPage
from selenium.webdriver import Chrome

from second_scenario.result import SbisResultSecondScenarioPage


@pytest.fixture
def browser():
    # Инициализация ChromeDriver
    driver = Chrome()
    # Неявное ожидание готовности элементов перед попыткой взаимодействия
    driver.implicitly_wait(10)
    # Возвращение объекта драйвера в конце настройки
    yield driver
    # Для очистки покиньте драйвер
    driver.quit()

def test_first_scenario(browser):
    # Преход на еобходимую страницу
    search_page = SbisGoSearchPage(browser)
    search_page.load()
    search_page.search('//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/a')
    result_page = SbisResultSecondScenarioPage(browser)
    result_page.element_check_text('//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span') == 'Ярославская обл.'

#
# result_page = SbisResultSecondScenarioPage(browser)
#     result_page.element_check('//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span') == 'Ярославская обл.'
#     result_page.click('//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')