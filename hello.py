# Made by Ezhar!
import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1


while True:
    print("Make it red!")
    print("Make it red!")
    dot.fill((0, 225, 0))
    time.sleep(.5)
    print("Make it Blue")
    dot.fill((225, 0, 0))
    time.sleep(.5)
