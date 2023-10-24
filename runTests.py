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

#initalise known variables about system
fluidViscosity = 10**(-3)        #unit of Pascal seconds
sphereRadius = 1 * 10**(-6)    #unit of metres
temp = 300                       #unit of Kelvin

#initialise variables for the camera
frameRate = 100                  #unit of Hertz
xFrameLength = 512 #in no.pixels
yFrameLength = 512 #in no. pixels
pixelSize = 1e-6 #in m

#initialise general particle variables
particleSize = sphereRadius*2/pixelSize  #diameter in pixel size
numParticles = 20
maxPixelStack = 5 # maximum number of pixels on top of each other. larger number reduces the intensity per pixel 

zCutOff = math.sqrt(255*(1/maxPixelStack)) // 1 #constant. Div 1 to get lowest integer number

#initialise run and tumble variables
runTime = 1 #in seconds
runVelocity = 500e-6 # in m/s
tumbleTime = 0.01 #in seconds

#decideing length of data
videoLength = 3 #in seconds

#videoLength*frameRate must be integer for code to work.
numStepsAnalysed = int(videoLength*frameRate)

#Saving video options
videoTitle = "Test"


xCoords,yCoords,zCoords,time=RandomWalkSimulator.randomWalkCoordinateGeneration(numStepsAnalysed,fluidViscosity,sphereRadius,temp,frameRate,xFrameLength,yFrameLength,zCutOff,pixelSize)
textFiles.makeTabDelimitedFileThreeData("filename",xCoords,yCoords,zCoords,"X","Y","Z")
meanSquaredDisplacementCalculator.findGradient(zCoords,frameRate,pixelSize)
""" print(zCutOff)
fileNames = []
for x in range(1,2):
    print("generating set" + str(x))
    xCoords,yCoords,zCoords,time = runAndTumble.runandTumbleCoordinates(numStepsAnalysed,frameRate,xFrameLength,yFrameLength,zCutOff,pixelSize,runTime,runVelocity)
    print("appending")
    filename = f'code/coords/set_{x}.txt'
    textFiles.makeTabDelimitedFileThreeData(filename,xCoords,yCoords,zCoords,"X","Y","Z")
    fileNames.append(filename)

print("startSim")
simulationCode.coordinateSimulatorMultiple("Run and Tumble",frameRate,videoTitle,particleSize,xFrameLength,yFrameLength,fileNames,numStepsAnalysed,maxPixelStack) """

##ISSUE WITH Z COORDS COMING BACK EMPTY RANDOM WALK