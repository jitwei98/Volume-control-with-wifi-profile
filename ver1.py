import os, sys
import csv

os.system("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}'>ssid.txt")

class SSID:
	def get_SSID(self): ###for getting ssid from csv automatically
		with open("ssid.txt") as myFile:
			strs = myFile.readline()
			strs = strs.replace("\n","")
			return strs

	def promptVol(self):
		volume = input("Enter Volume: ")
		return volume

	def add_entry(self, SSID, volume):
	# 	SSID = get_SSID()
	# 	volume = promptVol()
		with open('ssid.csv', 'a') as csvfile:
			fieldnames = ['SSID', 'volume']
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

			writer.writeheader()
			writer.writerow({'SSID': SSID, 'volume': volume})


print(SSID().get_SSID())
print(SSID().promptVol())
SSID().add_entry(SSID().get_SSID(), SSID().promptVol())