
#!/bin/bash
source ./config.sh
echo "$today_date"

today_authlog_contents="$(sudo grep ^"$today_date" /var/log/auth.log)"

grep_invalid_user_andor_password() {
	failed_login_attempts=$(echo "$today_authlog_contents" | grep "Failed password for")
	echo "$failed_login_attempts"
}

grep_invalid_user_andor_password "$today_date"
