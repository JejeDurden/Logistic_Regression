import copy
from math import sqrt, pow, isnan

def get_count(data, column):
    return len(data) - data.iloc[:,column].isnull().sum()

def get_mean(data, column):
    return data.iloc[:, column].sum() / get_count(data, column)

def get_std(data, column):
    col_mean = get_mean(data, column)
    n = get_count(data, column)
    quadra_mean = 0
    for index, row in data.iterrows():
        if not isnan(row[column]):
            quadra_mean += pow(row[column] - col_mean, 2)
    return sqrt(quadra_mean / (n - 1))
    

def get_min(data, column):
    minimum = data.iloc[0, column]
    for index, row in data.iterrows():
        if row[column] < minimum:
            minimum = row[column]
    return minimum
        

def get_max(data, column):
    maximum = data.iloc[0, column]
    for index, row in data.iterrows():
        if row[column] > maximum:
            maximum = row[column]
    return maximum

def get_percentile(data, column, percentile):
    data_cpy = copy.deepcopy(data)
    count = get_count(data_cpy, column)    
    data_cpy.sort_values(by=data.columns.values[column], inplace=True)
    data_cpy = data_cpy.reset_index(drop=True)
    indice = (percentile / 100) * count
    if indice.is_integer():
        for index, row in data_cpy.iterrows():
            if index == indice - 1:
                return ((row[column] + data_cpy.iloc[index + 1, column]) / 2)
                    
    else:
        indice = round(indice)
        for index, row in data_cpy.iterrows():
            if index == indice:
                return row[column]
