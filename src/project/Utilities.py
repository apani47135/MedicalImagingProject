import cv2
import numpy as np
from SelectiveImageAcquisition import circlePattern


def loadImage(image_path):
    image = cv2.imread(image_path,0) #Given the path, imread will return the image
    image = cv2.resize(image, (800,800))
    return image



def loadMatrix(filename):
    matrix = None
    return matrix


def saveImage(filename, image):
    return True


def saveMatrix(filename, matrix):
    return True


# map input image to values from 0 to 255"
def normalizeImage(image):
    normalized = np.zeros((800, 800))
    normalized = cv2.normalize(image, normalized, 0, 255, cv2.NORM_MINMAX)
    return normalized



# Remember: the DFT its a decomposition of signals
#  To be able to save it as an image you must convert it.
def writableDFT(dft_image):
    converted = None
    return converted


# Use openCV to display your image"
# Remember: normalize binary masks and convert FFT matrices to be able to see and save them"
def displayImage(image):
    cv2.namedWindow("Image")
    cv2.imshow("Image", image)
    cv2.waitKey()
    cv2.destroyAllWindows4()


def getDFT(image):
    f = cv2.dft(np.float32(image), flags = cv2.DFT_COMPLEX_OUTPUT)
    f_shift = np.fft.fftshift(f)

    return f_shift

# Confert from fft matrix to an image"
def getImage(dft_img):
    f_complex = dft_img[:,:,0] + 1j*dft_img[:,:,1]
    f_abs = np.abs(f_complex) + 1
    f_bounded = 20 * np.log(f_abs)
    f_img = 255 * f_bounded / np.max(f_bounded)
    f_img = f_img.astype(np.uint8)
    return f_img


# Both input values must be raw values"
def applyMask(image_dft, mask):
    masked_data = cv2.bitwise_and(image_dft, image_dft, mask=mask)
    return masked_data


def signalToNoise():
    return False


#[Provide] Use this function to acomplish a good final image
def post_process_image(image):
    a = np.min(image)
    b = np.max(image)
    k = 255
    image = (image - a) * (k / (b - a))
    return image.astype('uint8')

# mask = circlePattern(800,200)

# impage = loadImage('src/interface/images/brain.png')
# normal = normalizeImage(impage)
# dft = getDFT(normal)
# dft_img = getImage(dft)
# masked_data = applyMask(dft_img, mask)
# displayImage(masked_data)
