import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#C = q*v
def DDMfunctionRunAndTumble(t,A,C):
    y = A * ( 1 - np.sinc( C * t) ) 
    return y

def analyseDDMFunctionRunAndTumble(filepath, pixelSize, xFrameSize, resultantPath):  
    #initialise lists  
    file = open(filepath,'r')
    data = []
    time = []
    qs = []
    As = []
    Bs = []
    Cs = [] # c = q*v
    Velocities = []

    deltaq = 2*np.pi/(pixelSize*xFrameSize)
    
    #split data into colums
    for line in file:
        data.append(line.split())
    file.close()

    #get the time step variables
    for step in range(0,len(data)):
        time.append(float(data[step][0]))

    #for each q after this
    for arrayNumber in range (1,len(data[0])):
        DIFCarray = []
        #get te data
        for step in range (0,len(data)):
            DIFCarray.append(float(data[step][arrayNumber]))

        q = arrayNumber * deltaq

        #create initial values
        Ainitial = max(DIFCarray)

        #as velocity is E-6 and and qs are of the order 1000
        Cinitial = 1

        initialParameters = [Ainitial,Cinitial]
        
        try:
            parameters, covariance = curve_fit(DDMfunctionRunAndTumble,time,DIFCarray,initialParameters)
            qs.append(q)
            As.append(parameters[0])
            Cs.append(parameters[1]) #C = q * v so v = C / q
            Velocities.append(parameters[1]/q)
        except:
            print("error for q",str(q))
            #plt.plot(time,DIFCarray)
            #plt.show()



    file = open(resultantPath,'w')
    for index in range(0,len(qs)):
        file.write("\n"+"{0}\t{1}\t{2}\t{3}".format(qs[index],As[index],Cs[index],Velocities[index]))
    file.close()

    return qs,As,Cs,Velocities


xFrameSize = 512
pixelSize = 1e-6

filepath = 'Uts\\runOnlySpeed30_1_Ut.txt'
resultantPath = 'FittingResults\\runOnlySpeed30_1_fittingResults.txt'
qs,As,Cs,Velocities = analyseDDMFunctionRunAndTumble(filepath,pixelSize,xFrameSize,resultantPath)
plt.plot(qs,Velocities)
plt.title('runOnlyMotion_Ut')
plt.xlabel("q")
plt.ylabel("velocities")
plt.show()