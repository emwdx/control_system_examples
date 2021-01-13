from math import *
from random import randint


def proportionalDerivativeControlX(setpoint,duration):
    maxSpeed = 100
    k = 3
    kD = 3
    oldError = 0

    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        error = setpoint - currentXLocation
        changeError = error - oldError
        output = k*error - kD*changeError
        oldError = error
        # Ensure the output is not more than the maximum speed
        if(output > maxSpeed):
            output = maxSpeed
        elif(output < -maxSpeed):
            output = -maxSpeed
        brain.print(output)
        brain.new_line()
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)
        # Set the direction of movement

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def proportionalDerivativeControlY(setpoint,duration):
    maxSpeed = 100
    k = 3
    kD = 3
    oldError = 0

    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentYLocation = location.position(Y,MM)
        error = setpoint - currentYLocation
        changeError = error - oldError
        output = k*error - kD*changeError
        oldError = error
        # Ensure the output is not more than the maximum speed
        if(output > maxSpeed):
            output = maxSpeed
        elif(output < -maxSpeed):
            output = -maxSpeed
        brain.print(output)
        brain.new_line()
        drivetrain.drive(FORWARD)
        drivetrain.set_drive_velocity(output,PERCENT)
        # Set the direction of movement

        #VEXCode VR requires that we have a small pause in any loop we run.    
        wait(1,MSEC)
    drivetrain.stop()

def proportionalDerivativeControlDiagonal(setpoint,duration):
    maxSpeed = 100
    k = 3
    kD = 3
    oldError = 0

    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        error = setpoint - currentXLocation
        changeError = error - oldError
        output = k*error - kD*changeError
        oldError = error
        # Ensure the output is not more than the maximum speed
        if(output > maxSpeed):
            output = maxSpeed
        elif(output < -maxSpeed):
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
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    proportionalDerivativeControlX(0,3)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    proportionalDerivativeControlY(0,3)
    drivetrain.turn_to_heading(45,DEGREES,wait=True)
    proportionalDerivativeControlDiagonal(400,3)
# VR threads — Do not delete
vr_thread(main())
