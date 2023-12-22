from config import DB_CONFIG
import requests
import json
import os
import datetime
import psycopg2

from config import DB_CONFIG


# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
def convert_string_month_to_int_month(month:str):
    list_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    int_month = list_of_months.index(month) + 1
    return int_month


def convert_time_format(month: str=None, day: str=None, hour: str=None, minute: str=None, second: str=None):
    # This method is created to convert the current time-format in /var/log/auth.log to
    #  a correct Psql TIMESTAMP format.
    if False in (month, day, hour, minute, second):
        return

    int_month = convert_string_month_to_int_month(month=month)
    year = int(datetime.datetime.now().strftime("%Y"))
    psql_format = datetime.datetime(year=year, month=int_month, day=int(day), hour=int(hour), minute=int(minute), second=int(second))
    return psql_format


def dump_all_to_psql():
    conn = psycopg2.connect(
        f"dbname={DB_CONFIG['db_name']}"
        f"user={DB_CONFIG['db_user']}"
        f"host={DB_CONFIG['db_host']}"
        f"password={DB_CONFIG['db_password']}"
        f"port={DB_CONFIG['db_name']}"
    )
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    cursor.close()
    conn.close()

# Dec 21 10:41:31
print(convert_time_format(month='Dec', day='21', hour='10', minute='10', second='10'))

