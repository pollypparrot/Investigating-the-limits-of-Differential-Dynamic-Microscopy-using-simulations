#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Run and tumble walk

import math
import numpy as np

#pick three random directions
def randomDirection():
    #random number choice
    xDirection = np.random.randint(-10,10) # set x and y larger so larger velocity at that point to watch
    yDirection = np.random.randint(-10,10)
    zDirection = np.random.randint(-10,10)
    #find normalisation factor
    normalisationFactor = 1/np.sqrt(xDirection**2+yDirection**2+zDirection**2)
    #unit directions
    xDirection=xDirection*normalisationFactor
    yDirection=yDirection*normalisationFactor
    zDirection=zDirection*normalisationFactor
    #return values
    return xDirection,yDirection,zDirection

#Change by a set degree
#takes input of the xyz normalised unit direction and the angle that the change is to be in
#returns new unit direction
def setAngleChangeDirection(initialX,initialY,initialZ,tumbleAngle):
    tumbleAngle = tumbleAngle*np.pi/180
    r = np.sqrt(initialX**2+initialY**2+initialZ**2)
    phi = math.atan2(initialY,initialX)
    theta = np.arccos(initialZ/r)
    psi = np.random.randint(0,2*np.pi)
    matrixstartingVector = [0,0,1]
    matrixRotateBySetAmount_Y = [
                                [np.cos(tumbleAngle),0,np.sin(tumbleAngle)],
                                [0,1,0],
                                [-np.sin(tumbleAngle),0,np.cos(tumbleAngle)]
                                ]
    matrixRotateRandom_Z = [
                            [np.cos(psi),-np.sin(psi),0],
                            [np.sin(psi),np.cos(psi),0],
                            [0,0,1]
                            ]
    matrixRotateTheta_Y = [
                            [np.cos(theta),0,np.sin(theta)],
                            [0,1,0],
                            [-np.sin(theta),0,np.cos(theta)]
                            ]
    matrixRotatePhi_Z = [
                        [np.cos(phi),-np.sin(phi),0],
                        [np.sin(phi),np.cos(phi),0],
                        [0,0,1]
                        ]
    
    finalVector = np.matmul(matrixRotatePhi_Z,np.matmul(matrixRotateTheta_Y,np.matmul(matrixRotateRandom_Z,np.matmul(matrixRotateBySetAmount_Y,matrixstartingVector))))
    initialVector = [initialX,initialY,initialZ]    
    return finalVector[0], finalVector[1], finalVector[2]

    
#calculates run and tumble coordinates
def runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutOff,pixelSize,runVelocity,probTumble,tumbleTime,tumbleAngle):
    
    #calculate time period
    timePeriod = 1/frameRate
    
    #set starting location of sphere and parameters
    currentTime = 0                 #set to initial time of 0. 
    
    #initialise coordinate and time lists. Set starting point to that chosen above
    xCoords = [np.random.randint(0,xFrameSize)]
    yCoords = [np.random.randint(0,yFrameSize)]
    zCoords = [np.random.randint(-zCutOff,zCutOff)]
    time = [currentTime]

    #start with tumble not occuring
    tumbleOccuring = False
    xDirection,yDirection,zDirection = randomDirection()

    
    #calulate each position for each step
    for step in range (0,numSteps):

        #check if tumble occuring
        if tumbleOccuring:
            #if it is then we add to time
            tumblingTimeTracker +=timePeriod
            #let this rounds coordinates stay the same
            xCoordsNew = xCoords[step]
            yCoordsNew = yCoords[step]
            zCoordsNew = zCoords[step]
            #check if the tumbling will now stop
            if tumblingTimeTracker>tumbleTime:
                tumbleOccuring=False
        
        #if we arent already tumbling
        else:
            #generate a random number and check if it is less than likelyhood
            thisTurnTumble = np.random.uniform(0,1)
            if thisTurnTumble<probTumble:
                #if less than liklihood then tumbling is now occuring
                tumbleOccuring=True
                #resent the time tracker for the time period of this round
                tumblingTimeTracker = timePeriod
                #set the coordinates to be the same
                xCoordsNew = xCoords[step]
                yCoordsNew = yCoords[step]
                zCoordsNew = zCoords[step]
                #generate the new direction post tumble
                xDirection,yDirection,zDirection = setAngleChangeDirection(xDirection,yDirection,zDirection,tumbleAngle)
            else:
                #then we arent tumbling- we are moving!
                xCoordsNew = xCoords[step] + timePeriod*runVelocity*xDirection*1/pixelSize
                yCoordsNew = yCoords[step] + timePeriod*runVelocity*yDirection*1/pixelSize
                zCoordsNew = zCoords[step] + timePeriod*runVelocity*zDirection*1/pixelSize
            
        #add time changes
        currentTime += timePeriod  #add the change in time to find the new time
        time.append(currentTime)   #add to time array
        
        #check boundry condition of   --- kept outside at the moment in case drift velocity will be added
        #x
        if (xCoordsNew>=xFrameSize):
            xCoordsNew-=xFrameSize
        elif (xCoordsNew<0):
            xCoordsNew+=xFrameSize
        #y  
        if (yCoordsNew>=yFrameSize):
            yCoordsNew-=yFrameSize
        elif (yCoordsNew<0):
            yCoordsNew+=yFrameSize
        #z
        zUpperBoundryCheck = zCoordsNew//zCutOff
        zLowerBoundryCheck = -zCoordsNew//zCutOff
        if (zUpperBoundryCheck>0):
            zCoordsNew-=zCutOff*zUpperBoundryCheck
        elif(zLowerBoundryCheck>0):
            zCoordsNew+=zCutOff* zLowerBoundryCheck
        
        #append these new coordinates
        xCoords.append(xCoordsNew)
        yCoords.append(yCoordsNew)
        zCoords.append(zCoordsNew)
    
    #return arrays of all coordinate functions
    return xCoords,yCoords,zCoords,time

