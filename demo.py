# -*- coding: utf-8 -*-
"""
@author: Mark Vismer
"""

import geomtk as gtk
from draw import Frame3D



ax = Frame3D()

ax.draw_axes(pose=gtk.HOMOG_IDENTITY)
p = gtk.Z + 0.5
ax.draw_line([0, 0, 0], p)

rz = gtk.rot_z(gtk.deg2rad(30))
pose = gtk.hm(rz, p)
ax.draw_axes(pose=pose)

ax.show()
