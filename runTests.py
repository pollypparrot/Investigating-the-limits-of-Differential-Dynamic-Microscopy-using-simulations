#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Test Data from here


import textFiles
import math
import swarmingCoords
import numpy as np
import os
import runAndTumble
import brownianMotion
import runOnly

#initalise known variables about system
sphereRadius = 1e-6   #unit of metres

#initialise variables for the camera
frameRate = 100                  #unit of Hertz
timePeriod = 1/frameRate
xFrameSize = 512 #in no.pixels
yFrameSize = 512 #in no. pixels
zFrameSize = 512  #Chosen based on data giving size expansion   
zCutoffVolume = zFrameSize/2 #constant. Div 1 to get lowest integer number
computerPixelSize = 1e-6 #in m

#initialise general particle variables
particleSize = sphereRadius*2/computerPixelSize  #diameter in pixel size #units-pixels    
numParticles = 100
runVelocity = 1.42e-05# in m/s 


#initialise run and tumble variables
avgRunTime = 0.86 #in seconds
tumbleTime = 0.14 #in seconds
tumbleAngle = 68
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



zCutoffView = 512

diffusionCoeff = 1e-11
directory = 'images\\dissertationVideos2\\1e-11'
os.mkdir(directory)
brownianMotion.randomWalkCoordinateGeneration(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,diffusionCoeff)

diffusionCoeff = 2e-11
directory = 'images\\dissertationVideos2\\2e-11'
os.mkdir(directory)
brownianMotion.randomWalkCoordinateGeneration(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,diffusionCoeff)

diffusionCoeff = 3e-11
directory = 'images\\dissertationVideos2\\3e-11'
os.mkdir(directory)
brownianMotion.randomWalkCoordinateGeneration(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,diffusionCoeff)