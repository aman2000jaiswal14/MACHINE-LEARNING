import matplotlib.pyplot as plt

# if you make multiple lines with
# one plot command, the kwargs
# apply to all those lines, e.g.:
x1=[1,2,3]
y1=[1,2,3]

x2=[1,2,3]
y2=[1,4,9]

plt.plot(x1,y1,x2,y2,linewidth=3)  # x1,x2,x2,x4   --> positional arguments,linewidth is keyword argument(= necessary)
# keyword argument will be written in last
plt.show()
