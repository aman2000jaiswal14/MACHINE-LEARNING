# Pie Charts

import matplotlib.pyplot as plt
labels = 'S1','S2','S3'
sections=[30,50,20]
# sections=[60,100,40]
colors=['c','g','r']

plt.pie(sections,labels=labels,colors=colors,
        startangle=90,
        explode=(0,0.1,0),
        autopct='%1.2f%%') # autopct means auto percentage
      # % means blank space in which 1.2f is fill up
      # negative means left align , positive means right align
      # print float value with 2 decimal places
# plt.axis('equal')
plt.title('Pie Chart Example')
plt.show()
