#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Graoh Plotters
#27/09/23

import matplotlib.pyplot as plt
import numpy  as np

#draw a 2D plot with coordinates given in arrays
def twoDimensionGraphPlot(xCoords,yCoords,xLabel,yLabel):
    plt.plot(xCoords,yCoords)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.show()

#draw a 3D plot with coordinates given in arrays
def threeDimensionGraphPlot(xCoords,yCoords,zCoords,xLabel,yLabel,zLabel,title):
    ax = plt.axes(projection='3d')
    ax.plot3D(xCoords, yCoords, zCoords, label = title)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_zlabel(zLabel)
    plt.show()
  
#draw a histogram of data points against a gaussian curve    
def HistogramAndGaussLine(mean,standardDeviation,checkArray):
    count, bins, ignored = plt.hist(checkArray, 30, density=True)
    plt.plot(bins, 1/(standardDeviation * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mean)**2 / (2 * standardDeviation**2) ),
                linewidth=2, color='r')
    plt.show()
    