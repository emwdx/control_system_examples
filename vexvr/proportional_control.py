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


def driveControlProportional(duration):
    setpoint = 0
    maxSpeed = 100
    k = 1
    # reset the timer
    brain.timer_reset()
    # begin algorithm to drive straight to the position of y = 0

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentYLocation = location.position(Y,MM)
        error = setpoint - currentYLocation
        output = k*error
        # Ensure the output is not more than the maximum speed
        if(output>maxSpeed):
            output = maxSpeed
        elif(output<-maxSpeed):
            output = -maxSpeed
        brain.print(output)
        brain.new_line()
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)
        # Set the direction of movement
        
        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()



# Add project code in "main"
def main():
    driveControlProportional(5)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)

# VR threads — Do not delete
vr_thread(main())
