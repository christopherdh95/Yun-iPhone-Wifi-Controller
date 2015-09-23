# Wifi-Controller
This project is for controlling whatever you want over wifi from your iPhone using OSC(Open Sound Control) communication and the TouchOSC app and an arduino Yún.

Sorry if this instillation is unclear and hard to follow.  I'm very busy with other work in college and tossed this together quickly.  Please ask any questions and I'll try to get back when I can.  

There are three main components of communication in this project: the OSC app on an iPhone, the linux chip (Atheros AR9331) on the Yún, and the ATmega32u4 chip which recieves signal from the Atheros chip per Arduino's bridge communication protocal.  First, OSC communication is sent from the TouchOSC app (http://hexler.net/software/touchosc) on a phone to the Atheros chip on the Arduino Yún over a local wifi networks.  This communication is recieved by the Atheros chip and the piece of python code above.  The piece of arduino code above then takes the signal from the Atheros chip over the Yun's bridge and executes them.

All the code should be modified with the OSC layout you use in both the Arduino and Python files.  TouchOSC has a very simple and nice IDE where you can add toggles, sliders, and whatnot.  Your layouts can be easily uploaded to your iPhone.  Right now I have two toggles and a slider included in the code.  

Instillation Instructions:
1. Format Yún and SD card for Yún.  Look up how to do this if you've never down it before.  The SD card should contain a downloaded copy of the arduino OSC library (https://github.com/CNMAT/OSC) and the piece of python code above. The code should be placed in an apporpiate file path like sda1/Arduino/www/python within the SD card. This is probably the trickiest part to get working.  Make sure you change the IP's in the .py file to those of your Yún and iPhone.  
2. Create a touchOSC format using touchOSC's IDE.  Perhaps this should be done before the first step.
3. Connect the Arduino Yún to your computer and upload the Arduino sketch.  
4. Connect components to your Arduino to the respective ports assinged in the sketch.  Feel free to take away, change, and mess around with it.  I started with hooking up a 5v relay to control a string of LED's in my room.
5. ssh to the Yún from a terminal.  Find the python file and run it.  Expect it to fail and go from there!  
6. Note: It's useful to run, for example, python oscpython.py &.  The '&' keeps the program running in the background, so even when you exit terminal it'll still run.  To stop it you could unplug the Yún or find the PID of the process and kill it.  i.e. type ps, find the pid and type 'kill #pid' (where #pid is the number of the pid).


Extension & Extra Notes:
1. The server you're on will assign a dynamic IP for both your phone and Yún.  This means that if the system reboots the OSC controller yoy made won't work until you adjust the IP's in the .py file.  At my house, I have a home server so I was able to assign a port to my Yun and phone giving them static IP's and also enabling me to control stuff outside my local network.  Kinda cool but also a little scary, given the lack of security with this whole setup.  Another idea would be when you boot the Yún to find the IP of your phone and yún and assign those values to the ip's in the python code.  I haven't looked into this too much, but the find IP program within my github could be a good place to start.
2. I had problems setting this up in my dorm room.  The college I go to uses a wpe2-enterprise encryption on their wireless internet and generally looks down on setting up servers off their own network.  After talking to the IITS at my school, they took interest in the project and tried to help me out, but we could never find a solution given that yún's don't support this encryption.  I instead opted to control everything using a 4d systems touch screen and some radio transcievers.  Not as classy but it still works well.
3. Also, perhaps a daemon for the python program within the Arduino's bootup could remove the need to ssh to the yún everytime you want to run the program. This would be useful if you were going for a more permanent instillation.
