import cv2
import numpy as np
from matplotlib import pyplot as plt

blue = [255, 0, 0]

image = cv2.imread('opencv.png')

replicate = cv2.copyMakeBorder(image, 100, 100, 100, 100, cv2.BORDER_REPLICATE)
constant = cv2.copyMakeBorder(image, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=blue)
reflect = cv2.copyMakeBorder(image, 100, 100, 100, 100, cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(image, 10, 10, 10, 10, cv2.BORDER_WRAP)

cv2.imshow('orijinal', image)
"""cv2.imshow('replicate', replicate)
cv2.imshow('constant', constant)
cv2.imshow('reflect', reflect)
cv2.imshow('reflect101', reflect101)
cv2.imshow('wrap', wrap)"""

plt.subplot(231), plt.imshow(image, 'gray'), plt.title('orijinal')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('replicate')
plt.subplot(233), plt.imshow(constant, 'gray'), plt.title('constant')
plt.subplot(234), plt.imshow(reflect, 'gray'), plt.title('reflect')
plt.subplot(235), plt.imshow(reflect101, 'gray'), plt.title('reflect101')
plt.subplot(236), plt.imshow(wrap, 'gray'), plt.title('wrap')

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()