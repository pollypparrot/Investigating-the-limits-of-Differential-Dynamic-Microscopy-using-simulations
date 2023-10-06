#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Test Data from here

import createGraphs
import meanSquaredDisplacementCalculator
import RandomWalkSimulator
import simulationCode
import textFiles


xCoords,yCoords,zCoords,time = RandomWalkSimulator.randomWalkSimulator(100000)
textFiles.createTabDelimitedFile("Xcoords",xCoords)
textFiles.createTabDelimitedFile("YCoords",yCoords)
XCOORDS = textFiles.readIntTabDelimitedFile("Xcoords")
YCOORDS = textFiles.readIntTabDelimitedFile("Ycoords")
print(XCOORDS)
xtimeSteps, xaverageSquaredDisplacement, xgradient = meanSquaredDisplacementCalculator.meanDisplacementChecker(XCOORDS,50)
ytimeSteps, yaverageSquaredDisplacement, ygradient = meanSquaredDisplacementCalculator.meanDisplacementChecker(xCoords,50)    
simulationCode.coordinateSimulator("Hello",XCOORDS,YCOORDS)
createGraphs.twoDimensionGraphPlot(xtimeSteps,xaverageSquaredDisplacement,"Time Steps","X Average Squared Displacement")
createGraphs.twoDimensionGraphPlot(ytimeSteps,yaverageSquaredDisplacement,"Time Steps","Y Average Squared Displacement")


""" xCoords,yCoords,zCoords,time = randomWalkSimulator(90000)

from meanSquaredDisplacementCalculator import meanDisplacementChecker
xtimeSteps, xaverageSquaredDisplacement, xgradient= meanDisplacementChecker(xCoords,50)
ytimeSteps, yaverageSquaredDisplacement, ygradient = meanDisplacementChecker(yCoords,50)
ztimeSteps, zaverageSquaredDisplacement, zgradient = meanDisplacementChecker(zCoords,50)
twoDimensionGraphPlot(xtimeSteps,xaverageSquaredDisplacement,"Time Steps","X Average Squared Displacement")
twoDimensionGraphPlot(ytimeSteps,yaverageSquaredDisplacement,"Time Steps","Y Average Squared Displacement")
twoDimensionGraphPlot(ztimeSteps,zaverageSquaredDisplacement,"Time Steps","Z Average Squared Displacement")
print(diffusionCoeffCaclculator(300,10**(-3),0.5*10**(-6)), xgradient,ygradient,zgradient) """


""" twoDimensionGraphPlot(xCoords,yCoords,"X axis","Y axis")
twoDimensionGraphPlot(xCoords,zCoords,"X axis","Z axis")
twoDimensionGraphPlot(yCoords,zCoords,"Y axis","Z axis")
twoDimensionGraphPlot(time,xCoords,"Time","X axis")
twoDimensionGraphPlot(time,yCoords,"Time","Y axis")
twoDimensionGraphPlot(time,zCoords,"Time","Z axis")
threeDimensionGraphPlot(xCoords,yCoords,zCoords,"X axis","Y Axis","Z Axis","Brownian Motion") """