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
def randomWalkCoordinateGeneration(numSteps,fluidViscosity,sphereRadius,temp,frameRate,xFrameSize,yFrameSize,zCutOff,pixelSize):
    
    #set starting location of sphere and parameters
    currentTime = 0                 #set to initial time of 0. Float                  #initial y position
    
    #initialise coordinate and time lists. Set starting point to that chosen above
    xCoords = [np.random.randint(0,xFrameSize) ]
    yCoords = [np.random.randint(0,yFrameSize) ]
    zCoords = [np.random.randint(-zCutOff,zCutOff)]
    time = [currentTime]
   
    timePeriod = 1/frameRate         #unit of seconds
    
    #calculating the Diffusion Coefficient
    diffusionCoeff = diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius)   #unit of metres squared per second

    #initialising the parameters of the Gaussian distribution
    mean = 0                        #as we can equally go in any direction from the current position
    standardDeviation = math.sqrt(2*diffusionCoeff*timePeriod) # taken from the probability of movement function for brownian motion
    
    #changesTracker = [] # used to keep track of the numbers generated from the number generator to then be plotted on a histogram with the gaussian curve
    #commented out as no longer needed to check data
    
    coordinates = [xCoords,yCoords]
    boundries = [xFrameSize,yFrameSize]
    
    for step in range(0,numSteps):  
        #calculate change for each coordinate
        changex = np.random.normal(mean,standardDeviation) *1/pixelSize
        changey = np.random.normal(mean,standardDeviation) *1/pixelSize  
        changez = np.random.normal(mean,standardDeviation) *1/pixelSize 
    
        #add change to previous coordinate
        newX = xCoords[step] + changex
        newY = yCoords[step] + changey
        newZ = zCoords[step] + changez
     
        #check boundaries
        newX = newX%xFrameSize
        newY = newY%yFrameSize        
        if (newZ>zCutOff):
            newZ-=zCutOff
        elif(newZ<-zCutOff):
            newZ+=zCutOff
        
        #append new coordinate
        xCoords.append(newX)
        yCoords.append(newY)
        zCoords.append(newZ)
    #check gaussian changes
    #changesTracker.append(xchange)
    
    #plot histogram to check changes    
    #HistogramAndGaussLine(mean,standardDeviation,changesTracker)
    
    #return arrays of all coordinate functions
    return xCoords,yCoords,zCoords,time

