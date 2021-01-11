# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode VR Python Project
# 
# ------------------------------------------

from math import *
from random import randint



def driveXDistance(setpoint,duration):
    setpoint = 0
    maxvel = 100
    
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        error = setpoint-location.position(X,MM)
        k=1.5
        drivespeed = error*k
        if(drivespeed>maxvel):
            drivespeed = maxvel
        elif(drivespeed<-maxvel):
            drivespeed = -maxvel
        drivetrain.set_drive_velocity(drivespeed, PERCENT)
        brain.print(drivespeed)
        brain.new_line()
        drivetrain.drive(FORWARD)

        

        

        

        









        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def driveYDistance(setpoint,duration):
    setpoint = 0
    maxvel = 100
    
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        error = setpoint-location.position(Y,MM)
        k=1.5
        drivespeed = error*k
        if(drivespeed>maxvel):
            drivespeed = maxvel
        elif(drivespeed<-maxvel):
            drivespeed = -maxvel
        drivetrain.set_drive_velocity(drivespeed, PERCENT)
        brain.print(drivespeed)
        brain.new_line()
        drivetrain.drive(FORWARD)




        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()


def driveDiagonalDistance(setpoint,duration):
    setpoint=400
    maxvel=100
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        error = setpoint-location.position(Y,MM)
        k=1.5
        drivespeed = error*k
        if(drivespeed>maxvel):
            drivespeed = maxvel
        elif(drivespeed<-maxvel):
            drivespeed = -maxvel
        drivetrain.set_drive_velocity(drivespeed, PERCENT)
        brain.print(drivespeed)
        brain.new_line()
        drivetrain.drive(FORWARD)
       









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
