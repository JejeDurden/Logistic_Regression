#!/usr/bin/python3

import pandas as pd
import numpy as np
import os
import sys
from tabulate import tabulate

from tools import get_count, get_min, get_max, get_mean, get_std, get_percentile
from parse import parse_arg

def describe(argv):
    fd = parse_arg(argv)
    
    data = pd.read_csv(fd)
    data = data._get_numeric_data()
    counts = ["count"]
    means = ["mean"]
    stds = ["std"]
    mins = ["min"]
    twentyfives = ["25%"]
    fifties = ["50%"]
    seventyfives = ["75%"]
    maxes = ["max"]
    n = len(data.columns)

    for i in range(n):
        counts.append(get_count(data, i))
        means.append(get_mean(data, i))
        stds.append(get_std(data, i))
        mins.append(get_min(data, i))
        twentyfives.append(get_percentile(data, i, 25))
        fifties.append(get_percentile(data, i, 50))
        seventyfives.append(get_percentile(data, i, 75))
        maxes.append(get_max(data, i))
    
    labels = list(data.columns.values)
    labels.insert(0, "  ")
    print (tabulate([counts, means, stds, mins, twentyfives, fifties, seventyfives, maxes], labels, numalign="right"))

if __name__ == "__main__":
    describe(sys.argv[1:])