import pytest

from first_scenario.result import SbisResultFirstScenarioPage
from search import SbisGoSearchPage
from selenium.webdriver import Chrome


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
    search_page.search('//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img')
    # Проверка, что объект на странице
    result_page = SbisResultFirstScenarioPage(browser)
    browser.switch_to.window(browser.window_handles[1])
    assert result_page.element_check('//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]') == True

    result_page.click('//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    assert result_page.link_check() == 'https://tensor.ru/about'
    assert result_page.checking_parameters('270', '192') == True

    # assert result_page.current_url == 'https://tensor.ru/about'
