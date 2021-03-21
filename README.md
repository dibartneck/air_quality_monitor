# Air Quality Monitor Project 

## What the project does

### Create an indoor air quality monitor station with [tinkerforge.com](https://tinkerforge.com/en/doc/) bricklets and a raspberry pi zero.
![Image 1](/images/IMG_6932.png)

The station uses an [Integrated Air Quality (IAQ) sensor](https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Air_Quality.html#air-quality-bricklet) (BME680) and a [CO2 sensor](https://www.tinkerforge.com/en/doc/Hardware/Bricklets/CO2_V2.html) (SCD30) to monitor air quality inside the room. An [alert sound](https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Piezo_Speaker_V2.html#piezo-speaker-v2-bricklet) is generated, when both sensors detect bad air quality. The alert level can be adjusted via setup. The project is based on a modification of the [Tabletop Weather Station](https://www.tinkerforge.com/en/doc/Kits/TabletopWeatherStation/TabletopWeatherStation.html).

![Image 2](/images/IMG_6940.png)

A graph is plotted for both sensor outputs (IAQ and CO2):

![Image 3](/images/IMG_6941.png)

![Image 3](/images/IMG_6942.png)

## Why the project is useful

The air quality - especially inside classrooms - came into focus in relation with aerosol formation causing Cvid 19 infections. Monitoring can provide data to ensure in time room ventilation. Good air quality can be achieved and aerosol formation can be avoided. 

Indoor air quality characteristic is related to CO2-concentration and Air Quality Index. The different quality ranges are illustrated below.

The CO2 Bricklet ([SCD30](https://github.com/Tinkerforge/co2-v2-bricklet/raw/master/datasheets/SCD30.pdf)) provides the CO2 concentration in ppm. The Bricklet also measures temperature and humidity. These values are used for internal compensation and can additionally be read out.

![Image 5](/images/CO2.png)

The IAQ index is a measure for the quality of air. To calculate the IAQ index the Bricklet ([BME680](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf) detects ethane, isoprene (2-methylbuta-1,3-diene), ethanol, acetone and carbon monoxide (often called VOC, volatile organic components) by adsorption. These gas measurements are combined with the measurements of air pressure, humidity and temperature to calculate the final IAQ index.

![Image 6](/images/IAQ.png)

There are 3 alert level available via setup. Preset is level 3. 

Alert level  | CO2 (ppm) |  IAQ
:----------: | --------: |  --------
 3 | 2000  | 200
 2 | 1500  | 150
 1 | 1000  | 100

## How users can get started with the project

### 1. Parts and Assembly

Before starting the project you should get the following parts from [tinkerforge shop](https://www.tinkerforge.com/en/shop/):
Quantity | Part   | Price (in €)
-------: | ------ | ------------:
1 | CO2 Bricklet 2.0 | 89.99
1 | Air Quality Bricklet | 29.99
1 | LCD Bricklet 128x64 | 32.99
1 | HAT Zero Brick | 14.99
1 | Tabletop Weather Station | 15.99
4 | Bricklet Cable (7p - 7p) | 0.79
1 | Mounting Kit 12 mm | 1.69
2 | Mounting Kit 9 mm | 1.69
1 | Mounting Kit for Raspberry PI Zero| 1.99

Further you need the following parts for the raspberry. A raspberry zero wm is recommended because it fits into the tabletop station enclosure:
Quantity | Part | Price (in €)
-------: | ---- | -----------:
1 | Raspberry Pi Zero WM| 19.99
1 | USB A to USB micro cable | 3.99
1 | SD Card 16 GB | 12.99
1 | USB Power Supply | 6.99

Assembly of the station is in analogy to the Tabletop weather station. You should fix the raspberry zero with double-sided adhesive tape. Be careful not damaging the bricklet cables.

### 2. Software and Installation

The best way to install the necessary software on Raspberry is to prepare the SD card on a PC or Mac. Use [Raspberry Pi Imager](https://www.raspberrypi.org/software/). Then prepare the image for [headless operation](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) of the raspberry (ssh and vnc). It is recommended to set up also your Wifi preferences, the pi zero has no ethernet port.

When you have got remote access to your raspberry, install the Python [IDLE](https://projects.raspberrypi.org/en/projects/generic-python-install-python3#linux) next. You further have to set up the tinkerforge [Brick Deamon](https://www.tinkerforge.com/en/doc/Software/Brickd.html#brickd) and [Brick Viewer](https://www.tinkerforge.com/en/doc/Software/Brickv.html#brickv). You can now test the HAT connection and the Bricklet functionality. Write down the UID's of the HAT Brick and all Bricklets. You have to enter the UID's in he Python Code before running the program.

Before you can run the application you have copied from this site please install the [API for Python](https://www.tinkerforge.com/en/doc/Software/API_Bindings_Python.html#api-bindings-python).

To autostart the python program after rebooting you can add a line in crontab. So you don't have to start the Python code remotely over VNC.


## Where users can get help with your project

I'm happy to help if there are any questions.

## Who maintains and contributes to the project

It would be great to see how others use the project. So please contribute!
