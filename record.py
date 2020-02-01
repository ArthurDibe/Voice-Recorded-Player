#!/usr/bin/python3
 
###############################################################
# 
# This python module uses the sounddevice library
# in order to record an audio on LINUX environment
# by using the computer's microphone, and this module
# uses the spicy to write the recorded block of audio
# in a .wav file
#
# File: record.py
# Version: 1.0
# Date: 2019-09-28
# Developer: Arthur
#
################################################################
 
import sounddevice as sd                # library to record
from scipy.io.wavfile import write      # library to write audio files
 
import sys      # receive the arguments from the system

print("..................................................................\n");
print ("RECORDING STARTED !!!");

size = len(sys.argv); # get the size of the array of pointer 

fs = 48000;     # Sample rate
seconds = 3;    # Duration of recording

print ("\n",seconds," seconds of recording ...");

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2);
sd.wait();      # Wait until recording is finished

if size == 0:
        write("audio.wav", fs, myrecording);  # Save as WAV file
else:
        write("audio{}.wav".format(size), fs, myrecording);  # Save as WAV file
