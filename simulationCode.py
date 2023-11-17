#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Simulation Code

import pygame
import math 
import cv2
import os
import numpy as np
import textFiles
import matplotlib.pyplot as plt


def createVideoCOMPRESS(videoFileName,frameRate,xFrameSize,yFrameSize,filenames):
    print("Starting Video Making")
    #make the video
    out = cv2.VideoWriter(videoFileName+'.avi',-1,frameRate,(xFrameSize,yFrameSize))
    #write each file to video
    for filename in filenames:
        out.write(cv2.imread(filename))
    out.release()
    #remove all images
    for filename in set(filenames):
        os.remove(filename)
    print('done') 


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

def OLDPYGAMEsimulatorParticleByParticle(Title,frameRate,videoFileName,particleSize,xFrameSize,yFrameSize,zCutOff,coordinateFileNames,numSteps,maxPixelStack):
    #initialise pygame
    pygame.init()
    
    #set up the display screen that the user sees
    display = pygame.display.set_mode((xFrameSize,yFrameSize))  #512 pixels by 512 pixels
    pygame.display.set_caption(Title) #set a lable on the frame
    
    #initilase pixel array and array of images    
    imagefilenames = []
    colourArray = np.zeros((xFrameSize,yFrameSize),dtype = float)

    
    #initialise for percentage calculator
    number = 1   

    print("Starting Image creation")
    
    #do a loop for the number of points in the array
    for step in range (0,numSteps):
        
        #reset colourArray to zero
                
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
                    
                    x = x%xFrameSize
                    y = y%yFrameSize
                    
                    #add in the change of colour for the splodge at that point
                    colourArray[x][y] += (1-(zPosition/zCutOff)**2)*(255*math.exp(-((x-xPosition)**2+(y-yPosition)**2)/(2*particleSize**2)))/(maxPixelStack)
        
        #add colour to every pixel if it is non-zero colour for the particles position
        for x in range (0,xFrameSize):
            for y in range(0,yFrameSize):
                colour = colourArray[x][y]
                if (colour==0):
                    pass
                else:
                    colour = colour//1
                    pygame.draw.circle(display, (colour,colour,colour), (x,y), 1)
                    #reset all values to zero for next go
                    colourArray[x][y] = 0
        #update the display screen
        pygame.display.update()     
    
        #save the screen at that point
        filename = f'code/images/frame_{step}.png'
        pygame.image.save(display,filename)
        #add to image list
        imagefilenames.append(filename)
        #clear the screen for next image
        display.fill(0)

    
    
    
    
def   simulatorParticleByParticle(frameRate,particleSize,xFrameSize,yFrameSize,zCutOff,coordinateFileNames,numSteps,simulationTypePath):
    
    #directory information
    directory = 'code/images/' + str(simulationTypePath) + '_' + str(frameRate) + '_' + str(particleSize)  + '_' + str(xFrameSize) + '_' + str(yFrameSize) + '_' + str(zCutOff) + '_' + str(numSteps)
    os.mkdir(directory)       
    #initilase pixel array and array of images    
    imagefilenames = []
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
                    
                    #add in the change of colour for the splodge at that point
                    colourArray[x][y] += (1-(zPosition/zCutOff)**2)*(255*math.exp(-((x-xPosition)**2+(y-yPosition)**2)/(2*particleSize**2)))
        
        #plot colours and save the file in images        
        plt.imshow(colourArray,cmap='gray',interpolation='none', vmin=0)
        plt.axis('off')
        filename = directory+f'/{step}.png'
        plt.savefig(filename)
        imagefilenames.append(filename)
    return imagefilenames
        
