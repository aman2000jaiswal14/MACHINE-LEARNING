import pandas as pd
import numpy as np
filename = "mydata.csv"

df = pd.read_csv(filename,header = None)
print(df.groupby(2).size())

