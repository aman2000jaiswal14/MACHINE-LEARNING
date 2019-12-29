import pandas
filename= 'indians-diabetes.data.csv'
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class'] #if lesser metadata(say n) then it leave first n column
# ' , ' delimiter is default pandas
dataframe= pandas.read_csv(filename,names=hnames)  # metadata(names) mandatory otherwise it take first row data as metadata
print("pandas Data : ",dataframe.shape)
print(dataframe)
print("\n\n")
print(type(dataframe))
a=5
print(type(a))
a=12.5
print(type(a))
a="MMM"
print(type(a))
a=[1,2,3,4]
print(type(a))
a=(1,2,3,4)
print(type(a))

