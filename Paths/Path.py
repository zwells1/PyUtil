import os
import sys

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def getAbsolutePathUpNLevels(absolutePathTo, numberOfLevelsUp = None):
    #will not handle if too many levels up requested.

    print("asdfasdfasdfasdf")
    print("asdfasdfasdfasdf")
    print(absolutePathTo)
    print("asdfasdfasdfasdf")
    print("asdfasdfasdfasdf")

    #lots of path issues in windows need absolute paths over relative.
    if not os.path.exists(absolutePathTo):
        print("Path to file doesn't exist")
        sys.exit(1)

    absPath = os.path.abspath(absolutePathTo)

    if numberOfLevelsUp is None:
        return absPath

    #determine if FS uses /  or \\
    backSlash = '\\'
    forwardSlash = '/'
    selector = None


    #if both found default to /
    if "\\" in r"%r" % absPath:
        selector = backSlash

    if forwardSlash in r"%r" % absPath:
        selector = forwardSlash

    eachLevel = absPath.split(selector)

    reducedPath = None

    #if we go too far just return the highest whether that is C:\ or /home/
    if len(eachLevel) < numberOfLevelsUp:
        reducedPath = absPath[0]
    else:
        reducedPath = eachLevel[:-numberOfLevelsUp]

    reducedPath = selector.join([str(elem) for i, elem in enumerate(reducedPath)])

    listToReturn = None
    if os.name == "posix":
        listToReturn = [reducedPath, '/']
    else: #windows (not considering Mac at this point)
        listToReturn = [reducedPath + '\\']

    return ''.join([str(elem) for i,elem in enumerate(listToReturn)])

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def isScriptFrozen():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        return True
    else:
        return False

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def getAbsolutePathTolerantToFrozenExe():
    if isScriptFrozen():
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))


