import datetime
import psycopg2

from config import DB_CONFIG


def deliver_contents():
    """
    Reads sessionData.txt, which contains raw data, from /var/log/auth.log and outputs a
    list of PSQL-ready objects.

    :return: A list[data[]] where each object in the list is formatted as [timestamp, user, ip, status] all strings.
    The status is a binary string indicating 'success' or 'fail'.
    """
    file_rows_as_list_objects = read_file_contents()
    final_rows_as_list_objects = []
    for row in file_rows_as_list_objects:
        try:
            separated_contents = row.split(' ')
            month = separated_contents[0]
            day = separated_contents[1]
            full_time_list = separated_contents[2].split(':')

            user = separated_contents[3]
            ip_address = separated_contents[4]
            status = separated_contents[5]

            hour = full_time_list[0]
            minute = full_time_list[1]
            seconds = full_time_list[2]

            psql_ready_timestamp = convert_time_format(month=month, day=day, hour=hour, minute=minute, second=seconds)

            final_rows_as_list_objects.append([psql_ready_timestamp, user, ip_address, status])
        except IndexError as e:
            print('Index error encountered when processing this list: ' + str([row]))
            print(e)
        except Exception as e:
            print('Encountered an unknown error when processing this list: ' + str([row]))
            print(e)

    print(final_rows_as_list_objects)


# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
def convert_string_month_to_int_month(month:str):
    list_of_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    int_month = list_of_months.index(month) + 1
    return int_month


def convert_time_format(month: str=None, day: str=None, hour: str=None, minute: str=None, second: str=None):
    """
    Converts individual time components into a standardized time format.

    :param month: The month as a string.
    :param day: The day as a string.
    :param hour: The hour as a string.
    :param minute: The minute as a string.
    :param second: The second as a string.
    :return: A string representing the formatted time in 'YYYY-MM-DD HH:MM:SS' format.
    """

    # This method is created to convert the current time-format in /var/log/auth.log to
    #  a correct Psql TIMESTAMP format.
    if False in (month, day, hour, minute, second):
        return

    int_month = convert_string_month_to_int_month(month=month)
    year = int(datetime.datetime.now().strftime("%Y"))
    psql_format = datetime.datetime(year=year, month=int_month, day=int(day), hour=int(hour), minute=int(minute), second=int(second)).strftime("%Y-%m-%d %H:%M:%S")
    return psql_format


def read_file_contents():
    with open('sessionData.txt', 'r') as file:
        psql_ready_data_as_rows = file.read()
        psql_ready_data_as_rows = psql_ready_data_as_rows.split(sep='\n')

        return psql_ready_data_as_rows


def dump_all_to_psql():
    conn = psycopg2.connect(
        "dbname=" + DB_CONFIG['db_name'] + " user=" + DB_CONFIG['db_user'] + " host=" + DB_CONFIG['db_host'] + " password=" + DB_CONFIG['db_password'] + " port=" + DB_CONFIG['db_name']
    )
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    cursor.close()
    conn.close()


# Dec 21 10:41:31
# print(convert_time_format(month='Dec', day='21', hour='10', minute='10', second='10'))
deliver_contents()

