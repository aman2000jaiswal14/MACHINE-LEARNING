import pandas as pd
filename= "mydata.csv"
hnames=['d1','d2','d3','d4','d5','d6','d7','d8','d9']
df = pd.read_csv(filename,delimiter=',',names=hnames)
# particular row or column
print(df.loc[2:5,"d2":"d4"])
print()
print(df.loc[3,"d3"])
# set index
df1 = df.set_index("d3",drop = False)
print(df1.loc[0,"d2"])
#print column of any dataframe
print(df[["d1","d2"]])

#indexloc
print(df.iloc[2:4,1:2])