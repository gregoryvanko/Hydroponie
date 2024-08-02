import time
import RPi.GPIO as GPIO
import os

def measure():
  speed_of_sound = 34300 
  GPIO.output(TRIG_PIN, True) 
  time.sleep(0.00001) 
  GPIO.output(TRIG_PIN, False) 
  start = time.time()
  while GPIO.input(ECHO_PIN) == 0:
    start = time.time()
    
  while GPIO.input(ECHO_PIN) == 1:
    stop = time.time()

  elapsed = stop - start
  distance = (elapsed * speed_of_sound) / 2
  return distance

def measure_average():
  distance1 = measure()
  time.sleep(0.1)
  distance2 = measure()
  time.sleep(0.1)
  distance3 = measure()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance

GPIO.setmode(GPIO.BOARD)

TRIG_PIN = int(os.environ["TRIG_PIN"])
ECHO_PIN = int(os.environ["ECHO_PIN"])

GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.output(TRIG_PIN, False)
time.sleep(0.5)
distance = measure_average()
print('{:5.1f}'.format(distance))
GPIO.cleanup((TRIG_PIN, ECHO_PIN))