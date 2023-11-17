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

#initalise known variables about system
fluidViscosity = 10**(-3)        #unit of Pascal seconds
sphereRadius = 1 * 10**(-6)    #unit of metres
temp = 300                       #unit of Kelvin

#initialise variables for the camera
frameRate = 100                  #unit of Hertz
xFrameSize = 512 #in no.pixels
yFrameSize = 512 #in no. pixels
zFrameSize = 512
zCutOff = zFrameSize/2 #constant. Div 1 to get lowest integer number
pixelSize = 1e-6 #in m

#initialise general particle variables
particleSize = sphereRadius*2/pixelSize  #diameter in pixel size
numParticles = 100
maxPixelStack = 15 # maximum number of pixels on top of each other. larger number reduces the intensity per pixel 

#initialise run and tumble variables
avgRunTime = 1 #in seconds
runVelocity = 100e-6 # in m/s
tumbleTime = 0.05 #in seconds
tumbleAngle = 60
probTumble = 1/(frameRate*avgRunTime)

#initialise circularTrajectories variables
angularVelocity = 15
distanceFromCentre = 25
pClockwise= 0.7

#decideing length of data
videoLength = 2 #in seconds

#videoLength*frameRate must be integer for code to work.
numSteps = int(videoLength*frameRate)

#Saving video options
videoFileName = "Test"


fileNames = []
for x in range(0,numParticles):
    print("generating set" + str(x))
    xCoords,yCoords,zCoords,time = circularTrajectories.twoDimensionangularTrajectoryCoordinateGeneration(numSteps,frameRate,xFrameSize,yFrameSize,zCutOff,angularVelocity,distanceFromCentre,pClockwise)
    print("appending")
    filename = f'code/coords/set_{x}.txt'
    textFiles.makeTabDelimitedFileThreeData(filename,xCoords,yCoords,zCoords,"X","Y","Z")
    fileNames.append(filename)

print("startSim")
imageFileNames = simulationCode.simulatorParticleByParticle("Run and Tumble",frameRate,videoFileName,particleSize,xFrameSize,yFrameSize,zCutOff,fileNames,numSteps,maxPixelStack)
print(imageFileNames)

