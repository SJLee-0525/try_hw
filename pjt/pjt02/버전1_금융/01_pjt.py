import csv
import pandas as pd
import numpy as np

def file_open_by_numpy():  
    np_netflix = np.loadtxt('archive/NFLX.csv', delimiter = ",", encoding = 'cp949', dtype = str)
    return np_netflix

netflix = file_open_by_numpy()
columns = netflix[0]
netflix = np.delete(netflix, 0, 0)
df_netflix = pd.DataFrame(netflix, columns=columns)
print(df_netflix.loc[:, 'Date':'Close'])