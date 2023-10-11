#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Test Data from here

import createGraphs
import meanSquaredDisplacementCalculator
import RandomWalkSimulator
import simulationCode
import textFiles

#initalise known variables
fluidViscosity = 10**(-3)        #unit of Pascal seconds
sphereRadius = 0.5 * 10**(-6)    #unit of metres
temp = 300                       #unit of Kelvin
frameRate = 100                  #unit of Hertz




xCoords,yCoords,zCoords,time = RandomWalkSimulator.randomWalkSimulator(1000,fluidViscosity,sphereRadius,temp,frameRate)
simulationCode.coordinateSimulator("Brownian Motion",xCoords,yCoords,1/frameRate)
#timeDelays, squaredisplacementAverages, xgradient = meanSquaredDisplacementCalculator.meanDisplacementChecker(xCoords)
#print(RandomWalkSimulator.diffusionCoeffCaclculator(temp,fluidViscosity,sphereRadius),xgradient) 
