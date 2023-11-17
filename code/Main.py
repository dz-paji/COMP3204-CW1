import sys
import cv2
import numpy as np

from MyHybridImages import myHybridImages, makeGaussianKernel
from MyConvolution import convolve

def testHybrid():
    args = sys.argv[1:]
    if len(args) != 4:
        print("Usage: python Main.py lowImage lowSigma highImage highSigma")
        sys.exit(1)
        
    low = cv2.imread(args[0])
    low_sigma = float(args[1])
    high = cv2.imread(args[2])
    high_sigma = float(args[3])
    
    hybrid = myHybridImages(low, low_sigma, high, high_sigma)
    cv2.imwrite("hybrid.png", hybrid)
    
def testConv():
    args = sys.argv[1:]
    if len(args) != 4:
        print("Usage: python Main.py lowImage lowSigma highImage highSigma")
        sys.exit(1)
        
    low = cv2.imread(args[0])
    low_sigma = float(args[1])
    high = cv2.imread(args[2])
    high_sigma = float(args[3])
    
    # hybrid = myHybridImages(low, low_sigma, high, high_sigma)
    # cv2.imwrite("hybrid.png", hybrid)
    low_padded = convolve(low, makeGaussianKernel(low_sigma))
    # cv2.imshow("low_padded", low_padded)
    # cv2.waitKey(0)
    cv2.imwrite("low_padded.png", low_padded[:, :, 0])

    
def testGaussian():
    k1 = makeGaussianKernel(12)
    print(k1)
    print("===================")
    

if __name__ == "__main__":
    testHybrid()