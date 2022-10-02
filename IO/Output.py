import time

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def getTimeStampedPrependedFile(outputFile):

    return time.strftime("%Y%m%d-%H%M%S--") + outputFile

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def saveDictToNewTimeStampedFile(outputFile, outputDict):

    outputFile = getTimeStampedPrependedFile(outputFile)
    f = open(outputFile, "a")
    for key, value in outputDict.items():
        f.write('file:  %s:     Strings Found:  %s\n' % (key, value))
    f.close()


