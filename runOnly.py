#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#17/03/24

import math
import numpy as np
import matplotlib.pyplot as plt
import textFiles


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
 
#calculates run and tumble images
def runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,sphereRadius,videoLength):
    
    textFiles.makeTabDelimitedFileTwoData(directory+'_info',['run And Tumble','video Length','number Of Steps','frame Rate',' frame Size in X','frame Size in Y','pixel Size','Number of Particles','particle Radius','Z cut off','Z view one size',' Run Velocity'],['',str(videoLength),str(numSteps),str(frameRate),str(xFrameSize),str(yFrameSize),str(computerPixelSize),str(numParticles),str(sphereRadius),str(zCutoffVolume),str(zCutoffView),str(runVelocity)],'','')
    #initialise variables for simulation time
    #initilase pixel array   
    colourArray = np.zeros((xFrameSize,yFrameSize),dtype = float)
    
    #calculate time period
    timePeriod = 1/frameRate
     
    #initialise coordinate list, direction list, tumbling list and tumblingTime list
    coords = np.zeros((numParticles,3))
    directions = np.zeros((numParticles,3))

    
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
    #setup complete
    #now begin doing coordinate changes:
    
    #for the number of frames that need to be generated
    for step in range (0,numSteps):
        
        #print(str(step),"/",str(numSteps))
        ##NewCoordinateGeneration##
        
        #then go particle by particle for that frame
        for particleIndex in range (0,numParticles):
            
                             
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
            if (zCoordinate>zCutoffView) or (zCoordinate<-zCutoffView):
                pass
            
            #otherwise it does contribute
            else:
                
                #get position on the grid
                xCoordinate = coords[particleIndex][0]
                yCoordinate = coords[particleIndex][1]
                
                apparentZParticleSize = particleSize
                
            
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
                        colourArray[x][y] += (1-(zCoordinate/zCutoffView)**2)*(255*math.exp(-((x-xCoordinate)**2+(y-yCoordinate)**2)/(2*apparentZParticleSize**2))) 
        
        #once all particle contributions are calculated
        
        #plot colours and save the file in images        
        filename = directory+f'/{step}.png'
        plt.imsave(fname=filename,arr=colourArray,cmap = 'gray',format = 'png',vmin = 0, vmax = 255)