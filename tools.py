import copy

def get_count(data):
    return len(data.index)

def get_mean(data, column):
    return data[column].sum() / get_count(data)

def get_std(data, column):
    col_mean = get_mean(data, column)
    n = get_count(data)
    quadra_mean = 0
    for index, row in data.iterrows():
        quadra_mean += (row[column] - col_mean) **2
    return  quadra_mean / n
    

def get_min(data, column):
    minimum = data[column].iloc[0]
    for index, row in data.iterrows():
        if row[column] < minimum:
            minimum = row[column]
    return minimum
        

def get_max(data, column):
    maximum = data[column].iloc[0]
    for index, row in data.iterrows():
        if row[column] > maximum:
            maximum = row[column]
    return maximum

def get_percentile(data, column, percentile):
    data_cpy = copy.deepcopy(data)
    data_cpy.sort_values(by=column, inplace=True)
    data_cpy = data_cpy.reset_index(drop=True)
    count = get_count(data_cpy)
    indice = (percentile / 100) * count
    if indice.is_integer():
        for index, row in data_cpy.iterrows():
            if index == indice - 1:
                if index < count - 1 and index != 0: 
                    return (row[column] + data_cpy[column].iloc[index + 1]) / 2
                else :
                    return row[column]
                    
    else:
        indice = int(indice)
        for index, row in data_cpy.iterrows():
            if index == indice - 1:
                return row[column]
