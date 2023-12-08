import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


filepath = 'images\simulation_0\sim_1_Ut.txt'
resultPath = 'images\simulation_0\sim_1.results.txt'

def DDMfunction(t,A,B,tau):
    y = A*(1-np.exp(t/tau))+B
    return y

frameRate = 100
xFrameSize = 512

file = open(filepath,'r')
data = []
time = []
tauc = []
qs = []
deltaq = 2*np.pi*frameRate*xFrameSize


for line in file:
    data.append(line.split())
file.close()
for step in range(0,len(data)):
    time.append(np.log(float(data[step][0])))
for arrayNumber in range (1,len(data[0])):
    array = []
    for step in range (0,len(data)):
        array.append(float(data[step][arrayNumber]))
    try:
        print(arrayNumber)
        parameters, covariance = curve_fit(DDMfunction,time,array)
        q = arrayNumber* deltaq
        qs.append(q)
        tauc.append(parameters[2])
        file = open(resultPath,'w')
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
plt.plot(qs,tauc)
plt.xlabel("q")
plt.ylabel("tau")
plt.xlim(1*10**7,2*10**7)
plt.show()

