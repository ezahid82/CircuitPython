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
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




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

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
