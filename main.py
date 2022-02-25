import os
import time
from digitalio import DigitalInOut
import board
from dotenv import load_dotenv, find_dotenv
from PIL import Image, GifImagePlugin
from adafruit_rgb_display.st7735 import ST7735

load_dotenv(find_dotenv())

#Configure GPIOs for Chip Select, DC Select and Reset pins
cs_pin:DigitalInOut = DigitalInOut(board.CE0)
dc_pin: DigitalInOut = DigitalInOut(board.D24) #RS
rst_pin: DigitalInOut = DigitalInOut(board.D23)

#Config for display baudrate (Default max is 64mhz)
BAUDRATE: int = 64000000

#Assign Hardware SPI
spi: board = board.SPI()

#Setup Display object
disp: ST7735 = ST7735(spi, width=128, height=128, rotation=270, cs=cs_pin, dc=dc_pin, rst=rst_pin, baudrate=BAUDRATE)

#Open Up Gif
gif: GifImagePlugin = Image.open('monkey_360_128.gif')

while True:
    print(f"Start of gif loading {gif.n_frames}")
    try:
        for frame_num in range(gif.n_frames):
            gif.seek(frame_num)
            # print(type(gif))
            print(f"Playing Frame Number: {frame_num}")
            #Convert PIL Image (Frame) to RGB and set the display to the current image
            disp.image(gif.convert("RGB"))
    except Exception as E:
        print(f"Exception caught: {E}. Waiting 30 seconds and then rebooting")
        # time.sleep(30)
        # os.system('reboot')

