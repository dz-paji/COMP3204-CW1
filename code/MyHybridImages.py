import math
# import cv2
import numpy as np
from MyConvolution import convolve
def myHybridImages(lowImage: np.ndarray, lowSigma: float, highImage: np.ndarray, highSigma:
float) -> np.ndarray:
    """
    Create hybrid images by combining a low-pass and high-pass filtered pair.
    :param lowImage: the image to low-pass filter (either greyscale shape=(rows,cols) or
    colour shape=(rows,cols,channels))
    :type numpy.ndarray
    :param lowSigma: the standard deviation of the Gaussian used for low-pass filtering
    lowImage
    :type float
    :param highImage: the image to high-pass filter (either greyscale shape=(rows,cols) or
    colour shape=(rows,cols,channels))
    :type numpy.ndarray
    :param highSigma: the standard deviation of the Gaussian used for low-pass filtering
    highImage before subtraction to create the high-pass filtered image
    :type float
    :returns returns the hybrid image created
    by low-pass filtering lowImage with a Gaussian of s.d. lowSigma and combining it
    with
    a high-pass image created by subtracting highImage from highImage convolved with
    a Gaussian of s.d. highSigma. The resultant image has the same size as the input
    images.
    :rtype numpy.ndarray
    """
    # Your code here.
    low_gaussian_kernel = makeGaussianKernel(lowSigma)
    high_gaussian_kernel = makeGaussianKernel(highSigma)
    low_filtered_image = convolve(lowImage, low_gaussian_kernel)
    high_filtered_image = highImage - convolve(highImage, high_gaussian_kernel)

        # print(high_filtered_image.shape)
        # print(low_filtered_image.shape)
    hybrid_image = np.zeros(low_filtered_image.shape)
    hybrid_image = low_filtered_image + high_filtered_image
                
    # cv2.imwrite("low_filtered_image.png", low_filtered_image)
    # cv2.imwrite("high_filtered_image.png", high_filtered_image)
    return hybrid_image




def makeGaussianKernel(sigma: float) -> np.ndarray:
    """
    Use this function to create a 2D gaussian kernel with standard deviation sigma.
    The kernel values should sum to 1.0, and the size should be floor(8*sigma+1) or
    floor(8*sigma+1)+1 (whichever is odd) as per the assignment specification.
    """
    # Your code here.
    size = (int) (8 * sigma + 1)
    if size % 2 == 0:
        size += 1
    
    centre = size // 2
    kernel = np.zeros((size, size))
    
    for i in range(size):
        for j in range(size):
            kernel[j, i] = (float) (1 / 2 * math.pi * (math.pow(sigma,2))) * (math.exp((-0.5) * (math.pow((i - centre) / sigma, 2.0) + math.pow((j - centre) / sigma, 2.0))))
            
    kernel /= np.sum(kernel)
                        
    return kernel