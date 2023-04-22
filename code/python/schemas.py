import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class DataBaseConnection:
    host: str = 'postgresql'
    user: str = 'admin'
    password: str = '12345'
    database: str = 'profile'


@dataclass(frozen=False)
class Profile:
    id: int
    created_at_dttm: datetime.datetime
    cookie_value: list
    last_start_at_dttm: datetime.datetime
    number_of_launch: int


@dataclass(frozen=False)
class Context:
    profile: Profile
    link: str
