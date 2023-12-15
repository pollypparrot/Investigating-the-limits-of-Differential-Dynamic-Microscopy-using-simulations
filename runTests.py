#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Test Data from here


import textFiles
import math
import circularTrajectories
import swarmingCoords
import numpy as np
import os
import runAndTumble
import brownianMotion

#initalise known variables about system
fluidViscosity = 1.380649e-23       #unit of Pascal seconds
sphereRadius = 1 * 10**(-6)    #unit of metres
temp = 1.884955592153876e-14                      #unit of Kelvin

#initialise variables for the camera
frameRate = 100                  #unit of Hertz
timePeriod = 1/frameRate
xFrameSize = 512 #in no.pixels
yFrameSize = 512 #in no. pixels
zFrameSize = 512     
zViewSize = 400
zCutoffVolume = zFrameSize/2 #constant. Div 1 to get lowest integer number
zCutoffView = zViewSize/2
computerPixelSize = 1e-6 #in m

#initialise general particle variables
particleSize = sphereRadius*2/computerPixelSize  #diameter in pixel size
numParticles = 100
runVelocity = 50e-6 # in m/s  doesnt apply fr brownian motion


#initialise run and tumble variables
avgRunTime = 1 #in seconds
tumbleTime = 0.1 #in seconds
tumbleAngle = 60
probTumble = 1/(frameRate*avgRunTime)

#initialise circularTrajectories variables
angularVelocity = 15e-6 #in m/s
distanceFromCentre = 25
pClockwise= 0.7

#initialise swarming variables
flockingRadius = 5
maxNoiseLevel = np.pi/2 #number from 0-pi
delayedResponseTime=0.05

#decideing length of data
videoLength = 10 #in seconds

#videoLength*frameRate must be integer for code to work.
numSteps = int(videoLength*frameRate)


number = textFiles.readInFileOneDataFilename('images/simulationNumber.txt')
directory = 'images/simulation_' + number
#make place for images to be stored
os.mkdir(directory)
textFiles.createFileOneDataFilename('images/simulationNumber.txt',int(number)+1)  
swarmingCoords.swarmingCoordGeneration(numSteps,frameRate,xFrameSize,yFrameSize,computerPixelSize,numParticles,particleSize,directory,runVelocity,flockingRadius,maxNoiseLevel,delayedResponseTime)