from __future__ import division

import xml.etree.cElementTree as ET
import urllib2
import json
import random
import time
import math
import os

from geopy.geocoders import Nominatim
from geopy.distance import vincenty




lastLat = "0"
lastLng = "0"
destination = 0
init = 0
frame = []
playerLocation = ()
frequency = 0.5
lastLocation = ()



homeLocation = {'lat':'43.01672019999999', 'lng': '-81.28793140000001'}

def changeDestination():
	global destination
	destination = destination + 1
	if destination > 3:
		destination = 0
	print ('==================== Changing Destination ====================')

def calculateFrame(currentLocation):
	r = 0.0017
	topRight = (currentLocation[0]+r,currentLocation[1]+r)   #radius of 250m
	bottomRight = (currentLocation[0]+r,currentLocation[1]-r)
	bottomLeft = (currentLocation[0]-r,currentLocation[1]-r)
	topLeft = (currentLocation[0]-r,currentLocation[1]+r)
	return [topRight,bottomRight,bottomLeft,topLeft]


def calculateNextLocation(currentLocation, targetLocation):
	#print('calculating next location:', currentLocation, targetLocation)
	global frequency
	kmH = 12
	speed = kmH/3.6      #m/s 	 #9km/h
	delta = 0.0020/250*speed		#0.0020/250*2.5
	delta = delta / frequency
	nextLocation = currentLocation
	x = targetLocation[0] - currentLocation[0]
	y = targetLocation[1] - currentLocation[1]
	#print (x,y)
	if(abs(x)<delta and abs(y)<delta):
		changeDestination()
	if abs(x)-abs(y) > 0: 	#horizontal
		if x > 0:			#walk right
			nextLocation = (nextLocation[0] + min(abs(targetLocation[0] - currentLocation[0]), delta), nextLocation[1])
		else:
			nextLocation = (nextLocation[0] - min(abs(targetLocation[0] - currentLocation[0]), delta), nextLocation[1])
	else:					#vertical
		if y > 0:			#walk up
			nextLocation = (nextLocation[0], nextLocation[1] + min(abs(targetLocation[1] - currentLocation[1]), delta))
		else:
			nextLocation = (nextLocation[0], nextLocation[1] - min(abs(targetLocation[1] - currentLocation[1]), delta))
	return nextLocation

def getPokemonLocation(currentLocation):
	global destination, init, frame, playerLocation,lastLocation,frequency

	if not init:
		print('initializing:')
		geolocator = Nominatim()
		location = geolocator.geocode("26 Thirlmere Rd London On")
		print('Current address: ',location.address)
		playerLocation = (location.longitude, location.latitude)
		print ('playerLocation: ', playerLocation)
		frame = calculateFrame(playerLocation)  #path we are walking - a square
		currentLocation = frame[0]
		destination = 1
		init = 1

	r = 250 		# how far it goes from you, in meters

	nextLocation = calculateNextLocation(currentLocation,frame[destination])
	

	distanceFromPlayer = vincenty(playerLocation, nextLocation).meters
	print('destination',destination,'distance from you:', distanceFromPlayer)

	if lastLocation:
		print('Your current speed: ', math.sqrt((nextLocation[0] - lastLocation[0])**2 + (nextLocation[1] - lastLocation[1])**2)*(250/0.0020)/(1/frequency)*3.6,' km/h')
	
	
	lastLocation = nextLocation
	return (str(nextLocation[0]),str(nextLocation[1]))



def generateXML():
	global lastLat, lastLng
	geo = getPokemonLocation((float(lastLng),float(lastLat)))
	print('geo:', geo)
	if geo != None:
		if geo[1] != lastLat or geo[0] != lastLng:
			lastLat = geo[1]
			lastLng = geo[0]
			gpx = ET.Element("gpx", version="1.1", creator="Xcode")
			wpt = ET.SubElement(gpx, "wpt", lat=geo[1], lon=geo[0])
			ET.SubElement(wpt, "name").text = "PokemonLocation"
			ET.ElementTree(gpx).write("pokemonLocation.gpx")
			#print "Location Updated!", "latitude:", geo[1], "longitude:" ,geo[0]


def clickAction():
	os.system("./autoClicker -x 976 -y 880")
	time.sleep(1)
	os.system("./autoClicker -x 999 -y 600")
	time.sleep(1)
	print "clicking!!"


def main():

	while True:
		clickAction()
		generateXML()
		#time.sleep(1/frequency)

if __name__ == "__main__":
    # execute only if run as a script
    main()