#!/bin/bash
set -m

mongodb_cmd="mongod"
cmd="$mongodb_cmd"

if [ "$AUTH" == "yes" ]; then
    cmd="$cmd --auth --bind_ip 0.0.0.0"
fi

echo $cmd

$cmd &

if [ ! -f /data/db/.mongodb_password_set ]; then
    /set_mongodb_password.sh
fi

fg