# raspberrypi_soundboard
A soundboard project built around python and a raspberry pi

Yeah the code is messy / amateur hour but I haven't had a chance to go rework it. Especially since everything as it is just works.

Install Raspian and copy soundboard files to /home/pi direcotry

Create the autostart piece:
pico ~/.config/lxsession/LXDE-pi/autostart

add the following lines:
@amixer set PCM -- 400.
@sudo python /home/pi/soundboard.py

The Amixer set PCM -- 400 line is a volume setting when I was troubleshooting volume issues. Not sure if it's still needed but it's included in my startup script. https://www.raspberrypi.org/forums/viewtopic.php?t=14966
It could be the reason I hear more static in the background,  hahaha.
