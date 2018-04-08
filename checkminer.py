import urllib.request
import time
import os

### Config parameters starts here

ipaddress = 'http://localhost:3333/' # ipaddress and port of your miner
minhashrate = 3900 # minimum acceptable hash-rate
checks = 5 # how many cycles to check before assuming the hash rate is really too low
delay = 10 # delay in seconds between each check
executefile = 'C:/reboot.bat' # full path to the file to execute if the hash rate is too low

### Do not edit anything after this line

subhash = 1;

while True:
	try:
		page = urllib.request.urlopen(ipaddress)
		data = page.read().decode(page.headers.get_content_charset())
		startpos = data.rfind("Total Speed: ")
		endpos =  data.find(" H/s", startpos)
		hashrate = int(data[ startpos + 13: endpos])
		print("Current Hashrate: " + str(hashrate))
		if hashrate < minhashrate:
			print("Hash rate LOW: " + str(subhash) + "/" + str(checks))
			subhash = subhash + 1
		else:
			subhash = 1
		if subhash > checks:
			print("Hashrate too low... executing: " + executefile)
			os.system(executefile)
			subhash = 1
	except:
		print("Waiting for the miner...")
	time.sleep(delay)
