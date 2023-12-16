#!/bin/bash

source ./config.sh

today_authlog_contents="$(sudo grep ^"$today_date" /var/log/auth.log)"

grep_invalid_user_andor_password() {
	failed_login_attempts=$(echo "$today_authlog_contents" | grep "Failed password for")
}

grep_invalid_user_andor_password

echo "$failed_login_attempts"

