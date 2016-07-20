# Overall flow
1. you provide your current location to the app, which then calculate a path around you
2. Based on the path it then generates gpx file constantly
3. Create a blank project referencing the gpx and simulate on your playing device
4. auto click the xcode buttons to constantly uploading the location

## Will I be banned?
There are softbans(a few hours) for players that spoof locations. The system does this by calculating the speed you move. Say you spoofed your location to NYC, then you disconnected and you will be back at your current loaction, then you will be moving too fast and you will be banned.

Using this app you will be just "runing" around your house, so the system will not detect that you are location spoofing.

##Disclaimer
Use at your own risk.

#Instruction
First of all you need XCODE for this to work, you can explore other options for androids and use the same logic under "eggrun.py"

This is a fork from https://github.com/kahopoon/Pokemon-Go-Controller , see the original project for more instructions.

Clone/download this project. Change the location into your current address: 

```
location = geolocator.geocode("ENTER YOUR ADDRESS HERE! be specific")
```

Open xcode and start a blank project. Include the 'pokemonLocation.gpx' file (Reference to the same file, don't copy another one). 

Click run.

You will have to find out your mouse location to click on the "change location" button at the bottom and the option of using your gpx file , we will be clicking on these two buttons constantly. Change the x,y in the clickAction function, you'll have to do some trial and error. 

```
def clickAction():
	os.system("./autoClicker -x 976 -y 880")
	time.sleep(1)
	os.system("./autoClicker -x 999 -y 600")
	time.sleep(1)
	print "clicking!!"
```
Open terminal and place it side by side with your xcode. cd to your folder and run the script using 

```
python eggrun.py
```

The script will start and if your clicking is set up correctly, it should be uploading the location onto your phone. 

Now the last step is to open Pokemon Go! Remember to close Pokemon go every time you start this script or you will be teleporting. (Even though it's a very small distance, you probably won't be banned for that)

##Configuration
Currently the script is set to move at the speed of 12km/h, which worked perfectly for me. you can play with it yourself to see if a faster speed would work.

# Have Fun!
