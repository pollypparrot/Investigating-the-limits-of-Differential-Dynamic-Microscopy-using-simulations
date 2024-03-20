#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Test Data from here


import textFiles
import math
import circularTrajectories
import swarmingCoords
import numpy as np
import os
import runAndTumble
import brownianMotion
import runOnly

#initalise known variables about system
fluidViscosity = 1.380649e-23       #unit of Pascal seconds
sphereRadius = 1e-6   #unit of metres
temp = 1.884955592153876e-14                      #unit of Kelvin

#initialise variables for the camera
frameRate = 100                  #unit of Hertz
timePeriod = 1/frameRate
xFrameSize = 512 #in no.pixels
yFrameSize = 512 #in no. pixels
zFrameSize = 512  #Chosen based on data giving size expansion   
zCutoffVolume = zFrameSize/2 #constant. Div 1 to get lowest integer number
computerPixelSize = 1e-6 #in m

#initialise general particle variables
particleSize = sphereRadius*2/computerPixelSize  #diameter in pixel size #units-pixels    
numParticles = 100
runVelocity = 1.42e-05# in m/s 


#initialise run and tumble variables
avgRunTime = 0.86 #in seconds
tumbleTime = 0.14 #in seconds
tumbleAngle = 68
probTumble = 1/(frameRate*avgRunTime)

#initialise circularTrajectories variables
angularVelocity = 15e-6 #in m/s
distanceFromCentre = 25
pClockwise= 0.7

#initialise swarming variables
flockingRadius = 5
maxNoiseLevel = np.pi/2 #number from 0-pi
delayedResponseTime=0.05

#decideing length of data
videoLength = 10 #in seconds

#videoLength*frameRate must be integer for code to work.   
numSteps = int(videoLength*frameRate)


#Brownian motion- 512 visable
""" 
zViewSize = 512
zCutoffView = zViewSize/2
directory = 'images\dissertationVideos2\diffusionSMALL' 
#make place for images to be stored
os.mkdir(directory)
brownianMotion.randomWalkCoordinateGeneration(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,fluidViscosity,sphereRadius,temp) 
 """
#purely run motion only- 512 visable

""" zViewSize = 512
zCutoffView = zViewSize/2

runVelocity = 1.42e-05# in m/s 

directory = 'images\dissertationVideos2\particlesRunOnlyEColi1' 
os.mkdir(directory)
runOnly.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\particlesRunOnlyEColi2' 
os.mkdir(directory)
runOnly.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\particlesRunOnlyEColi3' 
os.mkdir(directory)
runOnly.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,sphereRadius,videoLength)


runVelocity = 20e-6# in m/s 

directory = 'images\dissertationVideos2\particlesRunOnly20Speed2' 
os.mkdir(directory)
runOnly.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\particlesRunOnly20Speed3' 
os.mkdir(directory)
runOnly.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,sphereRadius,videoLength)

runVelocity = 30e-6# in m/s 

directory = 'images\dissertationVideos2\particlesRunOnly30Speed1' 
os.mkdir(directory)
runOnly.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\particlesRunOnly30Speed2' 
os.mkdir(directory)
runOnly.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\particlesRunOnly30Speed3' 
os.mkdir(directory)
runOnly.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,sphereRadius,videoLength) """

#run with instant tumbles- 512 visable
""" zViewSize = 512
zCutoffView = zViewSize/2
probTumble = 1/(frameRate*avgRunTime)
tumbleTime = 0 #in seconds
runVelocity = 14.2e-06# in m/s 

directory = 'images\dissertationVideos2\instantTumble1' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

directory = 'images\dissertationVideos2\instantTumble2' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

directory = 'images\dissertationVideos2\instantTumble3' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

runVelocity = 20e-06# in m/s 

directory = 'images\dissertationVideos2\instantTumble20Speed1' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

directory = 'images\dissertationVideos2\instantTumble20Speed2' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

directory = 'images\dissertationVideos2\instantTumble20Speed3' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

runVelocity = 30e-06# in m/s 

directory = 'images\dissertationVideos2\instantTumble30Speed1' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

directory = 'images\dissertationVideos2\instantTumble30Speed2' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

directory = 'images\dissertationVideos2\instantTumble30Speed3' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)   """

#run with finite tumbles - 512 visable - RUN THREE TIMES
""" 
probTumble = 1/(frameRate*avgRunTime)
tumbleTime = 0.14 #in seconds
runVelocity = 1.42e-05# in m/s 



directory = 'images\dissertationVideos2\eColiTumble1' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\eColiTumble2' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)


directory = 'images\dissertationVideos2\eColiTumble3' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) """ 

#finite tumbles, box size visable - 64 visable

""" zViewSize = 64
zCutoffView = zViewSize/2
probTumble = 1/(frameRate*avgRunTime)
tumbleTime = 0.14 #in seconds
runVelocity = 1.42e-05# in m/s 


directory = 'images\dissertationVideos2\eColiTumble64View1' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\eColiTumble64View2' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\eColiTumble64View3' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

 """


#finite tumbles, box size visable - 288 visable
""" 
zViewSize = 288
zCutoffView = zViewSize/2

directory = 'images\dissertationVideos2\eColiTumble288View1' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\eColiTumble288View2' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\eColiTumble288View3' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) """
#ADD EXPANSION BACK IN!!!!!!!!!!!!!!!!!!!!!!

#run with finite tumbles - 512 visable- expansion

zViewSize = 512
zCutoffView = zViewSize/2
probTumble = 1/(frameRate*avgRunTime)
tumbleTime = 0.14 #in seconds
runVelocity = 1.42e-05# in m/s 


directory = 'images\dissertationVideos2\eColiTumbleExpansionView512_1' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

directory = 'images\dissertationVideos2\eColiTumbleExpansionView512_2' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

directory = 'images\dissertationVideos2\eColiTumbleExpansionView512_3' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength) 

#finite tumbles, box size visable - 64 visable - expansion

zViewSize = 64
zCutoffView = zViewSize/2

directory = 'images\dissertationVideos2\eColiTumbleExpansionView64_1' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\eColiTumbleExpansionView64_2' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\eColiTumbleExpansionView64_3' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

#finite tumbles, box size visable - 288 visable - expansion

zViewSize = 288
zCutoffView = zViewSize/2

directory = 'images\dissertationVideos2\eColiTumbleExpansionView288_1' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\eColiTumbleExpansionView288_2' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)

directory = 'images\dissertationVideos2\eColiTumbleExpansionView288_3' 
os.mkdir(directory)
runAndTumble.runandTumbleCoordinates(numSteps,frameRate,xFrameSize,yFrameSize,zCutoffVolume,zCutoffView,computerPixelSize,numParticles,particleSize,directory,runVelocity,probTumble,tumbleTime,tumbleAngle,avgRunTime,sphereRadius,videoLength)
