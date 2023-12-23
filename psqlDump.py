import psycopg2
from config import DB_CONFIG
from datetime import datetime


def is_entry_valid(single_entry: list[str]):
    def is_valid_timestamp(time: str):
        try:
            datetime.strptime(time, "%Y-%m-%d %H:%M:%s")
            return True
        except TypeError as time_error:
            print('A time format error was encountered with the following entry: ' + str(single_entry))
            print(time_error)
            return False
        except ValueError as time_error:
            print('A time format error was encountered with the following entry: ' + str(single_entry))
            print(time_error)
        except Exception as time_error:
            print('An unexpected tme format error was encountered with the following entry: ' + str(single_entry))
            print(time_error)
            return False

    # Checks that all the incoming indexes are of the type string.
    if any(not isinstance(value, str) for value in single_entry):
        print("Error: Non-string value found.")
        return False

    # Checks that none of the incoming indexes in the list are empty
    if '' in single_entry:
        print("Error: Empty string found in entry.")
        return False

    # Checks that the last index is either 'success' or 'fail'
    if single_entry[3] not in ('success', 'fail'):
        print("Error: Last entry must be 'success' or 'fail'.")
        return False

    # Checking if all parts of the ip-address are convertible to an int
    try:
        ip_parts = [int(part) for part in
                    single_entry[2].split('.')]  # assuming single_entry[2] is the IP address string
        if len(ip_parts) != 4:
            print("Error: IP address does not have four parts.")
            return False
    except ValueError as e:
        print('Skipping entry due to invalid IP: ' + str(single_entry))
        print(e)
        return False
    except TypeError as e:
        print('Skipping entry due to invalid IP: ' + str(single_entry))
        print(e)
        return False

    if not is_valid_timestamp(single_entry[0]):
        return False

    return True



def dump_all_to_psql(single_entry: list[str]):
    conn = psycopg2.connect(
        f"dbname= {DB_CONFIG['db_name']} user= {DB_CONFIG['db_user']} host= {DB_CONFIG['db_host']} password= {DB_CONFIG['db_password']} port= {DB_CONFIG['db_name']}"
    )
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    cursor.close()
    conn.close()
