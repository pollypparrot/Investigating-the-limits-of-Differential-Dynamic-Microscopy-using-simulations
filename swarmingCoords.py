#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Generate Swarming Coords

import numpy as np
import math

def swarmingCoordGeneration(numSteps,timePeriod,xFrameSize,yFrameSize,runVelocity,numParticles,computerPixelSize,flockingRadius,maxNoiseLevel):
    #set up arrays to store information
    
    #direction array stores each particles directions where the index defines which particle it is describing
    directionArray = np.empty((2,numParticles))
    
    #store all the coords for the pixels
    pixelCoords = np.empty((numParticles,2,numSteps))
    
    #store current positions
    currentPositions = np.empty((xFrameSize,yFrameSize))
    for x in range (0,xFrameSize):
        for y in range(0,yFrameSize):
            currentPositions[x][y] = -1
    
    #set starting location of sphere and parameters
    currentTime = 0                 #set to initial time of 0. 
    
    time = [currentTime] 
    
    print("setting up system")
    #set up all initial directions and locations
    for setup in range(0,numParticles):
        #assign each particle a random angle for direction
        angleDirection = np.random.uniform(0,2*np.pi)
        directionArray[0][setup] = angleDirection
        #generate starting positions
        #until they have their own spot:
        foundSpot = False
        while not foundSpot:
            #generate location
            startingX = np.random.randint(0,xFrameSize)
            startingY = np.random.randint(0,yFrameSize)
            #check if it is occupied
            if currentPositions[startingX][startingY] == -1 :
                #if it isnt this is the new position
                pixelCoords[setup][0][0] = startingX
                pixelCoords[setup][1][0] = startingY
                currentPositions[startingX][startingY] = setup
                foundSpot = True
            else:
                #if it is occupied regenerate positions
                pass
    #need old and new to ensure that particles velocities are changed in bulk and arent based on changes already occured.
    oldDirections = 0
    newDirections = 1
    print("Starting coordinate generation")    
    for step in range (1,numSteps):
        #add new time
        currentTime +=timePeriod
        time.append(currentTime)
        
        #calculate new positions
        for particle in range(0,numParticles):
            #find old position
            oldX = pixelCoords[particle][0][step-1]
            oldY = pixelCoords[particle][1][step-1]

            
            #find any particles within the boundary and add their angles
            sinTotFlocking = 0
            cosTotFlocking = 0
            
            #for each particle
            for item in range(0,numParticles):
                #calcualte the distance between particles
                itemX = pixelCoords[item][0][step-1]
                itemY = pixelCoords[item][1][step-1]

                distance = np.sqrt((itemX-oldX)**2+(itemY-oldY)**2)
                #check if they are close enough to influence
                if distance<=flockingRadius:
                    angle = directionArray[oldDirections][item]
                    sinTotFlocking +=np.sin(angle)
                    cosTotFlocking+=np.cos(angle)
            
            #calculate new direction based on average and noise
            newAngle = math.atan2(sinTotFlocking,cosTotFlocking) + timePeriod*np.random.uniform(-1,1)*maxNoiseLevel
            directionArray[newDirections][particle] = newAngle
            
            #find new velocity with new running direction
            velocityX = runVelocity*np.cos(newAngle)*1/computerPixelSize
            velocityY = runVelocity*np.sin(newAngle)*1/computerPixelSize
            #calculate new position with boundary conditions
            newX = (velocityX*timePeriod+oldX) % xFrameSize
            newY = (velocityY*timePeriod+oldY) % yFrameSize
            
            
            checkX =round(newX) %xFrameSize
            checkY = round(newY) % yFrameSize
            #if the position is available
            if (currentPositions[checkX][checkY] ==-1) or (currentPositions[checkX][checkY] == particle):
                #append new position
                pixelCoords[particle][0][step]= newX
                pixelCoords[particle][1][step]= newY
                
                #change tracker
                currentPositions[checkX][checkY] = particle
                currentPositions[round(oldX)%xFrameSize][round(oldY)%yFrameSize] = -1

            else:
                #position isnt available
                #stays still
                pixelCoords[particle][0][step]= oldX
                pixelCoords[particle][1][step]= oldY
        #at end of step we need to change which direction array is the old one
        temporary = oldDirections
        oldDirections = newDirections
        newDirections = temporary
    return pixelCoords

