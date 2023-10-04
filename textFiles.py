#Holly Chandler
#Fast Image Analysis of Swimming Microbes
#Dissertation code
#Text Files sorter
#27/09/23

  
#create new file
#WARNING will overwrite data in file if it already exists (useful for running program many times but be careful)
def createTabDelimitedFile (fileName, data):
    file = open(fileName, "w")
    file.close()
    