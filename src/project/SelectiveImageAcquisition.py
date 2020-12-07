import numpy as np
import cv2


##
# Objective: Simulate different types of acquisition patterns by implementing the
# following functions.
##

def cartesianPattern(mask_size, percent):
    mask = None
    return mask


def circlePattern(mask_size, radius):
    circle_img = np.zeros((mask_size,mask_size), np.uint8)
    cv2.circle(circle_img, (int(mask_size/2), int(mask_size/2)), radius, 255, thickness=-1)
    mask = circle_img
    return mask


def ellipsePattern(mask_size, major_axis, minor_axis, angle):
    mask = None
    return mask


def bandPattern(mask_size, width, length, angle):
    mask = None
    return mask


def radialPattern(mask_size, ray_count):
    mask = None
    return mask


def spiralPattern(mask_size, sparsity):
    mask = None
    return mask
