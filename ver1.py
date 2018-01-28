import os, sys
import csv

os.system("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/ SSID/ {print substr($0, index($0, $2))}'>ssid.txt")

class SSID:
	def get_SSID(self): ###for getting ssid from csv automatically
		with open("ssid.txt") as myFile:
			strs = myFile.readline()
			strs = strs.replace("\n","")
			return strs

	def promptVol(self,SSID):
		print("SSID : {}".format(SSID))
		volume = input("Enter Volume: ")
		return volume

	def add_entry(self, SSID, volume):
	# 	SSID = get_SSID()
	# 	volume = promptVol()
		with open('ssid.csv', 'a') as csvfile:
			fieldnames = ['SSID', 'volume']
			writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

			# writer.writeheader()
			writer.writerow({'SSID': SSID, 'volume': volume})


	def list_SSID(self):
		with open('ssid.csv', 'r') as csvfile:
			fieldnames = ['SSID', 'volume']
			reader = csv.DictReader(csvfile, fieldnames = fieldnames)

			for row in reader:
				print(row['SSID'], row['volume']) # TODO: pretty print


	def adjustVolume(self,SSID):
		with open('ssid.csv', 'r') as csvfile:
			rows = csv.reader(csvfile)
			for row in rows:
				if row[0] == SSID:
					volume = row[1]
					os.system("osascript -e 'set volume output volume {}'".format(volume))

	# def pprint(self,col1,col2):
	# 	print("\t{}\t{}\n".format(str(col1)[5:-2],str(col2)[5:-2]))



# print(SSID().get_SSID())
# print(SSID().promptVol())
#SSID().add_entry(SSID().get_SSID(),SSID().promptVol())
# SSID().pprint(row['ssid'],row['volume'])
