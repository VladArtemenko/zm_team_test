"""
Модуль отвечающий за взаимодействие с БД
"""

import schemas
from abc import ABC, abstractmethod
import psycopg2
import local_logger
import os

logger = local_logger.LocalLogger(os.path.basename(__file__)).writer


class SQL(ABC):
    """
    Класс для отправки запросов к БД
    """
    def __init__(self):
        self._connection_settings = schemas.DataBaseConnection()
        self._connection = psycopg2.connect(
            host=self._connection_settings.host,
            user=self._connection_settings.user,
            database=self._connection_settings.database,
            password=self._connection_settings.password
        )
        logger.info('Open DB connection')

    @staticmethod
    def _convert_response(res, columns):
        converted_response = []
        for row in res:
            converted_response.append(
                {
                    columns[x]: row[x] for x in range(len(row))
                }
            )
        return converted_response

    @property
    @abstractmethod
    def _any_return(self) -> bool:
        """Ожидается ли ответ от БД"""

    def _execute_request(self, request: str, limit: int = 100):
        with self._connection.cursor() as cursor:
            cursor.execute(request)
            logger.debug(f'Execute DB request: "{request}"')
            if not self._any_return:
                self._connection.commit()
                result = None
            else:
                res = cursor.fetchmany(limit)
                result = self._convert_response(res, columns=[column.name for column in cursor.description])

        if self._connection:
            self._connection.close()
        logger.info('Close DB connection')

        return result


class QueryInterface(SQL, ABC):
    @abstractmethod
    def _make_request(self, *args, **kwargs):
        """Метод для создания запроса разных типов в БД"""

    def run(self, *args, **kwargs):
        request = self._make_request(*args, **kwargs)
        return self._execute_request(request=request)


class SelectQuery(QueryInterface):
    """
    Класс для выполнения SELECT запросов
    """
    def _make_request(self, conditions='1=1', table='cookie', columns='*'):
        request = "SELECT {columns} FROM {table} WHERE {conditions}"
        return request.format(columns=columns, table=table, conditions=conditions)

    @property
    def _any_return(self) -> bool:
        return True


class UpdateQuery(QueryInterface):
    """
    Класс для выполнения UPDATE запросов
    """
    def _make_request(self, table='cookie', column='cookie', value=None, condition='1=1'):
        request = "UPDATE {table} SET {column} = {value} WHERE {condition}"
        return request.format(table=table, column=column, value=value, condition=condition)

    @property
    def _any_return(self) -> bool:
        return False
