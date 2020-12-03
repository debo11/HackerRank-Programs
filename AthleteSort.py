import numpy as np
import pandas as pd


def AthleteSort(row, column, sort_column):
    list1 = []
    entries = list (map (int, input ().split ()))
    matrix = np.array (entries).reshape (row, column)
    data = pd.DataFrame (matrix)
    result = data.sort_values (sort_column)
    return result


# insert the input for row and columns space separated and hit enter after final input

row = int (input ("Enter the number of rows:"))
column = int (input ("Enter the number of columns:"))
sort_column = int (input ("Enter Column No. for Sorting:"))
output = AthleteSort (row, column, sort_column)
print (output)
