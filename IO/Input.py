import sys
import os

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def filePathCheck(PathAndFile):
    
    if os.path.isfile(PathAndFile):
        return PathAndFile
    else:
        print ("Error: IO/Input.py -- Path to file doesn't exist: " + PathAndFile)
        sys.exit(1)


