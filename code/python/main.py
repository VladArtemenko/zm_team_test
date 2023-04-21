import time
import psycopg2

time.sleep(10)

connection = psycopg2.connect(
    host='postgresql',
    user='admin',
    password='12345',
    database='profile',
    port='5432'
)

req = "SELECT * FROM public.cookie"
# req = 'SELECT * FROM pg_catalog.pg_tables;'

with connection.cursor() as cursor:
    cursor.execute(req)
    res = cursor.fetchmany(50)
    print(res)