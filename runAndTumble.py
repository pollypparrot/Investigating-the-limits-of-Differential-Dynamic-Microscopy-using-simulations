#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Run and tumble walk

import math
import numpy as np

#pick three random directions
def randomDirection():
    #random number choice
    xDirection = np.random.randint(0,5)
    yDirection = np.random.randint(0,5)
    zDirection = np.random.randint(0,5)
    #find normalisation factor
    normalisationFactor = 1/np.sqrt(xDirection**2+yDirection**2+zDirection**2)
    #unit directions
    xDirection=xDirection*normalisationFactor
    yDirection=yDirection*normalisationFactor
    zDirection=zDirection*normalisationFactor
    #return values
    return xDirection,yDirection,zDirection

def randomandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,pixelSize,runTime,runVelocity,tumbleTime):
    
    #calculate time period
    timePeriod = 1/frameRate
    
    #set starting location of sphere and parameters
    currentTime = 0                 #set to initial time of 0. 
    currentZ = 0                   #initial z position
    
    #initialise coordinate and time lists. Set starting point to that chosen above
    #xCoords = [np.random.randint(0,xFrameSize)]
    #yCoords = [np.random.randint(0,yFrameSize)]
    xCoords = [20]
    yCoords = [10]
    zCoords = [currentZ]
    time = [currentTime]
    
    #calculate the number of runs expected and a counter to track changes
    runCounter = 0
    #calulate each position for each step
    for step in range (0,numSteps):
        
        #calculate next run time
        nextRunTime = runTime*runCounter
        
        #if it is equal then we change direction
        if (step*timePeriod ==nextRunTime):
            runCounter+=1
            xDirection,yDirection,zDirection = randomDirection()
            print(xDirection,yDirection,zDirection)

        #add time changes
        currentTime += timePeriod  #add the change in time to find the new time
        time.append(currentTime)   #add to time array
        
        #append changes
        xCoordsNew = xCoords[step] + timePeriod*runVelocity*xDirection*1/pixelSize
        yCoordsNew = yCoords[step] + timePeriod*runVelocity*yDirection*1/pixelSize
        zCoordsNew = zCoords[step] + timePeriod*runVelocity*zDirection*1/pixelSize
        
        if (xCoordsNew>xFrameSize):
            xCoordsNew-=xFrameSize
        elif (xCoordsNew<0):
            xCoordsNew+=xFrameSize
            
        if (yCoordsNew>yFrameSize):
            yCoordsNew-=yFrameSize
        elif (yCoordsNew<0):
            yCoordsNew+=yFrameSize
                
        xCoords.append(xCoordsNew)
        yCoords.append(yCoordsNew)
        zCoords.append(zCoordsNew)
    #return arrays of all coordinate functions
    return xCoords,yCoords,zCoords,time

