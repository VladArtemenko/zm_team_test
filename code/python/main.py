import time
import os
import local_logger
import database_interface
from links_getter import LinksGetter
from local_selenium import Selenium
import multiprocessing
from schemas import *
import random
import json

logger = local_logger.LocalLogger(os.path.basename(__file__)).writer


def update_profile(profile: Profile):
    fields_to_update = {
        'cookie_value': f"array['{json.dumps(profile.cookie_value)}']::json[]",
        'last_start_at_dttm': f"'{str(profile.last_start_at_dttm)}'",
        'number_of_launch': profile.number_of_launch
    }

    for field in fields_to_update:
        database_interface.UpdateQuery().run(
            column=field,
            value=fields_to_update[field],
            condition=f'id = {profile.id}'
        )


def execute(context: Context):
    link = context.link
    profile = context.profile

    # Запускаем Селениум, передаем куки
    selenium = Selenium(profile.cookie_value)

    # Получили новые куки
    new_cookie_value = selenium.open_link(link)

    logger.info('Get new cookies')
    profile.cookie_value = new_cookie_value
    profile.number_of_launch += 1
    profile.last_start_at_dttm = datetime.datetime.now()

    # Обновляем куки в БД
    update_profile(profile)
    logger.info('Update profile')

    logger.info('Task executed')


def main():
    # Скачиваем профили
    profiles = database_interface.SelectQuery().run()
    profiles = [Profile(**x) for x in profiles]

    # Забираем ссылки
    links = LinksGetter().get_random_links_from_google_news
    # Перемешиваем их
    random.shuffle(links)

    # Присваиваем каждому профилю свою ссылку
    count_of_links = len(links)
    contexts = []
    for index in range(len(profiles)):
        contexts.append(
            Context(
                profile=profiles[index],
                link=links[index % count_of_links]
            )
        )

    # Запускаем 5 процессов для обновления куки всех профилей
    with multiprocessing.Pool(5) as p:
        p.map(execute, contexts)
        p.close()
        p.join()


if __name__ == '__main__':
    while True:
        # Обновляем наши профили раз в 60 секунд
        time.sleep(60)
        main()
