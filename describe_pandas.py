#!/usr/bin/python3

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import sys


def describe():
    if os.path.exists('dataset_train.csv'):
        data = pd.read_csv("dataset_train.csv")
    else:
        print ("There is no data.csv file. Please add one to the same directory as " + sys.argv[0])
        sys.exit()
    print(data.describe())

if __name__ == "__main__":
    describe()