import pandas
filename = "indians-diabetes.data.csv"
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = pandas.read_csv(filename,names=hnames)
# Peek at Your Data
# review the first 20 rows of your data using the head
# function of the Pandas DataFrame.
print(dataframe.head(10)) # give topmost 10 data by default it give 5 topmost data
print("-*-" * 20)
# Dimensions of YOur Data
print("dataframe.shape : ",dataframe.shape)
print("-*-" * 20)
# Data Type For Each Attribute
print(dataframe.dtypes) # not available in numpy
# dtype tells whether data is usable or not

print("-#-"*20)


# Descriptive Statistics
# pandas.set_option('display.width',1000)
pandas.set_option('precision',2)
print("description = \n", dataframe.describe()) # it generate report , very important for machine learning
print("-*-"*20)

# Class Distribution ( Classification Only)
print()

class_counts = dataframe.groupby('class').size() # grouping of the data according to a specific feature
print(class_counts)
print("-#-"*20)

# Correlations Between Attributes
# Correlation refers t the relationship between
# and how they may or may not change together.
correlations= dataframe.corr(method='pearson') # features selection
print(correlations)