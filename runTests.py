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
import os

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
zFrameViewSize = 400
zFrameOneSide = zFrameSize/2 #constant. Div 1 to get lowest integer number
zFrameViewOneSize = zFrameViewSize/2
computerPixelSize = 1e-6 #in m

#initialise general particle variables
particleSize = sphereRadius*2/computerPixelSize  #diameter in pixel size
numParticles = 100
runVelocity = 25e-6 # in m/s  doesnt apply fr brownian motion


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
videoLength = 5 #in seconds

#videoLength*frameRate must be integer for code to work.
numSteps = int(videoLength*frameRate)


def swarmingGeneration():
    fileNames=[]
    print("makingCoords")
    pixelCoords = swarmingCoords.swarmingCoordGeneration(numSteps,timePeriod,xFrameSize,yFrameSize,runVelocity,numParticles,computerPixelSize,flockingRadius,maxNoiseLevel,delayedResponseTime)
    print("Appending")
    for x in range(0,len(pixelCoords)):
        xCoords = pixelCoords[x][0]
        yCoords = pixelCoords[x][1]
        zCoords = np.zeros(numSteps)
        filename = f'coords/set_{x}.txt'
        textFiles.makeTabDelimitedFileThreeData(filename,xCoords,yCoords,zCoords,"X","Y","Z")
        fileNames.append(filename)

    print("startSim")
    #directory information
    number = textFiles.readInFileOneDataFilename('images/simulationNumber.txt')
    directory = 'images/simulation_' + number
    os.mkdir(directory)  
    textFiles.createFileOneDataFilename('images/simulationNumber.txt',int(number)+1)
    textFiles.makeTabDelimitedFileTwoData(directory+'_info',['swarming','video Length','number Of Steps','frame Rate',' frame Size in X','frame Size in Y','pixel Size','Number of Particles','particle Radius','flocking Radius','noise','run velocity'],['',str(videoLength),str(numSteps),str(frameRate),str(xFrameSize),str(yFrameSize),str(computerPixelSize),str(numParticles),str(sphereRadius),str(flockingRadius),str(maxNoiseLevel),str(runVelocity)],'','')
    simulationCode.simulatorParticleByParticle(frameRate,particleSize,xFrameSize,yFrameSize,zFrameOneSide,fileNames,numSteps,directory,zFrameViewOneSize)


def runAndTumbleGeneration():
    fileNames=[]
    print("makingCoords")
    for x in range(0,numParticles):
        xCoords, yCoords, zCoords, time  = runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zFrameOneSide,computerPixelSize,runVelocity,probTumble,tumbleTime,tumbleAngle)
        filename = f'coords/set_{x}.txt'
        textFiles.makeTabDelimitedFileThreeData(filename,xCoords,yCoords,zCoords,"X","Y","Z")
        fileNames.append(filename)
    print("startSim")
    #directory information
    number = textFiles.readInFileOneDataFilename('images/simulationNumber.txt')
    directory = 'images/simulation_' + number
    os.mkdir(directory)  
    textFiles.createFileOneDataFilename('images/simulationNumber.txt',int(number)+1)
    textFiles.makeTabDelimitedFileTwoData(directory+'_info',['run And Tumble','video Length','number Of Steps','frame Rate',' frame Size in X','frame Size in Y','pixel Size','Number of Particles','particle Radius','Z cut off','Z view one size',' Run Velocity','average run time','tumble probability per frame',' tumble time',' tumble angle'],['',str(videoLength),str(numSteps),str(frameRate),str(xFrameSize),str(yFrameSize),str(computerPixelSize),str(numParticles),str(sphereRadius),str(zFrameOneSide),str(zFrameViewOneSize),str(runVelocity),str(avgRunTime),str(probTumble),tumbleTime,tumbleAngle],'','')
    simulationCode.simulatorParticleByParticle(frameRate,particleSize,xFrameSize,yFrameSize,zFrameOneSide,fileNames,numSteps,directory,zFrameViewOneSize)


def brownianMotionGenerationtxtFile():
    fileNames=[]
    print("makingCoords")
    for x in range(0,numParticles):
        xCoords, yCoords, zCoords, time  = RandomWalkSimulator.randomWalkCoordinateGeneration(numSteps,fluidViscosity,sphereRadius,temp,frameRate,xFrameSize,yFrameSize,zFrameOneSide,computerPixelSize)
        filename = f'coords/set_{x}.txt'
        textFiles.makeTabDelimitedFileThreeData(filename,xCoords,yCoords,zCoords,"X","Y","Z")
        fileNames.append(filename)
    print("startSim")
    #directory information
    number = textFiles.readInFileOneDataFilename('images/simulationNumber.txt')
    directory = 'images/simulation_' + number
    os.mkdir(directory)  
    textFiles.createFileOneDataFilename('images/simulationNumber.txt',int(number)+1)
    textFiles.makeTabDelimitedFileTwoData(directory+'_info',['brownian Motion','video Length','number Of Steps','frame Rate',' frame Size in X','frame Size in Y','pixel Size','Number of Particles','particle Radius','Z cut off','Z frame view one side','fluid Viscoscity','Temperature','diffusion coeff'],['',str(videoLength),str(numSteps),str(frameRate),str(xFrameSize),str(yFrameSize),str(computerPixelSize),str(numParticles),str(sphereRadius),str(zFrameOneSide),str(zFrameViewOneSize),str(fluidViscosity),str(temp),str(RandomWalkSimulator.diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius))],'','')
    simulationCode.simulatorParticleByParticle(frameRate,particleSize,xFrameSize,yFrameSize,zFrameOneSide,fileNames,numSteps,directory,zFrameViewOneSize)


def brownianMotionGenerationList():
    totCoords=[]
    print("makingCoords")
    for x in range(0,numParticles):
        xCoords, yCoords, zCoords, time  = RandomWalkSimulator.randomWalkCoordinateGeneration(numSteps,fluidViscosity,sphereRadius,temp,frameRate,xFrameSize,yFrameSize,zFrameOneSide,computerPixelSize)
        totCoords.append([xCoords,yCoords,zCoords])
    print("startSim")
    #directory information
    number = textFiles.readInFileOneDataFilename('images/simulationNumber.txt')
    directory = 'images/simulation_' + number
    os.mkdir(directory)  
    textFiles.createFileOneDataFilename('images/simulationNumber.txt',int(number)+1)
    textFiles.makeTabDelimitedFileTwoData(directory+'_info',['brownian Motion','video Length','number Of Steps','frame Rate',' frame Size in X','frame Size in Y','pixel Size','Number of Particles','particle Radius','Z cut off','Z frame view one side','fluid Viscoscity','Temperature','diffusion coeff'],['',str(videoLength),str(numSteps),str(frameRate),str(xFrameSize),str(yFrameSize),str(computerPixelSize),str(numParticles),str(sphereRadius),str(zFrameOneSide),str(zFrameViewOneSize),str(fluidViscosity),str(temp),str(RandomWalkSimulator.diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius))],'','')
    simulationCode.simulatorParticleByParticleList(frameRate,particleSize,xFrameSize,yFrameSize,zFrameOneSide,totCoords,numSteps,directory,zFrameViewOneSize)


swarmingGeneration()