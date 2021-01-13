import time
import board
import neopixel

from TempController import TemperatureController

myContainer = TemperatureController()

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

currentTime = 0.0
lastTime = time.monotonic()

for i in range(100):
  currentTemperature = myContainer.getTemperature()
  if(currentTemperature< 76.0):
    myContainer.heaterOn(100)
  else:
    myContainer.heaterOff()
  myContainer.update()

  #Set the Metro LED to be red when the heater is on
  if(myContainer.heaterIsOn()):
    led[0] = (255, 0, 0)
  else:
    led[0] = (0, 0, 0)

  currentTime = time.monotonic() - lastTime + currentTime
  lastTime = time.monotonic()
  print(currentTime,",",myContainer.getTemperature())
  time.sleep(0.1)
