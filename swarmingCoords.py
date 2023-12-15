#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Generate Swarming Coords

import numpy as np
import math
import matplotlib.pyplot as plt

def swarmingResponseNumberOfFrames(timePeriod,delayedResponseTime):
    noFrames = round(delayedResponseTime/timePeriod)
    return noFrames+2


def swarmingCoordGeneration(numSteps,frameRate,xFrameSize,yFrameSize,computerPixelSize,numParticles,particleSize,directory,runVelocity,flockingRadius,maxNoiseLevel,delayedResponseTime):
    
    #initialise variables for simulation time
    #initilase pixel array   
    colourArray = np.zeros((xFrameSize,yFrameSize),dtype = float)
    
    #calculate time period
    timePeriod = 1/frameRate
     
    #calculate how many frames it takes to repond:
    numFramesDelayNeeded = swarmingResponseNumberOfFrames(timePeriod,delayedResponseTime) 
     
    #initialise coordinate list, direction list, tumbling list and tumblingTime list
    coords = np.zeros((numParticles,2,2))
    
    #direction array stores each particles directions where the index defines which particle it is describing and what delay it is on
    directions = np.zeros((numParticles,numFramesDelayNeeded))

    #store current positions so they do not sit on top of each other
    currentPositions = np.empty((xFrameSize,yFrameSize))
    for x in range (0,xFrameSize):
        for y in range(0,yFrameSize):
            currentPositions[x][y] = -1

    #set up all initial directions and locations
    for setup in range(0,numParticles):
        
        #assign each particle a random angle for direction
        angleDirection = np.random.uniform(0,2*np.pi)
        #setup all directions to starting values
        for direction in range(0,numFramesDelayNeeded):
            directions[setup][direction] = angleDirection
            
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
                coords[setup][0][0] = startingX
                coords[setup][0][1] = startingY
                currentPositions[startingX][startingY] = setup
                foundSpot = True
            else:
                #if it is occupied regenerate positions
                pass
            
    #need old and new to ensure that particles velocities are changed in bulk and arent based on changes already occured.
    oldDirections = 0
    newDirections = numFramesDelayNeeded-1
    oldCoords = 0
    newCoords = 1

    
    for step in range (1,numSteps):

        print(str(step),"/",str(numSteps))


        #calculate new positions
        
        for particle in range(0,numParticles):
            #find old position
            oldX = coords[particle][oldCoords][0]
            oldY = coords[particle][oldCoords][1]
            
            #find any particles within the boundary and add their angles
            sinTotFlocking = 0
            cosTotFlocking = 0
            
            #for each particle
            for item in range(0,numParticles):
                #calcualte the distance between particles
                itemX = coords[item][oldCoords][0]
                itemY = coords[item][oldCoords][1]

                distance = np.sqrt((itemX-oldX)**2+(itemY-oldY)**2)
                #check if they are close enough to influence
                if distance<=flockingRadius:
                    angle = directions[item][oldDirections]
                    sinTotFlocking +=np.sin(angle)
                    cosTotFlocking+=np.cos(angle)
            
            #calculate new direction based on average and noise
            newAngle = math.atan2(sinTotFlocking,cosTotFlocking) + timePeriod*np.random.uniform(-1,1)*maxNoiseLevel
            directions[particle][newDirections] = newAngle
            
            #find new velocity with new running direction
            velocityX = runVelocity*np.cos(newAngle)*1/computerPixelSize
            velocityY = runVelocity*np.sin(newAngle)*1/computerPixelSize
            #calculate new position with boundary conditions
            newX = (velocityX*timePeriod+oldX) % xFrameSize
            newY = (velocityY*timePeriod+oldY) % yFrameSize
            
            
            checkX = round(newX) %xFrameSize
            checkY = round(newY) % yFrameSize
            #if the position is available
            if (currentPositions[checkX][checkY] ==-1) or (currentPositions[checkX][checkY] == particle):
                #append new position
                coords[particle][newCoords][0]= newX
                coords[particle][newCoords][1]= newY
                
                #change tracker
                currentPositions[checkX][checkY] = particle
                currentPositions[round(oldX)%xFrameSize][round(oldY)%yFrameSize] = -1

            else:
                #position isnt available
                #stays still
                coords[particle][newCoords][0]= oldX
                coords[particle][newCoords][1]= oldY
        #at end of step we need to change which direction array is the old one and new location
        oldDirections = (oldDirections + 1) % (numFramesDelayNeeded)
        newDirections = (newDirections + 1) % (numFramesDelayNeeded)
        
        
        ##IMAGE GENERATION##
        
        #for each step the colour intensity array is reset to 0
        #this is what provides the final output
        colourArray.fill(0)  
                    
        #now the particles movement is updated we can add its intensity difference to colour array
        for particleIndex in range (0,numParticles):

            #get position on the grid
            xCoordinate = coords[particleIndex][newCoords][0]
            yCoordinate = coords[particleIndex][newCoords][1]
                
            #size of particle based on Z frame needs to be calculated HERE
            
            #calculate a box around the GAUSSIAN splodge as all relevant informaion is within it
            #standard deviation is the apparent particle size
            subtraction = 3*particleSize
                
            #find box boundaries that intensity will be calculated within
            #math.ceiling makes sure to always round up
            xStart = math.ceil(xCoordinate -subtraction)
            yStart = math.ceil(yCoordinate -subtraction)
            RangeChecked = math.ceil(6*particleSize+1)
                
            #for the box around the particle (~99% data)
            for x in range (xStart,xStart+RangeChecked):
                for y in range(yStart,yStart+RangeChecked):
                        
                    x = x%xFrameSize
                    y = y%yFrameSize
                        
                    #add in the change of colour for the splodge at that point
                    colourArray[x][y] += (255*math.exp(-((x-xCoordinate)**2+(y-yCoordinate)**2)/(2*particleSize**2)))
        
        #once all particle contributions are calculated
        
        #plot colours and save the file in images        
        plt.imshow(colourArray,cmap='gray',interpolation='none', vmin=0)
        plt.axis('off')
        filename = directory+f'/{step}.png'
        plt.savefig(filename)
        
        
        #also need to change old and new coordinates
        oldCoords = (oldCoords+1)%2
        newCoords = (newCoords+1)%2


