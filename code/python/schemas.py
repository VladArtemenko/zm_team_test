from dataclasses import dataclass


@dataclass(frozen=True)
class DataBaseConnection:
    host: str = 'postgresql'
    user: str = 'admin'
    password: str = '12345'
    database: str = 'profile'
