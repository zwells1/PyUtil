import configparser
import os
import sys

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def getConfig(filePath): 
    
    if not os.path.exists(filePath):
        print(
                "\tERROR: " + __file__ + 
                "\n\tmethod: " + sys._getframe(  ).f_code.co_name + 
                "\n\tfilePath: " + filePath)
        
        sys.exit(1)

    cfg = configparser.ConfigParser()
    cfg.read(filePath)
    return cfg

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def checkFor(cfg, sectionOptionsDict):
    
    for eachSection in sectionOptionsDict:
        if not cfg.has_section(eachSection):
            print(
                "\tERROR: " + __file__ + 
                "\n\tmethod: " + sys._getframe(  ).f_code.co_name +
                "\n\tsection issue: " + eachSection)
            sys.exit(1)

        for eachOption in sectionOptionsDict[eachSection]:
            if not cfg.has_option(eachSection, eachOption):
                print(
                    "\tERROR: " + __file__ + 
                    "\n\tmethod: " + sys._getframe(  ).f_code.co_name +
                    "\n\toption issue: " + eachOption)
                sys.exit(1)

