import matplotlib.pyplot as plt
import numpy as np

#print(plt.__version__)

x= np.array([1,110])
y= np.array([3,260])

#a line
plt.plot(x,y)
plt.show()

#single point
plt.plot(x,y, 'o')
plt.show()

#multiple points
x1= np.array([1,2,10,6,23,21,0,5])
y1= np.array([3,5,6,45,85,12,3,0])

plt.plot(x1,y1)
plt.show()

x1= np.array([1,2,10,6,23,21,0,5])
#y1= np.array([3,5,6,45,85,12,3,0])

plt.plot(x1, marker='o')
plt.show()