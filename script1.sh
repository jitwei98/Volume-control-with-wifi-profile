#!/bin/sh


#output the current network settings to network.out
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}' > network.out

#more ./network.out

if SSID = "NUS_STU"; then
    echo "equal"
else
    echo "not equal"

#FIRST_ARGUMENT="$1"

#sudo osascript -e "set Volume $FIRST_ARGUMENT"
