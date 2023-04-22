from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import local_logger
import os

logger = local_logger.LocalLogger(os.path.basename(__file__)).writer


class Selenium:
    def __init__(self, cookies):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--ignore-gpu-blacklist')
        options.add_argument('--disable-web-security')

        self._driver = webdriver.Remote(
            'http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options
        )

        self._cookies = cookies

    def __del__(self):
        self._driver.quit()

    def _scroll(self, length: int) -> None:
        self._driver.execute_script(f"window.scrollTo(0, {length})")

    def open_link(self, url):
        self._driver.get(url)

        for cookie in self._cookies:
            self._driver.add_cookie(cookie)

        self._scroll(100)

        return self._driver.get_cookies()
