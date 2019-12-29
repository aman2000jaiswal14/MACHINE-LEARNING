import warnings
warnings.filterwarnings(action="ignore")
import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(412)
plt.plot([1,2,3])

plt.subplot(413)             # 3 rows  1 column   2 is the no of box (see in copy)
plt.plot([4,5,6])

plt.subplot(414)
plt.plot([7,8,9])

plt.figure(2)
plt.plot([11,12,13])

plt.figure(1)
plt.subplot(411)
plt.plot([1,3,9])
plt.title('Easy as 1,2,3')
plt.show()