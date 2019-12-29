# -*- coding: utf-8 -*-
"""
@author: Mark Vismer

Generic functions for 3D geometry plotting and visualisation.
"""

from numpy import vstack

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Frame3D(object):
    def __init__(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        self._axis = ax

    def draw_line(self, p1, p2, style='k--'):
        v = vstack((p1, p2))
        line = self._axis.plot(v[:, 0], v[:, 1], v[:, 2], style)
        return line
    
    def draw_axes(self, rot=None, pos=[0, 0, 0], pose=None, size=0.2):
        if pose is not None:
            rot = pose[0:3, 0:3]
            pos = pose[0:3, 3]
        ax = self._axis
        ax.plot([pos[0]], [pos[1]], [pos[2]], c='k', marker='o')
        pos = pos.reshape((1, 3))
        x_axis = rot[:, 0] * size
        v = vstack((pos, pos + x_axis))
        x = ax.plot(v[:, 0], v[:, 1], v[:, 2], 'r-')
        y_axis = rot[:, 1] * size
        v = vstack((pos, pos + y_axis))
        y = ax.plot(v[:, 0], v[:, 1], v[:, 2], 'g-')
        z_axis = rot[:, 2] * size
        v = vstack((pos, pos + z_axis))
        z = ax.plot(v[:, 0], v[:, 1], v[:, 2], 'b-')
    
    def show(self):
        plt.show()
    
    
