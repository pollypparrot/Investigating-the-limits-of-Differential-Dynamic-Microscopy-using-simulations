#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Mean Squared Displacement calculator
#27/09/23

from scipy import stats
import createGraphs

def calculateGradient(xCoords,yCoords):
    gradient, intercept, r_value, p_value, std_err = stats.linregress(xCoords, yCoords)
    return gradient

#mean displacement checker
#maxStepLength must be smaller than len(coordinates)-1
def meanDisplacementChecker(coordinates,percentOfDataForTimeDelay,frameRate,pixelSize):
    
    #calculate max value of step length as the first 20% of array size
    #div by 5. div rounds down to the nearest integer so makes the smaller choice
    maxValueOfStepLength = round(len(coordinates)*percentOfDataForTimeDelay/100)
   
    #initialise lists
    timeDelays = [0]
    squaredisplacementAverages = [0]
    
    #initialise for percentage calculator
    number = 1
    
    #loop for the number of time delays in graph
    #starting from one as that is the initial step length
    for stepLength in range(1,maxValueOfStepLength+1):
        
        #for larger data sets (greater than 100) this keeps track and outputs a percentage for how far through the data is
        #check if the current step being calculated  is a percent of the total number        
        if (stepLength == number*maxValueOfStepLength//100):
            #outputs the percent and increase number ahead of the next iteration
            print(str(number) + "%")
            number +=1
            
        #reset the total displacement squared for each steplength
        totalDisplacementSquared = 0
        
        #calculate the number of steps required for this step length
        numberSteps = len(coordinates) - stepLength
        
        #loop though the number of steps required. Starting from index 0
        for coordinateIndex in range (0,numberSteps-1):
            
            #calculate the difference between the current coordinate and the one above
            #square the difference and add to the total displacements squared
            difference = (coordinates[coordinateIndex + stepLength] -coordinates [coordinateIndex])*pixelSize #as coordinates are given in pixel size
            differenceSquared = difference*difference
            totalDisplacementSquared +=differenceSquared
        
        #once all coordinates for a step length are added, calculate the average of the squares
        averageDisplacementSquared = totalDisplacementSquared / (numberSteps -1)
        
        #add average squared displacement and step length to their arrays
        squaredisplacementAverages.append(averageDisplacementSquared)
        timeDelays.append(stepLength/frameRate)
        
    return timeDelays, squaredisplacementAverages
    
    
def findGradient(coords,frameRate,pixelSize):
    #start with 20%
    timeDelays, squaredisplacementAverages = meanDisplacementChecker(coords,20,frameRate,pixelSize)
    #to ensure they know to check before graph appears
    input("Prepare to pick up to what point you would like the gradient to be plotted (Press enter to continue)")
    #show graph
    createGraphs.twoDimensionGraphPlot(timeDelays,squaredisplacementAverages,"Time Delays","mean displacement squared")
    #input maximum time delay
    timeDelayChosen = float(input("Up to which time delay would you like the gradient to be plotted to?   "))
    #calculate the chosen index
    chosenIntIndex = round(timeDelayChosen*frameRate)
    #calculate chosen percent
    chosenPercent = chosenIntIndex/len(coords)*100
    #caclculate new arrays and gradient
    timeDelays, squaredisplacementAverages = meanDisplacementChecker(coords,chosenPercent,frameRate,pixelSize)
    gradient = calculateGradient(timeDelays,squaredisplacementAverages)
    #return results
    return timeDelays, squaredisplacementAverages, gradient