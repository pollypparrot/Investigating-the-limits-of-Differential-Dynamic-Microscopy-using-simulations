import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


filepath = 'images\sim_1_Ut.txt'
resultPath = 'images\sim_1.results.txt'

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
deltaq = 2*np.pi*pixelSize*xFrameSize


for line in file:
    data.append(line.split())
file.close()
for step in range(0,len(data)):
    time.append(float(data[step][0]))
for arrayNumber in range (1,len(data[0])):
    array = []
    for step in range (0,len(data)):
        array.append(float(data[step][arrayNumber]))
    try:
        Ainitial = max(array)
        Binitial = min(array)
        TauCinitial = 1
        initialParameters = [Ainitial,Binitial,TauCinitial]

        parameters, covariance = curve_fit(DDMfunction,time,array,initialParameters)
        q = arrayNumber* deltaq
        qs.append(q)
        tauc.append(parameters[2])
        file = open(resultPath,'a')
        file.write(' n = '+ str(arrayNumber))
        file.write('   q = ' + str(arrayNumber*deltaq))
        file.write('   A = '+ str(parameters[0]))
        file.write('   B = '+ str(parameters[1]))
        file.write('   tau = '+ str(parameters[2]))
        file.write('   D = '+ str(1/arrayNumber**2*parameters[2]))
        file.write('\n')
        file.close()
    except:
        print('q value of ' + str(arrayNumber) + ' could not be calculated')
plt.scatter(qs,tauc)
plt.yscale('log')
plt.xscale('log')
plt.xlabel("q")
plt.ylabel("tau")
plt.show()



