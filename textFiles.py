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

def createTabDelimitedFile(fileName, data):
    file = open(fileName, "w")
    for item in data:
        file.write(str(data[item])+"\t")
    file.close()

def readTabDelimitedFile(fileName):
    file = open(fileName,"r")
    txt = file.read()
    print(txt)
    file.close()
    
    
createTabDelimitedFile("Xcoord",[2,4,5,6,4,2,4,5,3])
readTabDelimitedFile("Xcoord")