#!/usr/bin/python3

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import sys
from tools import get_count, get_min,get_max, get_mean, get_std, get_percentile

def render():
    print ("       ")

def describe():
    if os.path.exists('data.csv'):
        data = pd.read_csv("data.csv")
    else:
        print ("There is no data.csv file. Please add one to the same directory as " + sys.argv[0])
        sys.exit()
    counts = []
    means = []
    stds = []
    mins = []
    twentyfives = []
    fifties = []
    seventyfives = []
    maxes = []


if __name__ == "__main__":
    describe()