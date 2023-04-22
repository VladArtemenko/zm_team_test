import time
import local_logger
import database_interface
import os
from links_getter import LinksGetter

# Ждем когда поднимется Селениум и ПостгреСКЛ
time.sleep(20)

logger = local_logger.LocalLogger(os.path.basename(__file__)).writer

links = LinksGetter().get_random_links_from_google_news

import local_selenium
