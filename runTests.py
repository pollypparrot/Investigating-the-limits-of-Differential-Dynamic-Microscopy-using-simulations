#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Test Data from here

import createGraphs
import meanSquaredDisplacementCalculator
import RandomWalkSimulator
import simulationCode
import textFiles
import runAndTumble
import math
import circularTrajectories
import swarmingCoords
import numpy as np

#initalise known variables about system
fluidViscosity = 10**(-3)        #unit of Pascal seconds
sphereRadius = 1 * 10**(-6)    #unit of metres
temp = 300                       #unit of Kelvin

#initialise variables for the camera
frameRate = 100                  #unit of Hertz
timePeriod = 1/frameRate
xFrameSize = 512 #in no.pixels
yFrameSize = 512 #in no. pixels
zFrameSize = 512
zCutOff = zFrameSize/2 #constant. Div 1 to get lowest integer number
computerPixelSize = 1e-6 #in m

#initialise general particle variables
particleSize = sphereRadius*2/computerPixelSize  #diameter in pixel size
numParticles = 100
runVelocity = 100e-6 # in m/s  doesnt apply fr brownian motion


#initialise run and tumble variables
avgRunTime = 1 #in seconds
tumbleTime = 0.05 #in seconds
tumbleAngle = 60
probTumble = 1/(frameRate*avgRunTime)

#initialise circularTrajectories variables
angularVelocity = 15e-6 #in m/s
distanceFromCentre = 25
pClockwise= 0.7

#initialise swarming variables
flockingRadius = 4
maxNoiseLevel = np.pi/2 #number from 0-pi

#decideing length of data
videoLength = 8 #in seconds

#videoLength*frameRate must be integer for code to work.
numSteps = int(videoLength*frameRate)

fileNames=[]
print("makingCoords")
pixelCoords = swarmingCoords.swarmingCoordGeneration(numSteps,timePeriod,xFrameSize,yFrameSize,runVelocity,numParticles,computerPixelSize,flockingRadius,maxNoiseLevel)
print("Appending")
for x in range(0,len(pixelCoords)):
    xCoords = pixelCoords[x][0]
    yCoords = pixelCoords[x][1]
    zCoords = np.zeros(numSteps)
    filename = f'code/coords/set_{x}.txt'
    textFiles.makeTabDelimitedFileThreeData(filename,xCoords,yCoords,zCoords,"X","Y","Z")
    fileNames.append(filename)

print("startSim")
simulationTypePath = 'Swarming' + '_fr' + str(flockingRadius)+ '_noise' + str(maxNoiseLevel/math.pi) +"pi" + '_v' + str(runVelocity) + '_noP' + str(numParticles) + '_s' + str(particleSize)
imageFileNames = simulationCode.simulatorParticleByParticle(frameRate,particleSize,xFrameSize,yFrameSize,zCutOff,fileNames,numSteps,simulationTypePath)
