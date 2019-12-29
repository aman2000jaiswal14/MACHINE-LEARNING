import pandas as pd
import matplotlib.pyplot as plt

filename = 'mydata4.csv'
df = pd.read_csv(filename,header = None)
df.plot(kind = 'box')
plt.show()
