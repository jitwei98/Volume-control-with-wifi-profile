from ver1 import SSID
import urllib

try:
    url = "https://www.google.com"
    urllib.urlopen(url)
    status = "Connected"
except:
    status = "Not connected"
print status
if status == "Connected":
	SSID().adjustVolume(SSID().get_SSID())