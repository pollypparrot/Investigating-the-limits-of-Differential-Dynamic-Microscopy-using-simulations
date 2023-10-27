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
zCutOff = 51 #constant. Div 1 to get lowest integer number
pixelSize = 1e-6 #in m

#initialise general particle variables
particleSize = sphereRadius*2/pixelSize  #diameter in pixel size
numParticles = 100
maxPixelStack = 2 # maximum number of pixels on top of each other. larger number reduces the intensity per pixel 

#initialise run and tumble variables
runTime = 1 #in seconds
runVelocity = 100e-6 # in m/s
tumbleTime = 0.01 #in seconds

#initialise circularTrajectories variables
angularVelocity = 7
distanceFromCentre = 10

#decideing length of data
videoLength = 3 #in seconds

#videoLength*frameRate must be integer for code to work.
numSteps = int(videoLength*frameRate)

#Saving video options
videoFileName = "Test"


fileNames = []
for x in range(0,numParticles):
    print("generating set" + str(x))
    xCoords,yCoords,zCoords,time = circularTrajectories.angularTrajectoryCoordinateGeneration(numSteps,frameRate,xFrameSize,yFrameSize,zCutOff,pixelSize,angularVelocity,distanceFromCentre)
    print("appending")
    filename = f'code/coords/set_{x}.txt'
    textFiles.makeTabDelimitedFileThreeData(filename,xCoords,yCoords,zCoords,"X","Y","Z")
    fileNames.append(filename)

print("startSim")
simulationCode.simulatorParticleByParticle("Run and Tumble",frameRate,videoFileName,particleSize,xFrameSize,yFrameSize,zCutOff,fileNames,numSteps,maxPixelStack)

""" 
xp=40
yp=40
zp = -25
x=40
y=40
 
print(math.exp(-((x-xp)**2+(y-yp)**2)/(2*particleSize**2)))

b=2*particleSize**2

print(math.exp(-(xp**2)/b)*(1+x*2*xp/b-(x**2)*(b-2*xp**2)/b**2)*math.exp(-((y-yp)**2)/(2*particleSize**2)))

#x**3*(4*xp**3-6*b*xp)/(3*b**3)
# """