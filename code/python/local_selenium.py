from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import local_logger
import os
import time
import random

logger = local_logger.LocalLogger(os.path.basename(__file__)).writer


class Selenium:
    """
    Класс который подключается к контейнеру с Селениумом
    """
    def __init__(self, cookies):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-gpu-blacklist')
        options.add_argument('--disable-web-security')

        self._driver = webdriver.Remote(
            'http://hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options
        )

        self._cookies = cookies if cookies is not None else [[]]

        logger.info('Created remote selenium webdriver')

    def _scroll(self, length: int) -> None:
        """Метод для скролла вниз с заданной задержкой"""
        time.sleep(length)
        self._driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight)")
        logger.info(f'Make random delay in {length}s')

    def open_link(self, url) -> list:
        """Публичный метод для открытия ссылки, добавлению куки, обновлению странички и скроллу с задержкой"""
        self._driver.get(url)

        for cookie in self._cookies[0]:
            self._driver.add_cookie(cookie)

        self._driver.refresh()
        self._scroll(random.randint(1, 10))
        cookies = self._driver.get_cookies()
        self._driver.quit()

        return cookies
