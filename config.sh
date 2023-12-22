#!/bin/bash

today_date="$(date +'%b %d')"

# Currently the only accepted unit of time is h
timespan="24h"

database_name="loginattemptsdb"

table_login_attempts="login_attempts"
table_dropped_users="dropped_users"
table_good_users="good_users"
