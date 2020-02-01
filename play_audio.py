#!/usr/bin/python3

###############################################################
# 
# This python module uses the playsound library
# in order to play an audio on LINUX environment
#
# File: play_audio.py 
# Version: 1.0
# Date: 2019-09-28
# Developer: Arthur
#
################################################################

from playsound import playsound	#library to play audio files

import sys	# receive arguments from system

size = len(sys.argv);
element = sys.argv;
print("..................................................................\n");
print("LIST OF AUDIO\n")

for i in range(size):
	if i > 0: print(i,") ",element[i]);

option = int(input("\nPlease, ENTER one option (0 to exit): "));

while True:	
	if option > 0 and option < size:
		print("NOW PLAYING: ", element[option]);
		playsound(element[option]);
		break;
	elif option == 0: 
		break;

	option = int(input("Please enter a VALID option: "));
