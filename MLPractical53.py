# 3D Bar Plots
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
fig = plt.figure()
ax=fig.add_subplot(111,projection='3d')
x=[1,2,3,4,5,6,7,8,9,10]
y=np.random.randint(10,size=10)
z=np.zeros(10)   # to deploy dots on the surface of xy plane ie the base starting point  of the bar
# ground design |^
dx= np.ones(10)     # give the width/thick of the bar
dy=np.ones(10)      # give the width/thick of the bar
dz=[1,2,3,4,5,6,7,8,9,10]   # give the height of the bar
# upper design |^
ax.bar3d(x,y,z,dx,dy,dz,color='g')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
plt.title("3D Bar Chart Example")
plt.tight_layout()
plt.show()
