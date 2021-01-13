from random import uniform

'''
TemperatureController class - programmed by Evan Weinberg

See the README.TXT for instructions on using this library.

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>

'''
class TemperatureController:
  def __init__(self):
    self.__temperature = 28.0
    self.__heaterMaxPower = 100.0
    self.__coolerMaxPower = 55.0
    self.__heaterPower = 0
    self.__coolerPower = 0
    self.__environmentTemperature = 28.0
  def heaterOn(self,power):
    if(power > self.__heaterMaxPower):
      power = self.__heaterMaxPower
    elif (power < 0):
      power = self.__heaterMaxPower
    self.__heaterPower = power
  def heaterOff(self):
    self.__heaterPower = 0
  def coolerOn(self,power):
    if(power > self.__coolerMaxPower):
      power = self.__coolerMaxPower
    elif (power < 0):
      power = 0
    self.__coolerPower = power
  def coolerOff(self):
    self.__coolerPower = 0
  def update(self):
    k = uniform(.018,0.040)
    changeTemperature = k*(self.__heaterPower - self.__coolerPower - 0.28*(self.__temperature - self.__environmentTemperature))
    newTemperature = self.__temperature + changeTemperature
    if(newTemperature > 100.0):
      newTemperature = 100.0
    elif (newTemperature < 0):
      newTemperature = 0
    self.__temperature = newTemperature
  def getTemperature(self):
    return self.__temperature
  def heaterIsOn(self):
      return (self.__heaterPower > 0)
  def coolerIsOn(self):
      return (self.__coolerPower > 0)
