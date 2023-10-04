#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Mean Squared Displacement calculator
#27/09/23

from scipy import stats

#mean displacement checker
#maxStepLength must be smaller than len(coordinates)-1
def meanDisplacementChecker(coordinates, maxValueOfStepLength):
    
    #Check for human error in Max Step length that would break program.
    if (maxValueOfStepLength>= (len(coordinates) -1)):
        raise ValueError ("Maximum Step Length is too high. Must be smaller than the length of the array input")
    
    #initialise lists
    timeDelays = [0]
    squaredisplacementAverages = [0]
    
    #loop for the number of time delays in graph
    #starting from one as that is the initial step length
    for stepLength in range(1,maxValueOfStepLength+1):
        
        #reset the total displacement squared for each steplength
        totalDisplacementSquared = 0
        
        #calculate the number of steps required for this step length
        numberSteps = len(coordinates) - stepLength
        
        #loop though the number of steps required. Starting from index 0
        for coordinateIndex in range (0,numberSteps-1):
            
            #calculate the difference between the current coordinate and the one above
            #square the difference and add to the total displacements squared
            difference = coordinates[coordinateIndex + stepLength] -coordinates [coordinateIndex]
            differenceSquared = difference*difference
            totalDisplacementSquared +=differenceSquared
        
        #once all coordinates for a step length are added, calculate the average of the squares
        averageDisplacementSquared = totalDisplacementSquared / (numberSteps -1)
        
        #add average squared displacement and step length to their arrays
        squaredisplacementAverages.append(averageDisplacementSquared)
        timeDelays.append(stepLength/100)
    
    #calculate gradient of the graph
    
    gradient, intercept, r_value, p_value, std_err = stats.linregress(timeDelays, squaredisplacementAverages)
    
    
    return timeDelays, squaredisplacementAverages, gradient
    