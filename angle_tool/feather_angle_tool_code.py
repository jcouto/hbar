# This is a tool to measure the angle of the headbar holder
# Can be built from Adafruit
#     microcontroller: Adafruit Feather M4 express
#     lcd display: Adafruit sh1107
#     orientation sensor: Adafruit BNO055
#     (optional) battery: Adafruit 2750 - lipoly 3.7V 400mAh
#
# Coded with CircuitPython 7
# http://github.com/jcouto/hbar
# Joao Couto - November 2021

import board
import digitalio
import displayio
import analogio

import terminalio
import busio
import adafruit_bno055  # sensor

from adafruit_display_text import label
import adafruit_displayio_sh1107  # for the display
import time

displayio.release_displays()

i2c = board.I2C()
# load devices
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
sensor = adafruit_bno055.BNO055_I2C(i2c)
vbat  = analogio.AnalogIn(board.VOLTAGE_MONITOR)
mode = 'absolute' # or relative
mode_button = digitalio.DigitalInOut(board.D5)
mode_button.switch_to_input(pull=digitalio.Pull.UP)

position = [0,0,0]
zero = [0,0,0]
def battery():
    return (vbat.value*3.3)/65536*2

# SH1107 is 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 1

display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0
)

# Make the display context
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(WIDTH, HEIGHT, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White
inner_bitmap = displayio.Bitmap(WIDTH - BORDER * 2, HEIGHT - BORDER * 2, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

text1 = '''hbar angle tool

    http://github.com/
jcouto/hbar
'''  # overly long to see where it clips
text_area = label.Label(terminalio.FONT, text=text1, scale=1, color=0xFFFFFF, x=3, y=3)
splash.append(text_area)
for i in [1,0.8,0.6,0.4,0.2,0.01]:
    display.brightness = i
    time.sleep(0.1)
time.sleep(2)

while True:
    
    p = sensor.euler # read the sensor
    
    if not mode_button.value: # handle button press
        if mode == 'absolute':
            mode = 'relative'
            zero[0] = p[0]
            zero[1] = p[1]
            zero[2] = p[2]
        else:
            mode = 'absolute'
            zero = [0, 0, 0]
        while not mode_button.value: # wait
            pass
    
    position[0] = p[0] - zero[0]
    position[1] = p[1] - zero[1]
    position[2] = p[2] - zero[2]

    text1 = '''X: {0:.1f} deg 
Y: {1:.1f} deg
Z: {2:.1f} deg'''.format(*position)

    if battery() < 3.3:
        text1 += '''
        charge'''
    else:
        text1 += '''
        {0} mode'''.format(mode)
        
    text_area.text=text1
    time.sleep(0.05)
