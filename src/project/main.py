import cv2
import numpy as np
from SelectiveImageAcquisition import circlePattern
from Utilities import * 

mask = circlePattern(800,200)

image = loadImage('src/interface/images/chaplin.png')

normal = normalizeImage(image)
dft = getDFT(normal)
dft_img = getImage(dft)
masked_data = applyMask(dft_img, mask)
displayImage(dft_img)