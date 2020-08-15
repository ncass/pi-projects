# Write your code here :-)
from gpiozero import LED
from gpiozero import MotionSensor
import time
MS = MotionSensor(24)
green = LED(4)
red = LED(17)
#red.on()
#green.on()
green.off()
red.off()
time.sleep(3)
if MS.motion_detected == True:
    for i in range(10):
        green.on()
        red.on()
        time.sleep(1)
        green.off()
        red.off()
        time.sleep(1)
    
