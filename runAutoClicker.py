import os
import urllib2
import json
import time

def checkConnected():
	try:
		response = urllib2.urlopen("http://192.168.1.172/", timeout = 1)
		return json.load(response)
	except urllib2.URLError as e:
		print e.reason

def clickAction():
	os.system("./autoClicker -x 976 -y 880")
	time.sleep(0.5)
	os.system("./autoClicker -x 999 -y 600")
	time.sleep(1)
	print "clicking!!"

def start():
	while True:
		clickAction()
		# if checkConnected() != None:
		# 	clickAction()

start()