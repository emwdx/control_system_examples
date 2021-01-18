from math import *
from random import randint

def driveXDistance(setpoint,duration):
    drivetrain.set_drive_velocity(70, PERCENT)
    tolerance = 5
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currentXLocation = location.position(X,MM)
        if( currentXLocation < setpoint - tolerance):
            drivetrain.drive(FORWARD)
        elif (currentXLocation > setpoint + tolerance):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def driveYDistance(setpoint,duration):
    drivetrain.set_drive_velocity(70, PERCENT)    
    tolerance = 5
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currentYLocation = location.position(Y,MM)
        if( currentYLocation < setpoint - tolerance):
            drivetrain.drive(FORWARD)
        elif (currentYLocation > setpoint + tolerance):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()


def driveDiagonalDistance(setpoint,duration):
    drivetrain.set_drive_velocity(70, PERCENT)
    tolerance = 5
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        currentYLocation = location.position(Y,MM)
        if( currentYLocation < setpoint - tolerance):
            drivetrain.drive(FORWARD)
        elif (currentYLocation > setpoint + tolerance):
            drivetrain.drive(REVERSE)
        else:
            drivetrain.stop()

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

# Add project code in "main"
def main():
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveXDistance(0,3)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(0,3)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    driveDiagonalDistance(400,4)
# VR threads — Do not delete
vr_thread(main())
