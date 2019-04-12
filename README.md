# raspberrypi_soundboard

## Description
A soundboard project built around python and a raspberry pi. I found the initial source code from https://makezine.com/projects/make-33/simple-soundboard/ and built my prototype on a breadboard with the original Raspberry Pi. When I decided to build the actual device I had to upgrade to the Raspberry Pi 3 as the HATs were only being manufactured for the newer models. I mocked up a case design in Google Drawings and a buddy of mine built out the 3d model in CAD and 3d printed it for me with my specifications. I found the cool LED switches online at amazon, here's a few links to them. The red button is a halon abort button I took from a decomissioned data center at an old job.

LED Momentary Push Buttons

https://www.amazon.com/gp/product/B01I9KDVWQ/ref=oh_aui_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B01I9KDUC2/ref=oh_aui_search_asin_title?ie=UTF8&psc=1
https://www.amazon.com/gp/product/B01I9KDVXK/ref=oh_aui_search_asin_title?ie=UTF8&psc=1

Speaker

https://www.amazon.com/gp/product/B00CXLCMGY/ref=oh_aui_search_asin_title?ie=UTF8&psc=1


Yeah the code is messy / amateur hour but I haven't had a chance to go rework it. Especially since everything as it is just works.

## Install Guide
Install Raspian and copy soundboard files to /home/pi direcotry

Create the autostart piece:
pico ~/.config/lxsession/LXDE-pi/autostart

add the following lines:
@amixer set PCM -- 400.
@sudo python /home/pi/soundboard.py

### Note:
The Amixer set PCM -- 400 line is a volume setting when I was troubleshooting volume issues. Not sure if it's still needed but it's included in my startup script. https://www.raspberrypi.org/forums/viewtopic.php?t=14966
It could be the reason I hear more static in the background,  hahaha.

![Mockup](https://github.com/SXN31/raspberrypi_soundboard/blob/master/Raspberry%20Pi%20Soundboard%20Case.jpg)
