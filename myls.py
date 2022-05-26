import os
import sys
import argparse

# Create the parser
my_parser = argparse.ArgumentParser(prog = "myls", 
                                    usage='%(prog)s [options] path',
                                    description='List content of folder')

# add args
my_parser.add_argument("Path",
                        metavar="path",
                        type=str,
                        help="the path to list")

# execute the method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print("Path doesn't exist")
    sys.exit()

print('\n'.join(os.listdir(input_path)))

