import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


filepath = 'code\images\sim_1_Ut.txt'
resultPath = 'code\images\sim_1.results.txt'

def DDMfunction(t,A,B,tau):
    y = A*(1-np.exp(-t/tau))+B
    return y

pixelSize = 1*10**-6
xFrameSize = 512

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
    yValue = Ainitial+Binitial/2
    #find assosciated x values
    TauCinitial = 0.1

    initialParameters = [Ainitial,Binitial,TauCinitial]
    
    parameters, covariance = curve_fit(DDMfunction,time,array,initialParameters)
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
    
plt.scatter(qs,tauc)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("q")
plt.ylabel("tau")
plt.show()



