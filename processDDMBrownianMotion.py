import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import createGraphs
from scipy import stats


filepath = f'FinalDDMVideos\\Uts\\diffusion_Ut.txt'
resultPath = f'FinalDDMVideos\\ResultantAnalysis\\diffusion_DDManalysis.txt'

pixelSize = 1*10**-6
xFrameSize = 512

def DDMfunctionBrownianMotion(t,A,B,tau):
    y = A*(1-np.exp(-t/tau))+B
    return y

def analyseDDMFunctionsBrownianMotion(filepath, pixelSize,xFrameSize):

    file = open(filepath,'r')
    data = []
    time = []
    tauc = []
    qs = []
    As = []
    Bs = []
    Ds = []

    deltaq = 2*np.pi*1/(pixelSize*xFrameSize)


    for line in file:
        data.append(line.split())
    file.close()
    for step in range(0,len(data)):
        time.append(float(data[step][0]))
    for arrayNumber in range (1,len(data[0])):
        array = []
        for step in range (0,len(data)):
            array.append(float(data[step][arrayNumber]))
        
        Binitial = min(array)
        Ainitial = max(array)- Binitial
        #find initial tau_C
        TauCinitial = 0.1

        initialParameters = [Ainitial,Binitial,TauCinitial]
        try:

            parameters, covariance = curve_fit(DDMfunctionBrownianMotion,time,array,initialParameters)
            q = arrayNumber* deltaq
            qs.append(q)
            As.append(parameters[0])
            Bs.append(parameters[1])
            tauc.append(parameters[2])
            Ds.append(1/(q**2*parameters[2]))
        except:
            
            print("error for q",str(q))
            plt.plot(time,array)
            plt.show()

        
    file = open(resultPath,'w')
    for index in range(0,len(qs)):
        file.write("\n"+"{0}\t{1}\t{2}\t{3}\t{4}".format(qs[index],As[index],Bs[index],tauc[index],Ds[index]))
    file.close()

    return qs,As,Bs,tauc,Ds


qs,As,Bs,tauc,Ds = analyseDDMFunctionsBrownianMotion(filepath, pixelSize,xFrameSize)
plt.plot(qs,Ds)
plt.show()