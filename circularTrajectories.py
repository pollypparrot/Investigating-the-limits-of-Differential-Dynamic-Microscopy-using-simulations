#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Circular Trajectories


import numpy as np

#start with only x and y- axis of rotation is z
def angularTrajectoryCoordinateGeneration(numSteps,frameRate,xFrameSize,yFrameSize,zCutOff,pixelSize,angularVelocity,distanceFromCentre):
    #calculate time period
    timePeriod = 1/frameRate
    
    #set starting location of sphere and parameters
    currentTime = 0                 #set to initial time of 0. 
    
    #initialise coordinate and time lists. Set starting point to that chosen above
    xCoords = [np.random.randint(0,xFrameSize)]
    yCoords = [np.random.randint(0,yFrameSize)]
    zCoords = [np.random.randint(-zCutOff,zCutOff)]
    time = [currentTime]

    #angle setup
    angleChangePerStep = angularVelocity*timePeriod
    startingAngel = np.random.uniform(0,2*np.pi)

    #calulate each position for each step
    for step in range (0,numSteps):

        #add time changes
        currentTime += timePeriod  #add the change in time to find the new time
        time.append(currentTime)   #add to time array
        
        #append changes
        xCoordsNew = xCoords[0] + distanceFromCentre*np.cos(startingAngel+step*angleChangePerStep)
        yCoordsNew = yCoords[0] + distanceFromCentre*np.sin(startingAngel+step*angleChangePerStep)
        zCoordsNew = zCoords[0] 
        
        #boundry conditions
        if (xCoordsNew>xFrameSize):
            xCoordsNew-=xFrameSize
        elif (xCoordsNew<0):
            xCoordsNew+=xFrameSize
            
        if (yCoordsNew>yFrameSize):
            yCoordsNew-=yFrameSize
        elif (yCoordsNew<0):
            yCoordsNew+=yFrameSize
        
        #check for z changes
        zUpperBoundryCheck = zCoordsNew//zCutOff
        zLowerBoundryCheck = -zCoordsNew//zCutOff
        if (zUpperBoundryCheck>0):
            zCoordsNew-=zCutOff*zUpperBoundryCheck
        elif(zLowerBoundryCheck>0):
            zCoordsNew+=zCutOff* zLowerBoundryCheck
                    
        xCoords.append(xCoordsNew)
        yCoords.append(yCoordsNew)
        zCoords.append(zCoordsNew)
    #return arrays of all coordinate functions
    return xCoords,yCoords,zCoords,time

