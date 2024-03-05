import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#C = q*v
def DDMfunctionRunAndTumble(t,A,B,C):
    y = A * ( 1 - np.sinc( C * t) ) + B
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
    taus = []
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
        Binitial = min(DIFCarray)
        Ainitial = max(DIFCarray)- Binitial

        #as velocity is E-6 and and qs are of the order 1000
        Cinitial = 1

        initialParameters = [Ainitial,Binitial,Cinitial]
        
        try:
            parameters, covariance = curve_fit(DDMfunctionRunAndTumble,time,DIFCarray,initialParameters)
            qs.append(q)
            As.append(parameters[0])
            Bs.append(parameters[1])
            Cs.append(parameters[2]) #C = q * v so v = C / q
            Velocities.append(parameters[2]/q)
        except:
            print("error for q",str(q))
            #plt.plot(time,DIFCarray)
            #plt.show()



    file = open(resultantPath,'w')
    for index in range(0,len(qs)):
        file.write("\n"+"{0}\t{1}\t{2}\t{3}\t{4}".format(qs[index],As[index],Bs[index],Cs[index],Velocities[index]))
    file.close()

    return qs,As,Bs,Cs,Velocities




filepaths = ["Uts\zViewSize512_Ut.txt","Uts\zViewSize64_Ut.txt","Uts\zViewSize128_Ut.txt","Uts\zViewSize192_Ut.txt",
             "Uts\zViewSize256_Ut.txt","Uts\zViewSize320_Ut.txt","Uts\zViewSize284_Ut.txt",
             "Uts\zViewSize448_Ut.txt","Uts\zViewSize512_Ut.txt"]

xFrameSize = 512
pixelSize = 1*10**(-6)


for filepath in filepaths:
    resultantPath = "resultantAnalysis\stepsof64" + filepath[3:len(filepath)-7] + ".txt"
    qs,As,Bs,Cs,Velocities = analyseDDMFunctionRunAndTumble(filepath,pixelSize,xFrameSize,resultantPath)
    plt.plot(qs,Velocities)
    plt.title(filepath[3:len(filepath)])
    plt.xlabel("q")
    plt.ylabel("velocities")
    plt.show()