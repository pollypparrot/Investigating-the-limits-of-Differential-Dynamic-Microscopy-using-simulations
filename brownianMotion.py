#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Brownian motion
#15/12/23

import math  
import numpy  as np
import os
import matplotlib.pyplot as plt

#global constants
kb = 1.380649 * 10**(-23)        #Botlzmanns Constant. Unit of Joules per unit Kelvin.


#calculate the diffusion coefficient
def diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius):
    diffusionCoeff = (kb*temp)/(6*math.pi*fluidViscosity*sphereRadius) #unit of metres squared per second
    return diffusionCoeff



#create function for random walk simulator
def randomWalkCoordinateGeneration(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,fluidViscosity,sphereRadius,temp):
    
    #make place for images to be stored
    os.mkdir(directory)
    
    #initialise variables for simulation time
    #initilase pixel array   
    colourArray = np.zeros((xFrameSize,yFrameSize),dtype = float)
    
    #calculate time period
    timePeriod = 1/frameRate
     
    #initialise coordinate list, direction list, tumbling list and tumblingTime list
    coords = np.zeros((numParticles,3))
    #for each particle
    for index in range(0,numParticles):
        #setup initial positions
        coords[index][0]=np.random.randint(0,xFrameSize)
        coords[index][1]=np.random.randint(0,yFrameSize)
        coords[index][2]=np.random.randint(-zCutoffVolume,zCutoffVolume)
    
    #calculating the Diffusion Coefficient
    diffusionCoeff = diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius)   #unit of metres squared per second

    #initialising the parameters of the Gaussian distribution for position change
    #As it is the change in position, mean is 0
    mean = 0                      
    # Standard deviation calculated from the probability of movement function for brownian motion
    standardDeviation = math.sqrt(2*diffusionCoeff*timePeriod) 
    
    #for the number of frames that need to be generated
    for step in range(0,numSteps):  
        
        print(str(step),"/",str(numSteps))
        
        ##NewCoordinateGeneration##
        
        #then go particle by particle for that frame
        for particleIndex in range (0,numParticles):
        
            #calculate change for each coordinate
            changex = np.random.normal(mean,standardDeviation) *1/computerPixelSize
            changey = np.random.normal(mean,standardDeviation) *1/computerPixelSize  
            changez = np.random.normal(mean,standardDeviation) *1/computerPixelSize 
    
            #add change to previous coordinate
            newX = coords[particleIndex][0] + changex
            newY = coords[particleIndex][1] + changey
            newZ = coords[particleIndex][2] + changez
     
            #check boundaries
            newX = newX%xFrameSize
            newY = newY%yFrameSize        
            if (newZ>zCutoffVolume):
                newZ-=zCutoffVolume
            elif(newZ<-zCutoffVolume):
                newZ+=zCutoffVolume
        
            #append new coordinate
            coords[particleIndex][0] = newX
            coords[particleIndex][1] = newY
            coords[particleIndex][2] = newZ
            
            
        ##IMAGE GENERATION##
        
        #for each step the colour intensity array is reset to 0
        #this is what provides the final output
        colourArray.fill(0)  
                    
        #now the particles movement is updated we can add its intensity difference to colour array
        for particleIndex in range (0,numParticles):
            
            zCoordinate = coords[particleIndex][2]
            
            #if the particle is out of the z viewing range then it does not contribute to intensity
            if (zCoordinate>zCutoffView)or (zCoordinate<-zCutoffView):
                pass
            
            #otherwise it does contribute
            else:
                
                #get position on the grid
                xCoordinate = coords[particleIndex][0]
                yCoordinate = coords[particleIndex][1]
                
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
                        colourArray[x][y] += (1-(zCoordinate/zCutoffView)**2)*(255*math.exp(-((x-xCoordinate)**2+(y-yCoordinate)**2)/(2*particleSize**2)))
        
        #once all particle contributions are calculated
        
        #plot colours and save the file in images        
        plt.imshow(colourArray,cmap='gray',interpolation='none', vmin=0)
        plt.axis('off')
        filename = directory+f'/{step}.png'
        plt.savefig(filename)