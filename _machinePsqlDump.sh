#!/bin/bash

# Function to convert log date to PostgreSQL timestamp format
convert_to_psql_timestamp() {
    local month=$1
    local day=$2
    local time=$3
    local current_year=$(date +"%Y")  # Get the current year

    # Convert to PostgreSQL timestamp format
    echo $(date -d "$month $day $current_year $time" +"%Y-%m-%d %H:%M:%S")
}

# Initialize variable to store formatted data
psql_ready_data=""

while IFS= read -r line; do
    # Extract the necessary fields using awk or cut
    read month day time user ip status <<< $(echo "$line" | awk '{print $1, $2, $3, $4, $5, $6, $7}')

    # Convert the date and construct the final line
    converted_date=$(convert_to_psql_timestamp "$month" "$day" "$time")
    final_line="$converted_date $user $ip $status"

    # Append to psql_ready_data
    echo "$final_line"
done
