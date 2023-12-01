import numpy as np
import matplotlib as plt
from scipy.optimize import curve_fit


filepath = 'HCB1737_10x_100Hz_phase_contrast_0-4000_Ut.txt'

def DDMfunction(t,A,B,tau):
    y = A*(1-np.exp(t/tau))+B
    return y

frameRate = 100
xFrameSize = 512

file = open(filepath,'r')
data = []
time = []
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
        parameters, covariance = curve_fit(DDMfunction,time,array)
        q = arrayNumber* deltaq
        file = open('data.txt','a')
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

