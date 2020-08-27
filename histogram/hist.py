import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../resources/view.png', 0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.subplot(2,2,1)
plt.plot(cdf_normalized, color = 'b')
plt.legend(('cdf_normalized','histogram'), loc = 'upper left')
plt.subplot(2,2,2)
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')


equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
plt.subplot(2,2,3)
plt.imshow(res,cmap = 'gray')

plt.show()




	
	
	
	
	
	