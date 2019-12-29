import warnings   # in future if any library is updated and its sub-library is not update then it suppress the warnings
warnings.filterwarnings(action="ignore")
import pandas
import urllib.request
hnames = ['sepal-length','sepal-width','petal-length','petal-width','class']
web_path = urllib.request.urlopen("https://goo.gl/QnHW4g") # it can print any data structure whether it is un structured it will print
dataframe = pandas.read_csv(web_path,names=hnames)
print(dataframe.shape)
print(dataframe)
print(dataframe.columns)