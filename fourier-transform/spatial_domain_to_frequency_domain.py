#https://docs.opencv.org/master/de/dbc/tutorial_py_fourier_transform.html

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('../resources/lenna.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f) #Fast Fourier Transform
magnitude_spectrum = 20*np.log(np.abs(fshift))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Spatial Domain'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Frequency Domain / Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()