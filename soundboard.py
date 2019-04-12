import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
import os
import random
import subprocess
######################################
### Raspberry Pi Soundboard
### v1.01 - May 12, 2018
### Agent[31]/SXN31
######################################
GPIO.setmode(GPIO.BCM)
######################################
### Configuration
#Set working directory of soundboard files with a trailing slash
soundpath = "/home/pi/sounds/"
###
#Set path of files for each button with a trailing slash
redButtonPath = "warning/"
pinkButtonPath = "moviequotes/"
blueButtonPath = "gamequotes/"
greenButtonPath = "victory/"
bootPath = "boot/"
###
#Push buttons are NO (Normal Open) or NC (Normal Close)
#If your push button is NC select True, if it's NO select False.
redButtonNC = True
pinkButtonNC = False
blueButtonNC = False
greenButtonNC = False

#Initialize Initial Sound Settings.
#This should be configured to whatever rate your audio is. For best quality, ensure that all audio is encoded at the same rate.
pygame.mixer.init(48000, -16, 2, 4096) #provided defaults 
#pygame.mixer.init(44000, -16, 2, 4096) #this one doubled speed, made it only make ticking noises
###
#Configure which pins will be used:
GPIO.setup(23, GPIO.IN) #Red
GPIO.setup(17, GPIO.IN) #Pink
GPIO.setup(27, GPIO.IN) #Blue
GPIO.setup(25, GPIO.IN) #Green
#GPIO.setup(23, GPIO.IN)# raspberry pi1 pinouts
#GPIO.setup(24, GPIO.IN)# raspberry pi1 pinouts
#GPIO.setup(25, GPIO.IN) # raspberry pi1 pinouts
######################################
### End User Settings
######################################
#define text colors
redPrint = "\033[1;31;40m"
pinkPrint = "\033[1;35;40m"
bluePrint = "\033[1;34;40m"
greenPrint = "\033[1;32;40m"
bootPrint = "\033[1;33;40m"
normalPrint = "\033[1;37;40m"
######################################
######################################
#Verify Settings
#check if path is null
#check if soundpath has trailing slash
#check for trailing slash in file path
#check array if empty
#check if redButtonNo is either true or false
######################################
###Changelog
### 05.12.18 - v1.0.1
###     Added flag to prevent rapid fire of audio tracks
###     Added color text to the lists just for ease of reading the text
###     Python 3 compatible
### 03.05.18 - Initial Release
######################################
#Generate list of files
redSoundArray = []
for roots, dirs, files in os.walk(soundpath + redButtonPath, topdown=True):
    for file in files:
        if file.endswith('.wav'):
            redSoundArray.append(file)
        if file.endswith('.WAV'):
            redSoundArray.append(file)
print (redPrint,"Red (",len(redSoundArray),"):\n",redSoundArray,"\n")

pinkSoundArray = []
for roots, dirs, files in os.walk(soundpath + pinkButtonPath, topdown=True):
    for file in files:
        if file.endswith('.wav'):
            pinkSoundArray.append(file)
        if file.endswith('.WAV'):
            pinkSoundArray.append(file)
print (pinkPrint,"Pink (",len(pinkSoundArray),"):\n",pinkSoundArray,"\n")

blueSoundArray = []
for roots, dirs, files in os.walk(soundpath + blueButtonPath, topdown=True):
    for file in files:
        if file.endswith('.wav'):
            blueSoundArray.append(file)
        if file.endswith('.WAV'):
            blueSoundArray.append(file)
print (bluePrint,"Blue (",len(blueSoundArray),"):\n",blueSoundArray,"\n")

greenSoundArray = []
for roots, dirs, files in os.walk(soundpath + greenButtonPath, topdown=True):
    for file in files:
        if file.endswith('.wav'):
            greenSoundArray.append(file)
        if file.endswith('.WAV'):
            greenSoundArray.append(file)
print (greenPrint,"Green (",len(greenSoundArray),"):\n",greenSoundArray,"\n")

bootSoundArray = []
for roots, dirs, files in os.walk(soundpath + bootPath, topdown=True):
    for file in files:
        if file.endswith('.wav'):
            bootSoundArray.append(file)
        if file.endswith('.WAV'):
            bootSoundArray.append(file)
print (bootPath,"Boot (",len(bootSoundArray),"):\n",bootSoundArray,"\n")
print (normalPrint,"\n")
######################################
#Random Array Selector
######################################
def SelectRed():
	global sndA
	sndA = pygame.mixer.Sound(soundpath + redButtonPath + random.choice(redSoundArray))
def SelectPink():
	global sndB
	sndB = pygame.mixer.Sound(soundpath + pinkButtonPath + random.choice(pinkSoundArray))
def SelectBlue():
	global sndC
	sndC = pygame.mixer.Sound(soundpath + blueButtonPath + random.choice(blueSoundArray))
def SelectGreen():
	global sndD
	sndD = pygame.mixer.Sound(soundpath + greenButtonPath + random.choice(greenSoundArray))
def SelectBoot():
	global sndE
	sndE = pygame.mixer.Sound(soundpath + bootPath + random.choice(bootSoundArray))
################
#System Sounds
################
shutdownSound = pygame.mixer.Sound(soundpath + "system/Windows XP Shutdown.wav")
rebootSound = pygame.mixer.Sound(soundpath + "system/the_system_is_down_short.wav")
######################################
#End Function
######################################
######################################
#Set Sleep Interval
######################################
def sleeperAgent():
    sleep(.25)
######################################
#End Function
######################################

#sndA = pygame.mixer.Sound()
#sndB = pygame.mixer.Sound(PlaySound)
#sndC = pygame.mixer.Sound(PlayWarning)

soundChannelA = pygame.mixer.Channel(1)
soundChannelA.set_volume(1)
soundChannelB = pygame.mixer.Channel(2)
soundChannelB.set_volume(1)
soundChannelC = pygame.mixer.Channel(3)
soundChannelC.set_volume(1)
soundChannelD = pygame.mixer.Channel(4)
soundChannelD.set_volume(1)
soundChannelE = pygame.mixer.Channel(5)
soundChannelE.set_volume(1)
print ("Sampler Ready.")
#Play startup sound
SelectBoot()
soundChannelE.play(sndE)
######################################
#Sound flags
redOn = 0
pinkOn = 0
blueOn = 0
greenOn = 0
######################################
while True:
    try:
        if (GPIO.input(23) == False and GPIO.input(17) == True and GPIO.input(25) == True and GPIO.input(27) == True):
            pygame.mixer.stop()
            soundChannelA.play(shutdownSound)
            print('Shutdown')
            while pygame.mixer.get_busy() == True:
                if pygame.mixer.get_busy() == False:                
                    subprocess.Popen(['sudo','/sbin/poweroff','poweroff'])
                    break
        elif (GPIO.input(17) == True and GPIO.input(25) == True and GPIO.input(27) == True):
            pygame.mixer.stop()
            soundChannelA.play(rebootSound)
            print ("Reboot")
            while pygame.mixer.get_busy() == True:
                if pygame.mixer.get_busy() == False:                
                    subprocess.Popen(['sudo','/sbin/reboot','reboot'])
                    break
    #green Victory
        if (GPIO.input(25) == True and greenOn == 0 ):
    #if not (soundChannelA.get_busy()): #if i choose to uncomment this statement, remember to indent the below lines
            greenOn = 1
            SelectGreen()
            soundChannelA.play(sndD)
            sleeperAgent()
    #pink Failure
        if (GPIO.input(17) == True and pinkOn == 0):
    #if not (soundChannelB.get_busy()):
            pinkOn = 1
            SelectPink()
            soundChannelB.play(sndB)
            sleeperAgent()
    #blue sounds
        if (GPIO.input(27) == True and blueOn == 0):
    #if not (soundChannelC.get_busy()):
            blueOn = 1
            SelectBlue()
            soundChannelC.play(sndC)
            sleeperAgent()
    #This is set to false to allow for my default open Halon abort button
    #red WARNING
        if (GPIO.input(23) == False and redOn == 0):
    #if not (soundChannelD.get_busy()):
            redOn = 1
            SelectRed()
            soundChannelD.play(sndA)
            sleeperAgent()
            #Reset flags to false
        if (GPIO.input(25) == False ):
            greenOn = 0
        if (GPIO.input(17) == False ):
            pinkOn = 0
        if (GPIO.input(27) == False ):
            blueOn = 0
        if (GPIO.input(23) == True ):
            redOn = 0            
    except KeyboardInterrupt:
        exit()