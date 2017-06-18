"""
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from magneato.objects import StraightWire

# setup grid
xgrid = np.arange(-10, 12, 2)
ygrid = np.arange(-10, 12, 2)
zgrid = np.arange(-10, 12, 2)

# create wire
wire1 = StraightWire(start=np.array([-3, -3, -5]), 
                     end=np.array([-3, -3, 5]), 
                     current=1e7)
wire2 = StraightWire(start=np.array([1, 1, -5]),
                     end=np.array([1, 1, 0]), 
                     current=1e7)

# initialize values
xvals, yvals, zvals, b_x, b_y, b_z = [], [], [], [], [], []

for i, xval in enumerate(xgrid):
    for j, yval in enumerate(ygrid):
        for k, zval in enumerate(zgrid):

            loc = np.array([xval, yval, zval])
            bval = wire1.magnetic_field(loc)+\
                   wire2.magnetic_field(loc)
        
            xvals.append(xval)
            yvals.append(yval)
            zvals.append(zval)
            b_x.append(bval[0])
            b_y.append(bval[1])
            b_z.append(bval[2])

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.quiver(xvals, yvals, zvals, b_x, b_y, b_z, pivot='middle')

plt.show()

