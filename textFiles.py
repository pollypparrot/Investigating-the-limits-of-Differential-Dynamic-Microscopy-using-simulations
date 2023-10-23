#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Text Files sorter
#27/09/23

import split
import linecache

#create new file
#WARNING will overwrite data in file if it already exists (useful for running program many times but be careful)
def createFile (fileName):
    file = open(fileName, "x")
    file.close()


#adds items from the array data into a tab delimited file
#only input one set of numbers
def createFileOneData(fileName, data):
    file = open(fileName, "w")
    for item in range (0,len(data)):
        file.write(str(data[item])+"\t")
    file.close()


#read data from tab delimited file
#one set of data
def readInFileOneData(fileName):
    file = open(fileName,"r")
    txt = file.read()
    data = txt.split()
    for item in range (0,len(data)):
        data[item] = float(data[item])
    file.close()
    return(data)


#write two sets of data to a tab delimited function
def makeTabDelimitedFileTwoData(filename,data1,data2,data1Label,data2Label):
    file = open(filename,'w')
    file.write("{0}\t{1}".format(data1Label,data2Label))
    for item1, item2 in zip(data1,data2):
        file.write("\n"+"{0}\t{1}".format(item1,item2))
    file.close()


#read two sets of data in a tab delimited file
def readTabDelimitedFileTwoData(filename):
    file = open(filename,'r')
    
    #import data
    text = file.read()
    fileData = text.split("\n")
        
    #get names of data recieved
    data1Label,data2Label = fileData[0].split()
    
    #initialise data arrays
    data1 = []
    data2 = []

    #read data line by line
    for line in range(1,len(fileData)):
        value1,value2 = fileData[line].split("\t")
        data1.append(value1)
        data2.append(value2)
    
    #change to floats
    for item in range (0,len(data1)):
        data1[item] = float(data1[item])
        data2[item] = float(data2[item])
    file.close()

    return data1, data2, data1Label, data2Label


#write three sets of data to a tab delimited function
def makeTabDelimitedFileThreeData(filename,data1,data2,data3,data1Label,data2Label,data3Label):
    file = open(filename,'w')
    file.write("{0}\t{1}\t{2}".format(data1Label,data2Label,data3Label))
    for x in range(0,len(data1)):
        file.write("\n"+"{0}\t{1}\t{2}".format(data1[x],data2[x],data3[x]))
    file.close()



#read three sets of data in a tab delimited file
def readTabDelimitedFileThreeData(filename):
    file = open(filename,'r')
    
    #import data
    text = file.read()
    fileData = text.split("\n")
        
    #get names of data recieved
    data1Label,data2Label,data3Label = fileData[0].split()
    
    #initialise data arrays
    data1 = []
    data2 = []
    data3 = []
    
    #read data line by line
    for line in range(1,len(fileData)):
        value1,value2,value3 = fileData[line].split("\t")
        data1.append(value1)
        data2.append(value2)
        data3.append(value3)
        
    #change to floats
    for item in range (0,len(data1)):
        data1[item] = float(data1[item])
        data2[item] = float(data2[item])
        data3[item] = float(data3[item])
    file.close()

    return data1, data2, data3, data1Label, data2Label, data3Label


#read three sets of data in a tab delimited file
def readTabDelimitedFileThreeDataSpecificLineAsFloat(filename,lineNumber):
    #read data line by line
    value1,value2,value3 = linecache.getline(filename,lineNumber,module_globals=None).split("\t")
    value1 = float(value1)
    value2=float(value2)
    value3=float(value3)
    return value1,value2,value3
