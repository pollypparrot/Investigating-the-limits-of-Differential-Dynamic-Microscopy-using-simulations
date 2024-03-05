import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import createGraphs
from scipy import stats


filepath = f'images\zViewWholeSize0to256outOf512\zViewSize256_Ut.txt'
resultPath = f'images\zViewWholeSize0to256outOf512\zViewSize256_output.txt'

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
        
        parameters, covariance = curve_fit(DDMfunctionBrownianMotion,time,array,initialParameters)
        q = arrayNumber* deltaq
        qs.append(q)
        As.append(parameters[0])
        Bs.append(parameters[1])
        tauc.append(parameters[2])
        Ds.append(1/(q**2*parameters[2]))
        
    file = open(resultPath,'w')
    for index in range(0,len(qs)):
        file.write("\n"+"{0}\t{1}\t{2}\t{3}\t{4}".format(qs[index],As[index],Bs[index],tauc[index],Ds[index]))
    file.close()

    return qs,As,Bs,tauc,Ds


qs,As,Bs,tauc,Ds = analyseDDMFunctionsBrownianMotion(filepath, pixelSize,xFrameSize)


#finding the gradient of brownian motion analysis on DDM. Expectation is 1.
""" #
deltaq = 2*np.pi*1/(pixelSize*xFrameSize)


#input maximum time delay
startq =  190000
endq = 900000
#calculate the chosen index
startindex = round(startq/deltaq)
endindex = round(endq/deltaq)
gradient, intercept, r_value, p_value, std_err = stats.linregress(np.log(qs[startindex:endindex]), np.log(Ds[startindex:endindex]))
print(gradient)
print(intercept)

xs = []
ys = []
for x in range (round(startq),round(endq)):
    xs.append(x)
    ys.append(gradient*x+intercept)

plt.plot(xs,ys)
plt.scatter(qs,Ds)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("q")
plt.ylabel("D")
plt.show() """
