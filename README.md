# Overview
## Overall Flow
1. you provide your current location to the app, which then calculate a path around you
2. Based on the path it then generates gpx file constantly
3. Create a blank project referencing the gpx and simulate on your playing device
4. auto click the xcode buttons to constantly uploading the location

##What do I need?
A mac and an iphone/ipad. An android version is still under development, any help would be appreciated.

##What can I do with this app?
1. Hatch pokemon eggs
2. Collect rewards from local poke stops when you "walk" around
3. Catch any pokemon that appears when you "walk"
4. Explore any location given an address (If you disconnect you will teleport back, and you could be banned for a 1-2 hours)
5. Show off to your friends
6. Be a lazy Slowpoke in your couch

## Will I be banned?
There are softbans(a few hours) for players that spoof locations. The system does this by calculating the speed you move. Say you spoofed your location to NYC, then you disconnected and you will be back at your current loaction, then you will be moving too fast and you will be banned.

## How do I know if I'm banned
you can walk around normally, but you cannot hatch eggs, fight in gyms, collect rewards from Pokestops.
Most obviously, you will still encounter pokemons, but they escape 100% when you try to catch them.
The ban lasts around 2 hours usually, I haven't seen anyone that got permabanned.

### If you just use this app to walk around in your neighborhood, it's very unlikely the server will ban you.

Using this app you will be just "runing" around your house, so the system will not detect that you are location spoofing.

##Disclaimer
Use at your own risk.

#Instruction
First of all you need XCODE for this to work, you can explore other options for androids and use the same logic under "eggrun.py"

This is a fork from https://github.com/kahopoon/Pokemon-Go-Controller , see the original project for more instructions.

Clone/download this project. 

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

The script will ask for your current address, type the full address including including the country to avoid being located to a completely different place. Do NOT use comma, just use spaces.

Then the script will ask you to confirm your location so you don't get banned from teleporting. simply type "Y" to continue.

The script will start and if your clicking is set up correctly, it should be uploading the location onto your phone. 

Now the last step is to open Pokemon Go! Remember to close Pokemon go every time you start this script or you will be teleporting. (Even though it's a very small distance, you probably won't be banned for that)

##Configuration
Currently the script is set to move at the speed of 12km/h, which worked perfectly for me. you can play with it yourself to see if a faster speed would work.

# Have Fun!
