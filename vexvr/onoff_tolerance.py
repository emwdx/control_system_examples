# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode VR Python Project
# 
# ------------------------------------------

# Library imports
from vexcode import *


drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()


def driveControlOnOff(duration):
    setpoint = 0
    speed = 100
    # reset the timer
    brain.timer_reset()
    # begin algorithm to drive straight to the position of y = 0

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentYLocation = location.position(Y,MM)
        if( currentYLocation < setpoint):
            drivetrain.drive(FORWARD)
        elif (currentYLocation > setpoint):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)

def driveControlOnOffTolerance(duration):
    setpoint = 0
    speed = 100
    tolerance = 5
    # reset the timer
    brain.timer_reset()
    # begin algorithm to drive straight to the position of y = 0

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentYLocation = location.position(Y,MM)
        if( currentYLocation < setpoint - tolerance):
            drivetrain.drive(FORWARD)
        elif (currentYLocation > setpoint + tolerance):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)

# Add project code in "main"
def main():
    driveControlOnOffTolerance(5)
    drivetrain.turn_to_heading(90, DEGREES)


# VR threads — Do not delete
vr_thread(main())
