import sys
import os
import ast


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def filePathCheck(PathAndFile):
    
    if os.path.isfile(PathAndFile):
        return PathAndFile
    else:
        print ("Error: IO/Input.py -- Path to file doesn't exist: " + PathAndFile)
        sys.exit(1)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def getDictionaryFromFile(PathAndFile):
    filePathCheck(PathAndFile)

    # reading the data from the file
    with open(PathAndFile) as f:
        data = f.read()

    # reconstructing th# reconstructing the data as a dictionary
    return ast.literal_eval(data)