import requests
from bs4 import BeautifulSoup
import local_logger
import os

logger = local_logger.LocalLogger(os.path.basename(__file__)).writer


class LinksGetter:
    """
    Класс для получения ссылок из сервиса новостей google
    """
    def __init__(self, url='https://news.google.com/home'):
        self._url = url

    @property
    def get_random_links_from_google_news(self):
        google_response = requests.get(url=self._url)
        logger.info('Get HTML code from google news')
        soup = BeautifulSoup(google_response.text, 'html.parser')

        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href is None:
                continue
            if 'articles' in href:
                href = 'https://news.google.com' + href[1:]
                links.append(href)

        logger.info(f'Get {len(links)} links from google news')
        return links