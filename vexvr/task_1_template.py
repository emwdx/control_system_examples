from math import *
from random import randint

def driveXDistance(setpoint,duration):
    maxSpeed = 100
    k = 1
    brain.timer_reset()

    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        error = setpoint - currentXLocation
        output = k*error
        if(output>maxSpeed):
            output = maxSpeed
        elif(output<-maxSpeed):
            output = -maxSpeed
        brain.print(output)
        brain.new_line()
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)
        # Set the direction of movement
           
        wait(1,MSEC)
    drivetrain.stop()

    
    
def driveYDistance(setpoint,duration):
    maxSpeed = 100
    k = 1
    brain.timer_reset()

    while(brain.timer_time(SECONDS)<duration):
        currentYLocation = location.position(Y,MM)
        error = setpoint - currentYLocation
        output = k*error
        if(output>maxSpeed):
            output = maxSpeed
        elif(output<-maxSpeed):
            output = -maxSpeed
        brain.print(output)
        brain.new_line()
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)
        # Set the direction of movement

        wait(1,MSEC)
    drivetrain.stop()


    
    
def driveDiagDistance(setpoint,duration):
    maxSpeed = 100
    k = 1
    brain.timer_reset()

    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        error = setpoint - currentXLocation
        output = k*error
        if(output>maxSpeed):
            output = maxSpeed
        elif(output<-maxSpeed):
            output = -maxSpeed
        brain.print(output)
        brain.new_line()
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)

        currentYLocation = location.position(Y,MM)
        error = setpoint - currentYLocation
        output = k*error
        if(output>maxSpeed):
            output = maxSpeed
        elif(output<-maxSpeed):
            output = -maxSpeed
        brain.print(output)
        brain.new_line()
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)
   
        wait(1,MSEC)
    drivetrain.stop()


def main():
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveXDistance(0,3)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    driveYDistance(0,3)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    driveDiagDistance(400,4)

vr_thread(main())
