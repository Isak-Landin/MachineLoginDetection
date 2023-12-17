#!/bin/bash

logged_attempts="$(./_machineGrepLog.sh)"

psql_ready_data=""

filter_logs_for_data(){
	failed_password=$( echo "$logged_attempts" | grep 'Failed password for invalid user')
	successful_password=$(echo "$logged_attempts" | grep 'Accepted password for')
	successful_pk=$(echo "$logged_attempts" | grep 'Accepted public')

	if [ -n "$failed_password" ]; then
		no_special_logs=$(echo "$failed_password" | grep -v "message repeated")
		special_logs=$(echo "$failed_password" | grep "message repeated")
		if [ -n "$no_special_logs" ]; then
			psql_ready_data+=$(echo "$no_special_logs" | awk '{print $1, $2, $3, $11, $13, "fail"}')
			psql_ready_data+=$'\n'
		fi
		if [ -n "$special_logs" ]; then
			psql_ready_data+=$(echo "$special_logs" | awk '{print $1, $2, $3, $16, $18, "fail"}')
			psql_ready_data+=$'\n'
		fi
	fi

	if [ -n "$successful_password" ]; then
		psql_ready_data+=$(echo "$successful_password" | awk '{print $1, $2, $3, $9, $11, "success"}')
		psql_ready_data+=$'\n'
	fi

	if [ -n "$successful_pk" ]; then
                psql_ready_data+=$(echo "$successful_pk" | awk '{print $1, $2, $3, $9, $11, "success"}')
                psql_ready_data+=$'\n'
        fi
}

filter_logs_for_data
#echo "no special logs"
#echo "$no_special_logs"
#echo "$(./_machinePsqlDump.sh psql_ready_data)"
#echo "$special_logs"
#echo "$failed_password_data"
#echo "$failed_password"

echo "$psql_ready_data"

