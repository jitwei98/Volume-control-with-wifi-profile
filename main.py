from ver1 import SSID
import os

os.system("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}'>ssid.txt")

print("Hi! Welcome to the freaking awesome program!")
print("This app will automatically adjust the volume for you when you connected to the wifi you have registered.")
print("1. Add Wifi Profile")
print("2. Waiting for response...")
print("3. Current wifi profile")
print("4. Quit")

userInput = input("Choice: ")

if userInput == 1:
    SSID().add_entry(SSID().get_SSID(),SSID().promptVol(SSID().get_SSID()))
    SSID().adjustVolume(SSID().get_SSID())
elif userInput == 4:
    exit()
elif userInput == 2:
    while True:
        SSID().adjustVolume(SSID().get_SSID())
else:
    SSID().list_SSID()
