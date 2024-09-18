import pytest

from first_scenario.result import SbisResultFirstScenarioPage
from search import SbisGoSearchPage
from selenium.webdriver import Chrome

from second_scenario.result import SbisResultSecondScenarioPage
from three_scenario.result import SbisResultThreeScenarioPage


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
    search_page_one = SbisGoSearchPage(browser)
    search_page_one.load()
    # Переход по ссылке Контакты
    search_page_one.search(
        "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/a"
    )
    # Переход по ссылке Тензор
    search_page_one.search(
        '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a/img'
    )
    result_page_one = SbisResultFirstScenarioPage(browser)
    browser.switch_to.window(browser.window_handles[1])
    # Проверка, что есть блок "Сила в людях"
    assert (
            result_page_one.element_check(
                '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]'
            )
    )
    # Переход по ссылке Подробнее
    result_page_one.click(
        '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'
    )
    # Проверка, что открывается нужный адрес
    assert result_page_one.link_check() == "https://tensor.ru/about"
    # Проверка, что все фото в разделе одинакового размера
    assert result_page_one.checking_parameters("270", "192")


def test_second_scenario(browser):
    search_page_two = SbisGoSearchPage(browser)
    search_page_two.load()
    # Переход на страницу Контакты
    search_page_two.search(
        "/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[3]/a"
    )
    result_page_two = SbisResultSecondScenarioPage(browser)
    # Проверка, что подтянулся нужный регион
    assert (
            result_page_two.element_check_text(
                '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'
            )
            == "Ярославская обл."
    )
    # Проверка, что есть блок с партнерами и регион соответствует
    assert result_page_two.regional_partners("Ярославль")
    # Переход на форму с выбором региона
    result_page_two.click(
        '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'
    )
    # Выбор другого региона
    result_page_two.click(
        '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span'
    )
    # Проверка, что подтянулся нужный регион
    assert (
            result_page_two.element_check_text(
                '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span'
            )
            == "Камчатский край"
    )
    # Проверка, что есть блок с партнерами и регион соответствует
    assert result_page_two.regional_partners("Камчатский")
    # Проверка, что URL изменился
    assert result_page_two.link_check("kamchatskij-kraj")
    # Проверка title
    assert result_page_two.title_check("Камчатский край")


def test_thee_scenario(browser):
    search_page_three = SbisGoSearchPage(browser)
    search_page_three.load()
    result_page_three = SbisResultThreeScenarioPage(browser)
    # Находим и переходим на ссылку "Скачать локальные версии"
    result_page_three.click("//*[.='Скачать локальные версии']/../a")
    # Скачиваем файл
    result_page_three.meaning_href()
    # Проверяем, что файл загрузился
    assert result_page_three.checking_for_file_availability()
    # Проверяем, что размер файла равен заявленному
    # assert result_page_three.file_size() == '11.451'
