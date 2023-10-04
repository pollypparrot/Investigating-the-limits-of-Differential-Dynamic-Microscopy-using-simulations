#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Random Walk
#27/09/23

import math  #for more complex math equations
import numpy  as np

from createGraphs import threeDimensionGraphPlot
from createGraphs import twoDimensionGraphPlot
from createGraphs import HistogramAndGaussLine


#global constants
kb = 1.380649 * 10**(-23)        #Botlzmanns Constant. Unit of Joules per unit Kelvin.


#calculate the diffusion coefficient
def diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius):
    diffusionCoeff = (kb*temp)/(6*math.pi*fluidViscosity*sphereRadius) #unit of metres squared per second
    return diffusionCoeff


#create function for random walk simulator
def randomWalkSimulator():
    
    #set starting location of sphere and parameters
    currentTime = 0                 #set to initial time of 0. Float
    currentX = 0                    #initial x position
    currentY = 0                    #initial y position
    currentZ = 0                    #initial z position
    
    #initialise coordinate and time lists. Set starting point to that chosen above
    xCoords = [currentX]
    yCoords = [currentY]
    zCoords = [currentZ]
    time = [currentTime]
   
    #initalise known variables
    fluidViscosity = 10**(-3)        #unit of Pascal seconds
    sphereRadius = 0.5 * 10**(-6)    #unit of metres
    temp = 300                       #unit of Kelvin
    frameRate = 100                  #unit of Hertz
    timePeriod = 1/frameRate         #unit of Time
    
    #calculating the Diffusion Coefficient
    diffusionCoeff = diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius)   #unit of metres squared per second

    #initialising the parameters of the Gaussian distribution
    mean = 0                        #as we can equally go in any direction from the current position
    standardDeviation = math.sqrt(diffusionCoeff*timePeriod) # taken from the probability of movement function for brownian motion
    
    #set 
    numSteps = 100000                 #change for a longer/shorter analysis
    changesTracker = [] # used to keep track of the numbers generated from the number generator to then be plotted on a histogram with the gaussian curve
    
    #calulate each position for each step
    for step in range (0,numSteps):
        currentTime += timePeriod  #add the change in time to find the new time
        time.append(currentTime)   #add to time array
        
        #calculate the change for each coordinate
        xchange = np.random.normal(mean,standardDeviation) 
        ychange = np.random.normal(mean,standardDeviation)
        zchange = np.random.normal(mean,standardDeviation)
        
        #update the current position of the sphere
        currentX += xchange
        currentY += ychange
        currentZ += zchange
        
        #add current position to the arrays
        xCoords.append(currentX)
        yCoords.append(currentY)
        zCoords.append(currentZ)

        #check gaussian changes
        changesTracker.append(xchange)
    
    #plot histogram to check changes    
    HistogramAndGaussLine(mean,standardDeviation,changesTracker)
    
    #return arrays of all coordinate functions
    return xCoords,yCoords,zCoords,time

xCoords,yCoords,zCoords,time = randomWalkSimulator()
twoDimensionGraphPlot(xCoords,yCoords,"X axis","Y axis")
twoDimensionGraphPlot(xCoords,zCoords,"X axis","Z axis")
twoDimensionGraphPlot(yCoords,zCoords,"Y axis","Z axis")
twoDimensionGraphPlot(time,xCoords,"Time","X axis")
twoDimensionGraphPlot(time,yCoords,"Time","Y axis")
twoDimensionGraphPlot(time,zCoords,"Time","Z axis")
threeDimensionGraphPlot(xCoords,yCoords,zCoords,"X axis","Y Axis","Z Axis","Brownian Motion")