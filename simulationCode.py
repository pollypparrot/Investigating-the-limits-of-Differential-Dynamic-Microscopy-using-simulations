#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Simulation Code

import pygame 

#simulator based on the information given by the array.
def coordinateSimulator(Title,xCoord,yCoord):
    #initialise pygame
    pygame.init()
    
    #set up the display screen that the user sees
    display = pygame.display.set_mode((512,512))  #512 pixels by 512 pixels
    pygame.display.set_caption(Title) #set a lable on the frame
    
    #set up a clock that is the same speed as the frame rate of the cameras
    frameRate = pygame.time.Clock()
    frameRate.tick(100) # set to the speed of the camera- 100Hz
    
    #do a loop for the number of points in the array
    for step in range (0,len(xCoord)):
        #update the display screen
        pygame.display.update()

        #set position of circle *100000 in order to make each pixcel = 1 um. + 512/2 to make starting position in the middle of the screen
        xPosition = xCoord[step]*1000000 + 512/2 
        yPosition = yCoord[step]*1000000 + 512/2
        
        #fill diplay window with black
        display.fill((0,0,0))
        
        pygame.draw.circle(display,(255,255,255),(xPosition,yPosition),3)
    
    
    pygame.quit()


import RandomWalkSimulator
xCoords,yCoords,zCoords,time = RandomWalkSimulator.randomWalkSimulator(100000)    
coordinateSimulator("Hello",xCoords,yCoords)