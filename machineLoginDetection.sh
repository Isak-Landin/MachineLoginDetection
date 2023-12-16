#!/bin/bash

result_from_failed="$(./_machineGrepLogFailed.sh)"
result_from_successful="$(./_machineGrepLogSuccess.sh)"

echo "$result_from_successful"
