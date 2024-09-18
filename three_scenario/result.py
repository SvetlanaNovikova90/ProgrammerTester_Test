import os

import requests
from selenium.webdriver.common.by import By


class SbisResultThreeScenarioPage:

    def __init__(self, browser):
        self.browser = browser

    def click(self, xpath):
        """Клик на элемент"""
        element = self.browser.find_element(By.XPATH, xpath)
        self.browser.execute_script("arguments[0].click();", element)

    def meaning_href(self):
        element = self.browser.find_element(
            By.XPATH,
            "/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/a",
        )
        link = element.get_attribute("href")

        response = requests.get(link)

        response.raise_for_status()

        with open("sbisplugin-setup-web.exe", "wb") as file:
            file.write(response.content)

    def checking_for_file_availability(self):
        f = open("sbisplugin-setup-web.exe")
        if f:
            f.close()
            return True
        return False

    def file_size(self):
        file_size = os.path.getsize("sbisplugin-setup-web.exe")
        return file_size
