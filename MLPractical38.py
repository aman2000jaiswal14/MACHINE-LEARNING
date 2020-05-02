# assignment
# skin vs age condition - whoes ages is greater than mean age without loop
import matplotlib.pyplot as plt
import pandas as pd
filename= 'indians-diabetes.data.csv'
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df = pd.read_csv(filename,names = hnames)
y = df[df['age']>df.mean()['age']]
plt.plot(y['skin'],y['age'],'mo',label = 'skin vs age(age>mean_age)')
plt.legend(loc = 'best')
plt.show()
