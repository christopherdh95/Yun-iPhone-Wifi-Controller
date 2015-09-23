from OSC import OSCServer,OSCClient, OSCMessage
import sys
from time import sleep
import types
import re
import urllib
sys.path.insert(0, '/usr/lib/python2.7/bridge/') 

from tcp import TCPJSONClient
													 

json = TCPJSONClient('127.0.0.1', 5700)
server = OSCServer( ("192.168.0.237", 8000) )#change to your yun's ip here
client = OSCClient()
client.connect( ("192.168.0.244", 9000) )#change to your phone's ip


def handle_timeout(self):
	print ("")

server.handle_timeout = types.MethodType(handle_timeout, server)

def toggle_callback(path, tags, args, source):
	global toggle1Feedback
	if path=="/1/toggle1":
		toggle1Feedback = float(args[0])
		json.send({'command':'put', 'key':'D11', 'value':'%i' % (toggle1Feedback)})

def toggle1_callback(path, tags, args, source):
    global toggle2Feedback
    if path=="/1/toggle2":
        toggle2Feedback = float(args[0])
        json.send({'command':'put', 'key':'D9', 'value':'%i' % (toggle2Feedback)})

"""def fader_callback(path, tags, args, source): # just an example if you wanted to include a fader or something.
    global fader1Feedback                         # these are just ideas of how you would format the things you could want to include
        if path=="/1/fader1":
            fader1Feedback = float(args[0])
                msg = OSCMessage("/1/label1")
                msg.insert(0, fader1Feedback)
                json.send({'command':'put', 'key':'D13', 'value':'%i' % (fader1Feedback)})
                client.send(msg)"""

server.addMsgHandler( "/1/toggle1",toggle_callback) 
server.addMsgHandler( "/1/toggle2",toggle1_callback)
#server.addMsgHandler( "/1/fader1",fader_callback)

while True:
	server.handle_request()

server.close()
