import numpy as np
import MyHybridImages
import cv2
import sys

def convolve(image: np.ndarray, sigma: float) -> np.ndarray:
    kernel = MyHybridImages.makeGaussianKernel(sigma)
    r = np.convolve(image, kernel)
    cv2.imwrite("np_convolved.png", r)

if __name__ == "__main__":
    args = sys.argv[1:]
    img = cv2.imread(args[0])
    sigma = (float) (args[1])
    convolve(img, sigma)