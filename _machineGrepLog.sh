#!/bin/bash

source ./config.sh

today_authlog_contents="$(sudo grep ^"$today_date" /var/log/auth.log)"

grep_filter_attempts() {
	login_attempts=$(echo "$today_authlog_contents" | grep -E "Failed password for|Accepted password|Accepted public")
}

grep_filter_attempts

echo "$login_attempts"


