import adafruit_hcsr04
import time
import board
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    if (sonar.distance <= 5.00)
    dot.fill(255, 0, 0)
