import sys
import argparse
from pathlib import Path

# set up the command line parser
parser = argparse.ArgumentParser()

# define the argument to set the config file
parser.add_argument("config_file", help="specify the full location of the config file")

# parse the arguments
args = parser.parse_args()

if args.config_file :
    cfgFile = args.config_file
    print('config file is at...', cfgFile)

    if Path(cfgFile).exists() :
        print('file found')
    else :
        print('file NOT found... exiting')
        sys.exit()
    
    

print('carrying on')    

print('config file is at...', cfgFile)
    
    
    




