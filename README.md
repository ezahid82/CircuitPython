# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

Here's how you make code look like code:

```python

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

```


### Evidence

![Hello mu ](Images/hello%20circute%20python%20gif.gif)

### Wiring

there was none ;)

### Reflection

This assignment was challengeing because I thought that we would be using arduino and turned out we used circuit python. The code was the most challenging part with the new way of coding that we required. I figured it out by finding out what the codes translated to from arduiono to circuit python. like **dot.fill** was to change color than arduino's manual L.E.D. change. **time.sleep** translated from **delay**. RGD values were also new to which **255** was the highest value.



## CircuitPython_Servo

### Description & Code

In this assignment, we made the servo move left and or right 90* using circuit python. The servo was turning left and right continuesly until we diconnected it. Then, we moved on to making it move using capacitive touch. The servo was able to move left when one wire is touched and right when another wire is touched. You didn't have to touch it physically, but just hover above it, and it will be able to move because of the magnetic force around it.


```python

"""CircuitPython Capacitive touch servo code."""
import time
import board
import pwmio
from adafruit_motor import servo
import touchio

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
touch_A5 = touchio.TouchIn(board.A5)  # Not a touch pin on Trinket M0!

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    if touch_A1.value:
        print("Touched A1!")
        for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)

    if touch_A5.value:
        print("Touched A5!")
        for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
            my_servo.angle = angle
            time.sleep(0.05)
    time.sleep(0.05)

```

### Evidence

![Servo Capacitive Touch ](Images/WIN-20210915-15-33-43-Pro.gif)


### Wiring

### Reflection
This assignment was a bit challenging at first because we are new to python and bash and this new way of coding and documenting. But, after doing some research online, I found out how to do the coding part which were a couple of "if" statements and "while" loops. It won't be challenging if you think of the code as logic and suedocoding. The servo moves when touched. "A5" etc...

---


## CircuitPython_LCD

### Description & Code

In this assignment we use **map range** to "map" the distance at certain heights and then change the color of metro as it corresponds. the heights **5**, **20**, **30** needs to change their color gradually drop red to green, and what ever in between. **rgb** values are also neccessary in making the **rainbow** color change.


```python
import adafruit_hcsr04
import time
import board
import neopixel
import simpleio

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
cm = 0
while True:
    try:
        cm = sonar.distance
        print((cm,))
        if (cm) <= 5:
            r = 255
            g = 0
            b = 0
            print("Make it red!")

        elif(cm) < 20:
            r = simpleio.map_range(cm, 5, 20, 255, 0)
            g = 0
            b = simpleio.map_range(cm, 5, 20, 0, 255)
            print("make it red - blue!")

        elif(cm) < 35:  # from cm = 20 to cm = 35
            r = 0
            g = simpleio.map_range(cm, 20, 35, 0, 255)
            b = simpleio.map_range(cm, 20, 35, 255, 0)
            print("make it blue-green!")

        else:
            r = 0
            g = 255
            b = 0

            print("make it green!")
        dot.fill((int(r), int(g), int(b)))

    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

```

### Evidence

### Wiring

### Reflection
This assignment was very difficult because *map ranging* was what I struggled with the most. I found online, a code of *map range* that I used and tinkered with, then added my *rgb values* to change color. next I will make sure that I have the right *rgb values* and *map range* so that my code and logic won't mess up and be confusing.



## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
