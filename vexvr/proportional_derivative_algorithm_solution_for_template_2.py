from math import *
from random import randint

def generateRandomPoint():
    xCoordinate = randint(-4,8)*100
    yCoordinate = randint(-4,8)*100
    return [xCoordinate,yCoordinate]

def proportionalDerivativeControlX(setpoint,duration):
    maxSpeed = 250
    k = 3
    kD = 1.5
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
    maxSpeed = 250
    k = 3
    kD = 1.5
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


def proportionalDerivativeControlUsingDistanceSensor(setpoint,duration):
    maxSpeed = 250
    k = 3
    kD = 1.5
    oldError = 0
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        currentXLocation = location.position(X,MM)
        error = (900-setpoint) - currentXLocation
        # 900-setpoint makes sure that the robot is actually 200mm from the right edge. 
        # Since the setpoint is 200, the robot will only until x = 200 not x = 700, which is the 200mm from the edge.
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
    # You should not change much in the code below. This code chooses a random point, puts the pen down,
    # and then calls the above functions to move to the point, turn to face the right wall, and then move the specified distance away.
    target = generateRandomPoint()
    brain.print("target location is x = ( " + str(target[0]) + " , " + str(target[1]) + " )" )
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    proportionalDerivativeControlX(target[0],4)
    drivetrain.turn_to_heading(0,DEGREES,wait=True)
    proportionalDerivativeControlY(target[1],4)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    proportionalDerivativeControlUsingDistanceSensor(200,5)
# VR threads — Do not delete
vr_thread(main())
