#!/bin/bash

script_dir="$( cd "$( dirname "$0" )" && pwd )"

env_file="$script_dir/.secrets.env"
source $env_file

rtl_433="/usr/local/bin/rtl_433"
# If did not install, can run from build dir by uncommenting line below:
# rtl_433="$script_dir/../rtl_433/build/src/rtl_433"

decoders="-R 191"
json=""
# If want to also output json locally (for debug), uncomment below
# json="-F json"
mqtt="-F \"mqtt://localhost:1883,user=$MQTT_USERNAME,pass=$MQTT_PASSWORD,retain=0,events=rtl_433[/model]__[id]\""

eval $rtl_433 $decoders $json $mqtt
