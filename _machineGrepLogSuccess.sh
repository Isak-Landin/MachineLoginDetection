#!/bin/bash

source ./config.sh

today_authlog_contents="$(sudo grep ^"$today_date" /var/log/auth.log)"

grep_valid_user_andor_password() {
        successful_login_attempts=$(echo "$today_authlog_contents" | grep -E "Accepted password|Accepted publickey for")
}

grep_valid_user_andor_password

echo "$successful_login_attempts"
