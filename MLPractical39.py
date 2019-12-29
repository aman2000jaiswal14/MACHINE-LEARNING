import matplotlib.pyplot as plt
import numpy as np
t= np.arange(0.0,5.0,0.2)
# evenly sampled time at 200 ms intervals

print(t)
# red sashes , blue squares and green triangle
plt.plot(t,t,'r*-',t,t+3,'bs-',t,t+6,'g-',t,t+6,'yo',markersize=5 )
plt.show()