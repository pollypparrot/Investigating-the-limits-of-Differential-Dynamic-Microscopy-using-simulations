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

def createVideo(videoFileName,frameRate,xFrameSize,yFrameSize,filenames):
    print("Starting Video Making")
    #make the video
    out = cv2.VideoWriter(videoFileName+'.avi',cv2.VideoWriter_fourcc(*'DIVX'),frameRate,(xFrameSize,yFrameSize))
    #write each file to video
    for filename in filenames:
        out.write(cv2.imread(filename))
    out.release()
    #remove all images
    for filename in set(filenames):
        os.remove(filename)
    print('done') 

#simulator based on the information given by the array.
def coordinateSimulatorMultiple(Title,frameRate,videoFileName,particleSize,xFrameSize,yFrameSize,zCutOff,coordinateFileNames,numSteps,maxPixelStack):
    #initialise pygame
    pygame.init()
    
    #set up the display screen that the user sees
    display = pygame.display.set_mode((xFrameSize,yFrameSize))  #512 pixels by 512 pixels
    pygame.display.set_caption(Title) #set a lable on the frame
        
    imagefilenames = []
    
    print("Starting Image creation")
    #initialise for percentage calculator
    number = 1   
    
    #do a loop for the number of points in the array
    for step in range (0,numSteps):
        #print updates of how far through image creation is
        if (step == number*numSteps//100):
            #outputs the percent and increase number ahead of the next iteration
            print(str(number) + "%")
            number +=1
        
        #change each of the pixels individually to correct colout
        for x in range (0,xFrameSize+1):
            for y in range(0,yFrameSize+1):
                colour = 0
                for filename in coordinateFileNames:
                    #find the new position of the particle
                    xPosition,yPosition,zPosition = textFiles.readTabDelimitedFileThreeDataSpecificLineAsFloat(filename,step+2)
                    #calculate colour
                    #0.2 allows for up to 5 particles on top of each other
                    #255 is maximum intensity
                    #exponential calculates degree of intensity based on the particle
                    colour += (1-(zPosition/zCutOff)**2)*(255*math.exp(-((x-xPosition)**2+(y-yPosition)**2)/(2*particleSize**2)))/(maxPixelStack)
                    #draw point
                if (colour == 0):
                    pass
                else:
                    colour = round(colour)
                [pygame.draw.circle(display, (colour,colour,colour), (x,y), 1)]
                
        #update the display screen
        pygame.display.update()
        
        #save the screen at that point
        filename = f'code/images/frame_{step}.png'
        pygame.image.save(display,filename)
        #add to image list
        imagefilenames.append(filename)
    
    createVideo(videoFileName,frameRate,xFrameSize,yFrameSize,imagefilenames)

        
    pygame.quit()

def checkxyboundries(coordinate,boundry):
    if coordinate>=boundry:
        coordinate-=boundry
    elif coordinate<0:
        coordinate+=boundry
    return coordinate

def checkxyRound(coordinate):
    if coordinate == 0:
        coordinate = 0
    else:
        round(coordinate)
    return(coordinate)

def simulatorParticleByParticle(Title,frameRate,videoFileName,particleSize,xFrameSize,yFrameSize,zCutOff,coordinateFileNames,numSteps,maxPixelStack):
    #initialise pygame
    pygame.init()
    
    #set up the display screen that the user sees
    display = pygame.display.set_mode((xFrameSize,yFrameSize))  #512 pixels by 512 pixels
    pygame.display.set_caption(Title) #set a lable on the frame
        
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

        for filename in coordinateFileNames:
            
            xPosition,yPosition,zPosition = textFiles.readTabDelimitedFileThreeDataSpecificLineAsFloat(filename,step+2)
            
            subtraction = 3*particleSize
            xStart = round(checkxyRound(xPosition -subtraction))
            yStart = round(checkxyRound(yPosition -subtraction))
            
            RangeChecked = round(6*particleSize+1)
            
            for x in range (xStart,xStart+RangeChecked):
                for y in range(yStart,yStart+RangeChecked):
                    
                    x = checkxyboundries(x,xFrameSize)
                    y = checkxyboundries(y,yFrameSize)
                    
                    colourArray[x][y] += (1-(zPosition/zCutOff)**2)*(255*math.exp(-((x-xPosition)**2+(y-yPosition)**2)/(2*particleSize**2)))/(maxPixelStack)
                    
        for x in range (0,xFrameSize):
            for y in range(0,yFrameSize):
                colour = colourArray[x][y]
                if (colour==0):
                    pass
                else:
                    colour = round(colour)
                    pygame.draw.circle(display, (colour,colour,colour), (x,y), 1)
                    colourArray[x][y] = 0
        #update the display screen
        pygame.display.update()     
    
        #save the screen at that point
        filename = f'code/images/frame_{step}.png'
        pygame.image.save(display,filename)
        #add to image list
        imagefilenames.append(filename)
        display.fill(0)

    
    createVideo(videoFileName,frameRate,xFrameSize,yFrameSize,imagefilenames)