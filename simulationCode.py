#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Simulation Code

import pygame
import math 
import cv2
import os
import numpy as np

#simulator based on the information given by the array.
def coordinateSimulator(Title,xCoord,yCoord,frameRate,videoFileName,particleSize,xFrameSize,yFrameSize):
    #initialise pygame
    pygame.init()
    
    #set up the display screen that the user sees
    display = pygame.display.set_mode((xFrameSize,yFrameSize))  #512 pixels by 512 pixels
    pygame.display.set_caption(Title) #set a lable on the frame
        
    filenames = []
    
    print("Starting Image creation")
    #initialise for percentage calculator
    number = 1   
    
    #do a loop for the number of points in the array
    for step in range (0,len(xCoord)):
        
        #print updates of how far through image creation is
        if (step == number*len(xCoord)//100):
            #outputs the percent and increase number ahead of the next iteration
            print(str(number) + "%")
            number +=1

        #set position of circle *100000 in order to make each pixcel = 1 um. + 512/2 to make starting position in the middle of the screen
        xPosition = xCoord[step]
        yPosition = yCoord[step]
        
        #change each of the pixels individually to correct colout
        for x in range (0,xFrameSize+1):
            for y in range(0,yFrameSize+1):
                #calculate colour
                colour =  round(255*math.exp(-((x-xPosition)**2+(y-yPosition)**2)/(2*particleSize**2)))
                #draw point
                pygame.draw.circle(display, (colour,colour,colour), (x,y), 1)
                
        #update the display screen
        pygame.display.update()
        
        #save the screen at that point
        filename = f'code/images/frame_{step}.png'
        pygame.image.save(display,filename)
        #add to image list
        filenames.append(filename)
    
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
        
        
        
        
    pygame.quit()

