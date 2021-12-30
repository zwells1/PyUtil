from IO import ConfigParserWrappers
from Welcome import Generic
import sys
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def main(argv):
    print("Tests from Welcome folder") 
    print(Generic.Welcome.__name__)
    Generic.Welcome()


    print("Tests from IO folder") 
    print(ConfigParserWrappers.getConfig.__name__)
    cfg = ConfigParserWrappers.getConfig("IO/TestInputs/ConfigParserInput.txt")
    
    print(ConfigParserWrappers.checkFor.__name__)
    sectionsOptions = {
            'Test': ['RootDirToSearch', 'SearchFor']}
    ConfigParserWrappers.checkFor(cfg, sectionsOptions)


# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main(sys.argv[1:])
