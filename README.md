# Air Qualiy Monitor Project 

## What the project does

### Create an indoor air quality monitor station with [tinkerforge.com](https://tinkerforge.com/en/doc/) bricklets and a raspberry pi zero.
![Image 1](/images/IMG_6932.png)

The station uses an [Integrated Air Quality (IAQ) sensor](https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Air_Quality.html#air-quality-bricklet) and a [CO2 sensor](https://www.tinkerforge.com/en/doc/Hardware/Bricklets/CO2_V2.html) to monitor air quality inside the room. An [alert sound](https://www.tinkerforge.com/en/doc/Hardware/Bricklets/Piezo_Speaker_V2.html#piezo-speaker-v2-bricklet) is generated, when both sensors detect bad air quality. The alert level can be adjusted via setup. The porject is based on the modification of the [Tabletop Weather Station](https://www.tinkerforge.com/en/doc/Kits/TabletopWeatherStation/TabletopWeatherStation.html).

![Image 2](/images/IMG_6935.png)

A graph is plotted for both sensor outputs (IAQ and CO2):

![Image 3](/images/IMG_6936.png)

![Image 3](/images/IMG_6937.png)

## Why the project is useful

The air quality - espaciually inseide classrooms - came into focus in relation wuth aerosol formation causing Cvid 19 infections. Monitoring can provide data to ensure in time room ventilaton. So good air quality can be achived and aerosole formation can be avoided. 

Indoor air quality characteristic is related to CO2-concentration and Air Quality Index. The different quality ranges are illustrated below.

![Image 5](/images/CO2.png)

The CO2 Bricklet provides the capability to measure CO2 concentration in the air. The measured CO2 concentration can be read out in ppm.The Bricklet also measures temperature and humidity. These are used internally for compensation and can additionally be read out.

![Image 6](/images/IAQ.png)

The IAQ index is a measurement for the quality of air. To calculate the IAQ index the Bricklet detects ethane, isoprene (2-methylbuta-1,3-diene), ethanol, acetone and carbon monoxide (often called VOC, volatile organic components) by adsorption. These gas measureme nts are combined with the measurements of air pressure, humidity and temperature to calculate the final IAQ index.

There are 3 alert level avaluable. Preset ist level 3. 

Alert level  | CO2 (ppm)   | IAQ
____________ | ___________ | _____
 3 | 2000  | 200
 2 | 1500  | 150
 1 | 1000  | 100

## How users can get started with the project

## Where users can get help with your project

## Who maintains and contributes to the project
