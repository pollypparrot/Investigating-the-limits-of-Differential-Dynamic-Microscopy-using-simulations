#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Text Files sorter
#27/09/23

import split
  
#create new file
#WARNING will overwrite data in file if it already exists (useful for running program many times but be careful)
def createFile (fileName):
    file = open(fileName, "x")
    file.close()

#adds items from the array data into a tab delimited file
#only input one set of numbers
def createTabDelimitedFile(fileName, data):
    file = open(fileName, "w")
    for item in range (0,len(data)):
        file.write(str(data[item])+"\t")
    file.close()

#read data from tab delimited file
#one set of data
def readIntTabDelimitedFile(fileName):
    file = open(fileName,"r")
    txt = file.read()
    data = txt.split()
    for item in range (0,len(data)):
        data[item] = int(data[item])
    file.close()
    
    
#createTabDelimitedFile("Xcoord",[23,2,5,34,26,4,2,4,5,3])
#readIntTabDelimitedFile("Xcoord")