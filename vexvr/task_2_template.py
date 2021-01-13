from math import *
from random import randint
xCoordinate = randint(-4,8)*100
yCoordinate = randint(-4,8)*100
maxvel = 100
def generateRandomPoint():
    return [xCoordinate,yCoordinate]

def driveXDistance(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        error = xCoordinate - location.position(X,MM)
        k = 1.5
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
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        error = yCoordinate - location.position(Y,MM)
        k = 1.5
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


def driveUsingDistanceSensor(setpoint,duration):
    # reset the timer
    brain.timer_reset()

    # loop while the timer is less than the duration input of the function.
    while(brain.timer_time(SECONDS)<duration):
        # Your code goes here!
        error = distance.get_distance(MM) - setpoint
        k=1.5
        drivespeed = k*error
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
    # You should not change much in the code below. This code chooses a random point, puts the pen down,
    # and then calls the above functions to move to the point, turn to face the right wall, and then move the specified distance away.
    target = generateRandomPoint()
    brain.print("target location is x = ( " + str(target[0]) + " , " + str(target[1]) + " )" )
    pen.move(DOWN)
    drivetrain.turn_to_heading(90,DEGREES,wait=True)
    #driveXDistance(target[0],4)
    #drivetrain.turn_to_heading(0,DEGREES,wait=True)
    #driveYDistance(target[1],4)
    #drivetrain.turn_to_heading(90,DEGREES,wait=True)
    driveUsingDistanceSensor(200,5)
# VR threads — Do not delete
vr_thread(main())

