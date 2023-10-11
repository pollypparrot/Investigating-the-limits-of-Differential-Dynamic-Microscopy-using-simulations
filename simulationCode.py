#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Simulation Code

import pygame 
import imageio
import cv2
import os

#simulator based on the information given by the array.
def coordinateSimulator(Title,xCoord,yCoord,timePeriod):
    #initialise pygame
    pygame.init()
    
    #set up the display screen that the user sees
    display = pygame.display.set_mode((512,512))  #512 pixels by 512 pixels
    pygame.display.set_caption(Title) #set a lable on the frame
    
    #set up a clock that is the same speed as the frame rate of the cameras
    frameRate = pygame.time.Clock()
    frameRate.tick(1/timePeriod) # set to the speed of the camera- 100Hz
    
    filenames = []
    
    #do a loop for the number of points in the array
    for step in range (0,len(xCoord)):
        #update the display screen
        pygame.display.update()

        #set position of circle *100000 in order to make each pixcel = 1 um. + 512/2 to make starting position in the middle of the screen
        xPosition = xCoord[step]*1000000 + 512/2 
        yPosition = yCoord[step]*1000000 + 512/2
        
        #fill diplay window with black
        display.fill((255,255,255))
        
        pygame.draw.circle(display,(0,0,0),(xPosition,yPosition),3)#    

        #save the file
        filename = f'code/images/frame_{step}.jpeg'
        pygame.image.save(display,filename)
        filenames.append(filename)
    
    
    out = cv2.VideoWriter('video.avi',cv2.VideoWriter_fourcc(*'DIVX'),100,(512,512))
    for filename in filenames:
        out.write(cv2.imread(filename))
    out.release()
    for filename in set(filenames):
        os.remove(filename)
    print('done')
        
        
        
        
    pygame.quit()

