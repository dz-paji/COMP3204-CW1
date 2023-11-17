import numpy as np

def convolve(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """
    Convolve an image with a kernel assuming zero-padding of the image to handle the borders
    :param image: the image (either greyscale shape=(rows,cols) or colour shape=(rows,cols,channels))
    :type numpy.ndarray
    :param kernel: the kernel (shape=(kheight,kwidth); both dimensions odd)
    :type numpy.ndarray
    :returns the convolved image (of the same shape as the input image)
    :rtype numpy.ndarray
    """
    # Your code here. You'll need to vectorise your implementation to ensure it runs
    # at a reasonable speed.
    if len(image.shape) == 2:
        img_w, img_h = image.shape
        c = 1
        # # flips the kernel horizontally and vertically
        # k_w, k_h = kernel.shape
        # fliped_kernel = np.copy(kernel)
        # for i in range(k_w):
        #     for j in range(k_h):
        #         fliped_kernel[j, i] = kernel[k_w - 1 - j, k_h - 1 - i]    
        # k_w_half = k_w // 2
        # k_h_half = k_h // 2
    
        # # do zero paddings to the input image
        # padded = np.zeros((img_w + k_w, img_h + k_h))
        # padded[k_w_half:(k_w_half + img_w), k_h_half:(k_h_half + img_h)] = image
        # convolved = np.copy(padded)

        # # print(kernel.shape)
        # # print(padded.shape)
        # # print(image.shape)

        # for i in range(img_w):
        #     for j in range(img_h):
        #         # Get the image patch
        #         # print(i, j)
        #         window = padded[i:i + k_h, j:j + k_w]
            
        #         convolved[i, j] = np.sum(window * kernel)
            
        # chopped = convolved[k_w_half:(k_w_half + img_w), k_h_half:(k_h_half + img_h)]
        # return chopped

    else:
        img_w, img_h, c = image.shape
        # flips the kernel horizontally and vertically

    k_w, k_h = kernel.shape
    fliped_kernel = np.copy(kernel)
    for i in range(k_w):
        for j in range(k_h):
            fliped_kernel[j, i] = kernel[k_w - 1 - j, k_h - 1 - i]    
    k_w_half = k_w // 2
    k_h_half = k_h // 2

    padded = np.zeros((img_w + k_w, img_h + k_h, c))
    
    for k in range(c):
        padded[k_w_half:(k_w_half + img_w), k_h_half:(k_h_half + img_h), k] = image[:, :, k]
        
    convolved = np.zeros((img_w, img_h, c))

    for k in range(c):
        for i in range(img_w):
            for j in range(img_h):
                # Get the image patch
                # print(f"image size: {image.shape}, padded size: {padded.shape}, i: {i}, j: {j}")
                window = padded[i:i + k_w, j:j + k_h, k]
                convolved[i, j, k] = np.sum(window * kernel)
                # if convolved[i, j, k] > 255:
                #     print(f"convolved[i, j, k] > 255: {convolved[i, j, k]}")
            
        
    # chopped = convolved[k_w_half:(k_w_half + img_w), k_h_half:(k_h_half + img_h), :]
    # if (convolved.shape != image.shape):
    #     print("convolved.shape != image.shape")
    #     print(convolved.shape)
    #     print(image.shape)
    #     raise RuntimeError("convolved.shape != image.shape")
    return convolved
        
            
