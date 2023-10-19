#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Test Data from here

import createGraphs
import meanSquaredDisplacementCalculator
import RandomWalkSimulator
import simulationCode
import textFiles

#initalise known variables about system
fluidViscosity = 10**(-3)        #unit of Pascal seconds
sphereRadius = 0.5 * 10**(-6)    #unit of metres
temp = 300                       #unit of Kelvin
frameRate = 100                  #unit of Hertz

#more set variables
xFrameLength = 512
yFrameLength = 512
particleSize = 2  #in radius of pixel circle
pixelSize = 1e-6 #in m
numStepsAnalysed = 100

#Saving video options
videoTitle = "Test"


xCoords,yCoords,zCoords,time = RandomWalkSimulator.randomWalkCoordinateGeneration(numStepsAnalysed,fluidViscosity,sphereRadius,temp,frameRate,xFrameLength,yFrameLength,pixelSize)
timeDelays, squaredisplacementAverages, gradient= meanSquaredDisplacementCalculator.findGradient(xCoords,frameRate,pixelSize)
createGraphs.twoDimensionGraphPlot(timeDelays,squaredisplacementAverages,"Time Delays","mean displacement squared")
print(gradient,RandomWalkSimulator.diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius))


#simulationCode.coordinateSimulator(videoTitle,xCoords,yCoords,frameRate,videoTitle,particleSize,xFrameLength,yFrameLength)
#timeDelays, squaredisplacementAverages, xgradient = meanSquaredDisplacementCalculator.meanDisplacementChecker(xCoords)
#print(RandomWalkSimulator.diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius),xgradient) 
