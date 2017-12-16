# execute a python file forever

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="the file you want to run forever")
args = parser.parse_args()

print( 'Running file: ' + args.file )

while True:
    exec(open(args.file).read())
