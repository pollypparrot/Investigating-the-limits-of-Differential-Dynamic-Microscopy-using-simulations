#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Simulation Code

import math 
import numpy as np
import textFiles
import matplotlib.pyplot as plt
import multiprocessing

#boundryConditionsFunction
def checkxyboundries(coordinate,boundry):
    if coordinate>=boundry:
        coordinate-=boundry
    elif coordinate<0:
        coordinate+=boundry
    return coordinate

#checkIf the value is 0.0 as round() gives errors if 0.0
def checkxyRound(coordinate):
    if math.isnan(coordinate):
        print(coordinate)
        coordinate = 0
    else:
        round(coordinate)
    return(coordinate)   
    
    
def  simulatorParticleByParticle(frameRate,particleSize,xFrameSize,yFrameSize,zFrameOneSide,coordinateFileNames,numSteps,directory,zFrameViewOneSize):     
    #initilase pixel array   
    colourArray = np.zeros((xFrameSize,yFrameSize),dtype = float)
    
    #initialise for percentage calculator
    number = 1   
    print("Starting Image creation")
    
    #do a loop for the number of points in the array
    for step in range (0,numSteps):
        #reset colourArray to zero
        colourArray.fill(0)    
           
        #print updates of how far through image creation is
        if (step == number*numSteps//100):
            #outputs the percent and increase number ahead of the next iteration
            print(str(number) + "%")
            number +=1

        #for each trajectory
        for filename in coordinateFileNames:
            
            #find particle position
            xPosition,yPosition,zPosition = textFiles.readTabDelimitedFileThreeDataSpecificLineAsFloat(filename,step+2)
            
            #calculate a box around the gaussian splodge as all relevant informaion is within it
            subtraction = 3*particleSize
            xStart = int(checkxyRound(xPosition -subtraction)//1)
            yStart = int(checkxyRound(yPosition -subtraction)//1)
            
            RangeChecked = round(6*particleSize+1)
            
            for x in range (xStart,xStart+RangeChecked):
                for y in range(yStart,yStart+RangeChecked):
                    
                    x = checkxyboundries(x,xFrameSize)
                    y = checkxyboundries(y,yFrameSize)
                    
                    if (zPosition>zFrameViewOneSize)or (zPosition<-zFrameViewOneSize):
                        pass
                    else:
                        #add in the change of colour for the splodge at that point
                        colourArray[x][y] += (1-(zPosition/zFrameViewOneSize)**2)*(255*math.exp(-((x-xPosition)**2+(y-yPosition)**2)/(2*particleSize**2)))
        
        #plot colours and save the file in images        
        plt.imshow(colourArray,cmap='gray',interpolation='none', vmin=0)
        plt.axis('off')
        filename = directory+f'/{step}.png'
        plt.savefig(filename)

        
def  simulatorParticleByParticleList(frameRate,particleSize,xFrameSize,yFrameSize,zCutOff,totCoords,numSteps,directory,zFrameViewOneSize):     
    #initilase pixel array  
    colourArray = np.zeros((xFrameSize,yFrameSize),dtype = float)
    
    #initialise for percentage calculator
    number = 1   
    print("Starting Image creation")
    
    #do a loop for the number of points in the array
    for step in range (0,numSteps):
        #reset colourArray to zero
        colourArray.fill(0)    
           
        #print updates of how far through image creation is
        if (step == number*numSteps//100):
            #outputs the percent and increase number ahead of the next iteration
            print(str(number) + "%")
            number +=1

        #for each trajectory
        for element in range(0,len(totCoords)):
            
            #find particle position
            xPosition = totCoords[element][0][step]
            yPosition = totCoords[element][1][step]
            zPosition = totCoords[element][2][step]
            
            #calculate a box around the gaussian splodge as all relevant informaion is within it
            subtraction = 3*particleSize
            xStart = int(checkxyRound(xPosition -subtraction)//1)
            yStart = int(checkxyRound(yPosition -subtraction)//1)
            
            RangeChecked = round(6*particleSize+1)
            
            for x in range (xStart,xStart+RangeChecked):
                for y in range(yStart,yStart+RangeChecked):
                    
                    x = checkxyboundries(x,xFrameSize)
                    y = checkxyboundries(y,yFrameSize)
                    
                    if (zPosition>zFrameViewOneSize)or (zPosition<-zFrameViewOneSize):
                        pass
                    else:
                        #add in the change of colour for the splodge at that point
                        colourArray[x][y] += (1-(zPosition/zFrameViewOneSize)**2)*(255*math.exp(-((x-xPosition)**2+(y-yPosition)**2)/(2*particleSize**2)))
        
        #plot colours and save the file in images        
        plt.imshow(colourArray,cmap='gray',interpolation='none', vmin=0)
        plt.axis('off')
        filename = directory+f'/{step}.png'
        plt.savefig(filename)

        
