#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#15/09/23

import math
import numpy as np
import matplotlib.pyplot as plt

#pick three random directions
def randomDirection():
    #random number choice
    xDirection = np.random.randint(-100,100) 
    yDirection = np.random.randint(-100,100)
    zDirection = np.random.randint(-100,100)
    #find normalisation factor
    normalisationFactor = 1/np.sqrt(xDirection**2+yDirection**2+zDirection**2)
    #unit directions
    xDirection=xDirection*normalisationFactor
    yDirection=yDirection*normalisationFactor
    zDirection=zDirection*normalisationFactor
    #return values
    return xDirection,yDirection,zDirection

#Change by a set degree
#takes input of the xyz normalised unit direction and the angle that the change is to be in
#returns new unit direction
def setAngleChangeDirection(initialX,initialY,initialZ,tumbleAngle):
    #make angle turn in radians
    tumbleAngle = tumbleAngle*np.pi/180
    #calculate relavant companents of rotation based on intial direction
    r = np.sqrt(initialX**2+initialY**2+initialZ**2)
    phi = math.atan2(initialY,initialX)
    theta = np.arccos(initialZ/r)
    psi = np.random.randint(0,2*np.pi)
    #initialise matrixs
    matrixstartingVector = [0,0,1]
    matrixRotateBySetAmount_Y = [
                                [np.cos(tumbleAngle),0,np.sin(tumbleAngle)],
                                [0,1,0],
                                [-np.sin(tumbleAngle),0,np.cos(tumbleAngle)]
                                ]
    matrixRotateRandom_Z = [
                            [np.cos(psi),-np.sin(psi),0],
                            [np.sin(psi),np.cos(psi),0],
                            [0,0,1]
                            ]
    matrixRotateTheta_Y = [
                            [np.cos(theta),0,np.sin(theta)],
                            [0,1,0],
                            [-np.sin(theta),0,np.cos(theta)]
                            ]
    matrixRotatePhi_Z = [
                        [np.cos(phi),-np.sin(phi),0],
                        [np.sin(phi),np.cos(phi),0],
                        [0,0,1]
                        ]
    #calculate final direction
    finalVector = np.matmul(matrixRotatePhi_Z,np.matmul(matrixRotateTheta_Y,np.matmul(matrixRotateRandom_Z,np.matmul(matrixRotateBySetAmount_Y,matrixstartingVector))))
    return finalVector[0], finalVector[1], finalVector[2]

 
def tumbleStartCheck(probTumble):
     #generate random number
        uniformGuess=np.random.uniform(0,1)
        #if it is less than the probability then a tumble occurs
        if uniformGuess<probTumble:
            return 1
        else:
            return 0
    
#calculates run and tumble images
def runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle):
    
    #initialise variables for simulation time
    #initilase pixel array   
    colourArray = np.zeros((xFrameSize,yFrameSize),dtype = float)
    
    #calculate time period
    timePeriod = 1/frameRate
     
    #initialise coordinate list, direction list, tumbling list and tumblingTime list
    coords = np.zeros((numParticles,3))
    directions = np.zeros((numParticles,3))
    #0 is tumble not occuring, 1 is tumble occuring
    tumbling = np.zeros(numParticles)
    tumblingTotalTimes = np.zeros(numParticles)
    
    #for each particle
    for index in range(0,numParticles):
        #setup initial positions
        coords[index][0]=np.random.randint(0,xFrameSize)
        coords[index][1]=np.random.randint(0,yFrameSize)
        coords[index][2]=np.random.randint(-zCutoffVolume,zCutoffVolume)
        #setup initial directions
        xDirection,yDirection,zDirection = randomDirection()
        directions[index][0]=xDirection
        directions[index][1]=yDirection
        directions[index][2]=zDirection
        #see if it is already in a tumble
        tumbleOccuring = tumbleStartCheck(probTumble)
        #if it is
        if tumbleOccuring == 1:
            #change result to state this in tumbling matrix
            tumbling[index]=1
            #set how long it has been tumbling for already
            tumblingTotalTimes[index] = np.random.uniform(0,tumbleTime)
    
    #setup complete
    #now begin doing coordinate changes:
    
    #for the number of frames that need to be generated
    for step in range (0,numSteps):
        
        print(str(step),"/",str(numSteps))
        ##NewCoordinateGeneration##
        
        #then go particle by particle for that frame
        for particleIndex in range (0,numParticles):
            
            #first check if tumble is already occuring:
            if tumbling[particleIndex]==1:
                
                #add timestep for how long a tumble has been going
                currentTumbleTime = tumblingTotalTimes[particleIndex] + timePeriod
                
                #check if tumble is now finished
                if currentTumbleTime>tumbleTime:
                    #state that the tumble is now finished
                    tumbling[particleIndex] = 0
                else:    
                    #update the total tumble time
                    tumblingTotalTimes[particleIndex] = currentTumbleTime
                    
                #particles do not move during tumbles so the coordinates stay the same
                #no code needed to change coordinate position
            
            #if we arent already tumbling
            else:
                
                #we need to check if we are about to start tumbling
                if tumbleStartCheck(probTumble)==1:
                    
                    #state that a tumble is now occuring
                    tumbling[particleIndex] = 1
                    
                    #update the time tracker
                    tumblingTotalTimes[particleIndex] =  timePeriod
                    
                    #generate the new direction for the particle to move in and save this                   
                    xDirection,yDirection,zDirection = setAngleChangeDirection(xDirection,yDirection,zDirection,tumbleAngle)
                    directions[index][0]=xDirection
                    directions[index][1]=yDirection
                    directions[index][2]=zDirection
                
                    #particles do not move during tumbles so the coordinates stay the same
                    #no code needed to change coordinate position
                    
                #otherwise we move in set direction
                else:
                    #calculate new coordinates
                    newXCoordinate = coords[particleIndex][0] + timePeriod*runVelocity*directions[particleIndex][0]*1/computerPixelSize
                    newYCoordinate = coords[particleIndex][1] + timePeriod*runVelocity*directions[particleIndex][1]*1/computerPixelSize
                    newZCoordinate = coords[particleIndex][2] + timePeriod*runVelocity*directions[particleIndex][2]*1/computerPixelSize
                    
                    #boundary check coordinates
                    #x
                    newXCoordinate=newXCoordinate%xFrameSize
                    #y
                    newYCoordinate=newYCoordinate%yFrameSize
                    #z
                    if(newZCoordinate>zCutoffVolume):
                        newZCoordinate-=2*zCutoffVolume
                    elif(newZCoordinate<-zCutoffVolume):
                        newZCoordinate+=2*zCutoffVolume

                    #change the stored coordinates
                    coords[particleIndex][0]=newXCoordinate
                    coords[particleIndex][1]=newYCoordinate
                    coords[particleIndex][2]=newZCoordinate
        
        ##IMAGE GENERATION##
        
        #for each step the colour intensity array is reset to 0
        #this is what provides the final output
        colourArray.fill(0)  
                    
        #now the particles movement is updated we can add its intensity difference to colour array
        for particleIndex in range (0,numParticles):
            
            zCoordinate = coords[particleIndex][2]
            
            #if the particle is out of the z viewing range then it does not contribute to intensity
            if (zCoordinate>zCutoffView)or (zCoordinate<-zCutoffView):
                pass
            
            #otherwise it does contribute
            else:
                
                #get position on the grid
                xCoordinate = coords[particleIndex][0]
                yCoordinate = coords[particleIndex][1]
                
                apparentZParticleSize = (0.266*zCoordinate+particleSize)/3
            
                #calculate a box around the GAUSSIAN splodge as all relevant informaion is within it
                #standard deviation is the apparent particle size
                subtraction = 3*apparentZParticleSize
                
                #find box boundaries that intensity will be calculated within
                #math.ceiling makes sure to always round up
                xStart = math.ceil(xCoordinate -subtraction)
                yStart = math.ceil(yCoordinate -subtraction)
                RangeChecked = math.ceil(6*apparentZParticleSize+1)
                
                #for the box around the particle (~99% data)
                for x in range (xStart,xStart+RangeChecked):
                    for y in range(yStart,yStart+RangeChecked):
                        
                        x = x%xFrameSize
                        y = y%yFrameSize
                        
                        #add in the change of colour for the splodge at that point
                        colourArray[x][y] += (1-(zCoordinate/zCutoffView)**2)*(255*math.exp(-((x-xCoordinate)**2+(y-yCoordinate)**2)/(2*apparentZParticleSize**2)))/5 ##NEED MAX PIXEL STACK AGAIN NOT JUST 5
        
        #once all particle contributions are calculated
        
        #plot colours and save the file in images        
        plt.imshow(colourArray,cmap='gray',interpolation='none', vmin=0,vmax = 255)
        plt.axis('off')
        filename = directory+f'/{step}.png'
        plt.savefig(filename)