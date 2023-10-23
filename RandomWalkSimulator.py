#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Random Walk
#27/09/23

import math  #for more complex math equations
import numpy  as np

#from createGraphs import HistogramAndGaussLine


#global constants
kb = 1.380649 * 10**(-23)        #Botlzmanns Constant. Unit of Joules per unit Kelvin.


#calculate the diffusion coefficient
def diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius):
    diffusionCoeff = (kb*temp)/(6*math.pi*fluidViscosity*sphereRadius) #unit of metres squared per second
    return diffusionCoeff


#create function for random walk simulator
def randomWalkCoordinateGeneration(numSteps,fluidViscosity,sphereRadius,temp,frameRate,xFrameSize,yFrameSize,pixelSize):
    
    #set starting location of sphere and parameters
    currentTime = 0                 #set to initial time of 0. Float                  #initial y position
    currentZ = 0                  #initial z position
    
    #initialise coordinate and time lists. Set starting point to that chosen above
    xCoords = [np.random.randint(0,xFrameSize) ]
    yCoords = [np.random.randint(0,yFrameSize) ]
    zCoords = [currentZ]
    time = [currentTime]
   
    timePeriod = 1/frameRate         #unit of seconds
    
    #calculating the Diffusion Coefficient
    diffusionCoeff = diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius)   #unit of metres squared per second

    #initialising the parameters of the Gaussian distribution
    mean = 0                        #as we can equally go in any direction from the current position
    standardDeviation = math.sqrt(2*diffusionCoeff*timePeriod) # taken from the probability of movement function for brownian motion
    
    #set 
    numSteps = numSteps                 #change for a longer/shorter analysis
    
    
    #changesTracker = [] # used to keep track of the numbers generated from the number generator to then be plotted on a histogram with the gaussian curve
    #commented out as no longer needed to check data
    
    coordinates = [xCoords,yCoords]
    boundries = [xFrameSize,yFrameSize]
    
    #calulate each position for each step
    for step in range (0,numSteps):
        currentTime += timePeriod  #add the change in time to find the new time
        time.append(currentTime)   #add to time array
        
        for coordNumber in range(0,2):
            #calculate change for each coordinate
            change = np.random.normal(mean,standardDeviation) *1/pixelSize 
            #coordinate
            coordinateCurrent = coordinates[coordNumber]
            
            #find the new coordinate by adding the previous change
            newCoordinate = coordinateCurrent[step] + change
            #check the boundry condition
            boundry = boundries[coordNumber]
            #if it is greater than boundry then it s off the screen, remove boundry to wrap around
            if newCoordinate > boundry:
                newCoordinate -= boundry
            #if it is less than zero it is off the screen, add the boundry to wrap around
            elif newCoordinate<0:
                newCoordinate+=boundry  
            #append the new coordinate
            coordinates[coordNumber].append(newCoordinate)
            
        
        #check gaussian changes
        #changesTracker.append(xchange)
    
    #plot histogram to check changes    
    #HistogramAndGaussLine(mean,standardDeviation,changesTracker)
    
    #return arrays of all coordinate functions
    return xCoords,yCoords,zCoords,time

