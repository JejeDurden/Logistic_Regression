import os
import argparse
import sys

def parse_arg(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=open_file, help="the file must be a .csv")
    args = parser.parse_args()
    return args.file

def open_file(string):
    if not os.path.exists(string) or string[-4:] != '.csv':
        raise argparse.ArgumentTypeError("{0} is not a valid format or does not exist. Use --help for more informaion".format(string))
    return open(string, 'r')