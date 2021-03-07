#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import icons

HOST = "localhost"
PORT = 4223
UID  = "Svi"  # CO2 Bricklet 2.0
UID1 = "R5P"  # LCD 128x64 Bricklet
UID2 = "QqZ"  # Air Quality Bricklet
UID4 = "QaX"  # Hat Brick
UID5 = "R7i"  # Piezo Speaker Brcklet
WIDTH = 128   # Columns
HEIGHT = 64   # Rows
icon   = None
t = 0         # time
dt = 3000     # callback time intervall
BL = 100      # Backlight
tab = 0       # gui_tab
alt_btn = 3   # Alertt Button
merker = 0    # for Alert Button
l = []        # list for display gui graph
l1 = []

from tinkerforge.ip_connection import IPConnection
from tinkerforge.brick_hat_zero import BrickHATZero
from tinkerforge.bricklet_co2_v2 import BrickletCO2V2
from tinkerforge.bricklet_air_quality import BrickletAirQuality
from tinkerforge.bricklet_lcd_128x64 import BrickletLCD128x64
from tinkerforge.bricklet_piezo_speaker_v2 import BrickletPiezoSpeakerV2

# draw icon from icons
def draw_icon(x, y, icon):
    lcd.write_pixels(x, y, x + icon.WIDTH-1, y + icon.HEIGHT-1, icon.data)

def iaq_acc(iaq_ac):
    if iaq_ac == BrickletAirQuality.ACCURACY_UNRELIABLE:
        return "Unrel"
    elif iaq_ac == BrickletAirQuality.ACCURACY_LOW:
        return "Low  "
    elif iaq_ac == BrickletAirQuality.ACCURACY_MEDIUM:
        return "Med  "
    elif iaq_ac == BrickletAirQuality.ACCURACY_HIGH:
        return "High "

def get_alert(al):
    if al == 1:
        iaq_max = 100
        co2_max = 1000
    elif al == 2:
        iaq_max = 150
        co2_max = 1500
    else:
        iaq_max = 200
        co2_max = 2000
    return iaq_max, co2_max    

# Callback function for GUI slider value callback
def cb_gui_slider_value(index, value):
    global BL, dt
    if index == 0:
      BL= value*100/50
      lcd.set_display_configuration(14,BL,False, True)
    elif index == 1:
      CI=value/52*6000
      if CI > 1000:
        dt = CI
      
# Callback function for GUI button pressed callback
def cb_gui_button_pressed(index, pressed):
  global alt_btn, merker
  if index == 0:
    time.sleep(5)
    lcd.clear_display()
    lcd.remove_all_gui()
    os.system("sudo shutdown -h now")
  elif index == 1:
    time.sleep(0.8)
    if pressed == True:
        if merker == 1:
            alt_btn = alt_btn +1
            if alt_btn == 4:
                alt_btn = 1
        lcd.draw_text(65, 12, 0, True, "SetAlert "+str(alt_btn))
        merker = 1

# Callback function for GUI tab selected callback
def cb_gui_tab_selected(index):
  global tab, BL, dt, merker
  lcd.remove_gui_button(0)
  lcd.remove_gui_button(1)
  lcd.remove_gui_slider(0)
  lcd.remove_gui_slider(1)
  lcd.remove_gui_graph(0)
  lcd.clear_display()
  co2.set_all_values_callback_configuration(dt, False)
  aq.set_all_values_callback_configuration(dt, False)
  if index == 0:
    tab = 0
  elif index == 1:
    tab = 1
    lcd.remove_gui_graph(1)
    lcd.set_gui_graph_configuration(0, lcd.GRAPH_TYPE_DOT, 10, 0, 100, 50, "t", "IAQ")
  elif index == 2:
    tab = 2
    lcd.remove_gui_graph(0)
    lcd.set_gui_graph_configuration(1, lcd.GRAPH_TYPE_DOT, 10, 0, 100, 50, "t", "CO2")
  elif index == 3:
    tab = 3
    lcd.remove_gui_graph(0)
    lcd.remove_gui_graph(1)
    lcd.set_gui_button(0, 0, 0, 60, 22, "Shutdown")
    lcd.set_gui_button(1, 62, 0, 65, 22, "")
    lcd.write_line(3,1,"Backlight")
    lcd.set_gui_slider(0, 0, 35, 60, lcd.DIRECTION_HORIZONTAL, BL*50/100)
    lcd.write_line(3,11,"Callback")
    lcd.set_gui_slider(1, 64, 35, 60, lcd.DIRECTION_HORIZONTAL, dt*52/6000)
    lcd.draw_text(65, 3, 0, True, "Version1.1")
    lcd.draw_text(65, 12, 0, True, "2021/02/28")
    merker = 0

# Callback function for all values callback 
def cb_all_values(co2_concentration, temperature, humidity):
    global t,tab,l
    t = t + dt/1000
    air_pressure = aq.get_air_pressure()
    co2.set_air_pressure(air_pressure // 100)
    co2_concentration, temperature, humidity = co2.get_all_values()
    y = int(255/3000 * co2_concentration)
    if len(l) < 100 and y < 255:
      l.append(y)
    else:
      l = []
    if tab == 0:
      screen_text(t, co2_concentration, temperature, humidity)
    elif tab == 2:
      if co2_concentration < 800:
        draw_icon(100, 15, icons.IconThumbsUp)
      elif co2_concentration < 1500:
        draw_icon(100, 15, icons.IconThumbsSide)
      elif co2_concentration < 2000:
        draw_icon(100, 15, icons.IconThumbsDown)
      else:
         lcd.clear_display()
         lcd.write_line(1,15,"ALERT")
      lcd.write_line(0, 8,'{0:6.0f}'.format(co2_concentration)+ " ppm")
      lcd.set_gui_graph_data(1, l) 
    elif tab == 3:
     lcd.write_line(3, 19,'{0:1.0f}'.format(dt/1000)+'s')
     
def cb_all_values1(iaq_index, iaq_index_accuracy, temperature, humidity, air_pressure):
    global tab,l1
    iaq_index, iaq_index_accuracy, temperature, humidity, air_pressure = aq.get_all_values()
    y = int(255/300 * iaq_index)
    if len(l1) < 100 and y < 255:
      l1.append(y)
    else:
      l1 = []
    if tab == 0:
      screen_text1(iaq_index, iaq_index_accuracy, temperature, humidity, air_pressure)
    elif tab == 1:
      if iaq_index < 50:
        draw_icon(100, 15, icons.IconThumbsUp)
      elif iaq_index < 150:
        draw_icon(100, 15, icons.IconThumbsSide)
      elif iaq_index < 200:
        draw_icon(100, 15, icons.IconThumbsDown)
      else:
         lcd.clear_display()
         lcd.write_line(1,15,"ALERT")
      lcd.write_line(0, 8,'{0:3.0f}'.format(iaq_index))
      lcd.write_line(0, 15,iaq_acc(iaq_index_accuracy))
      lcd.set_gui_graph_data(0, l1)
         
# function for Text on tab 0
def screen_text(ti, co2, temp, hum):
    lcd.write_line(0, 0,'Time  ' + time.strftime('%j:%H:%M:%S', time.gmtime(ti)))
    lcd.write_line(1, 0,'CO2     {0:6.0f}'.format(co2)+ " ppm")
def screen_text1(iaq, iaq_ac, temp,hum, air_p):
    lcd.write_line(2, 0,'Temp    {0:6.1f}'.format(temp/100.0) + " " + chr(0xF8)+ "C")
    lcd.write_line(3, 0,'Humidity{0:6.1f}'.format(hum/100.0) + " %RH")
    lcd.write_line(4, 0,'Pressure{0:6.0f}'.format(air_p/100.0) + " hPa")
    lcd.write_line(5, 0,'IAQ/Acc {0:6.0f}'.format(iaq))
    lcd.write_line(5,15,iaq_acc(iaq_ac))


# mein    
if __name__ == "__main__":
    icon = icons.IconTabGraph
    ipcon = IPConnection() # Create IP connection
    co2 = BrickletCO2V2(UID, ipcon) # Create device objects
    lcd = BrickletLCD128x64(UID1, ipcon) 
    aq = BrickletAirQuality(UID2, ipcon)
    ps = BrickletPiezoSpeakerV2(UID5, ipcon)
    hat = BrickHATZero(UID4, ipcon)
    ipcon.connect(HOST, PORT) # Connect to brickd
    # Don't use device before ipcon is connected

    # Register GUI slider value callback to function cb_gui_slider_value
    lcd.register_callback(lcd.CALLBACK_GUI_SLIDER_VALUE, cb_gui_slider_value)
    # Register GUI button pressed callback to function cb_gui_button_pressed
    lcd.register_callback(lcd.CALLBACK_GUI_BUTTON_PRESSED, cb_gui_button_pressed)
    # Register GUI tab selected callback to function cb_gui_tab_selected
    lcd.register_callback(lcd.CALLBACK_GUI_TAB_SELECTED, cb_gui_tab_selected)

    lcd.remove_all_gui()
    lcd.clear_display()
    
    lcd.set_gui_tab_configuration(lcd.CHANGE_TAB_ON_CLICK_AND_SWIPE, False)
    lcd.set_gui_tab_text(0, "Text")
    lcd.set_gui_tab_text(1, "IAQ")
    lcd.set_gui_tab_text(2, "CO2")
    lcd.set_gui_tab_text(3, "Setup")
    lcd.set_gui_slider_value_callback_configuration(200, True)
    lcd.set_gui_button_pressed_callback_configuration(200, True)
    lcd.set_gui_tab_selected_callback_configuration(200, True)

    # Register all values callback to function cb_all_values
    co2.set_temperature_offset(180)
    co2.register_callback(co2.CALLBACK_ALL_VALUES, cb_all_values)
    # Set period for all values callback to 1s (3000ms)
    co2.set_all_values_callback_configuration(dt, False)

    # Register all values callback to function cb_all_values
    aq.set_temperature_offset(320)
    aq.register_callback(aq.CALLBACK_ALL_VALUES, cb_all_values1)
    # Set period for all values callback to 1s (3000ms)
    aq.set_all_values_callback_configuration(dt, False)

    # Watchdog: Restart after 10 seconds without feetback
    while True:
     iaq_x, co2_x =get_alert(alt_btn)   
     iaq, iaq_a = aq.get_iaq_index()
     if iaq > iaq_x and iaq_a >1 and co2.get_co2_concentration() > co2_x:
         ps.set_alarm(250, 750, 1, 5, 0, 10000)
     time.sleep(1)

    input("Press key to exit\n") # Use raw_input() in Python 2
    ipcon.disconnect()
