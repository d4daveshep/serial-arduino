import argparse

# set up the command line parser
parser = argparse.ArgumentParser()

# define the argument to set the temperature
parser.add_argument("--set_temp", type=float, help="set the target temperature")

# parse the arguments
args = parser.parse_args()

if args.set_temp:
    target = args.set_temp
    print("target temp set to", target)
    




