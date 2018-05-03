import pyttsx
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
flag = "abc"
prev = "xyz"

print("dIST MEASUREMENT")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting for sensor")
time.sleep(2)

def saying(tosay):
    engine = pyttsx.init()
    engine.say(tosay)
    engine.runAndWait()

while(True):
    GPIO.output(TRIG, True)
    time.sleep(0.2)
    GPIO.output(TRIG, False)

    while(GPIO.input(ECHO)==0):
        pulse_start = time.time()

    while(GPIO.input(ECHO)==1):
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    prev = flag
    if(distance < 50):
        tosay = "Obstacle at " + str(distance) + "centi meter"
        flag = "yes"
    else:
        tosay = "obstacle not detected"
        flag = "no"

    if(flag != prev):
        if(flag == "yes"):
            saying(tosay)

GPIO.cleanup()
