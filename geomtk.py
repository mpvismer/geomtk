# -*- coding: utf-8 -*-
"""
@author: Mark Vismer
Generic functions for 3D geometry analytics.

In this module, we use arrays not matrices, explained well here:
  https://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u
  
Where possible prefer code in:
 - https://github.com/scipy/scipy/tree/master/scipy/spatial/transform
 - https://github.com/matthew-brett/transforms3d
 
Alternative frameworks to use:
 - https://github.com/moble/quaternion
 - https://docs.blender.org/api/master/mathutils.html


  
"""

from numpy.linalg import norm
from numpy import (
    identity, array, cos, sin, arccos, arcsin, dot, cross, deg2rad, rad2deg )

from scipy.spatial.transform import Rotation

# Homogenous identity matrix
HOMOG_IDENTITY = identity(4)

# Rotational identity matrix
ROT_IDENTITY = identity(3)

# Unit vectors
X_UNIT = array([1, 0, 0])
Y_UNIT = array([0, 1, 0])
Z_UNIT = array([0, 0, 1])

# Gravity constant
G = array([0, 0, -9.81])

# Zero position constant
Z = array([0, 0, 0])


def rot_x(angle):
    return array([
        [1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]
    ])

    
def rot_y(angle):
    return array([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)]
    ])


def rot_z(angle):
    return array([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1]
    ])


def normalise(v):
    """Returns the normalised version of a vector."""
    return v/norm(v)


def coerse_arccos(r):
    return arccos(min(max(r, -1.0), 1.0))


def coerse_arcsin(r):
    return arcsin(min(max(r, -1.0), 1.0))


def hm(rot=ROT_IDENTITY, trans=array([0, 0, 0])):
    """ Create homogenous matrix from rotation and translation."""
    m = HOMOG_IDENTITY.copy()
    m[0:3, 3] = trans[0:3]
    m[0:3, 0:3] = rot
    return m


def skew(v):
    """
    See http://en.wikipedia.org/wiki/Cross_product#Conversion_to_matrix_multiplication
    """
    return array([
        [0, -v[2], v[1]],
        [v[2], 0, -v[0]],
        [-v[1], v[0], 0]
    ])


def rot2aa(rot):
    angle = coerse_arccos(0.5 * (rot.trace() - 1))
    axis = (1.0/(2*sin(angle)))*array([
        [rot[2, 1] - rot[1, 2]],
        [rot[0, 2] - rot[2, 0]],
        [rot[1, 0] - rot[0, 1]]
    ])
    return angle, axis


def aa2rot(angle, axis):
    """ Based on the Rodrigues equation."""
    sk = skew(axis)
    m = ROT_IDENTITY + sk*sin(angle) + (1 - cos(angle)) * dot(sk, sk)
    return m


def quat2rot(quat):
    Rotation.fromquat(quat).as_matrix()
    
