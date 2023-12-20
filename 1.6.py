import matplotlib.pyplot as plt
import numpy as np
import cv2

#trnslating matrix of HHQ
#shifting by (100,50)
M = np.float32([[1, 0, 100], [0 , 1, 50]])
try:
    Q1 = cv2.imread(r"C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\bt\bt hh.tif")
    HHQ_T = cv2.warpAffine(Q1, M, (100, 50))
    cv2.imwrite("HHQ_T.tiff", Q1)
    plt.imshow(HHQ_T)
    plt.title("Translated HHQ")
    plt.show()
except IOError:
    print("error")

#trnslating matrix of HvQ
try:
    Q1 = cv2.imread(r"C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\bt\bt hv.tif")
    HVQ_T = cv2.warpAffine(Q1, M, (100, 50))
    cv2.imwrite("HVQ_T.tiff", Q1)
    plt.imshow(HVQ_T)
    plt.title("Translated HVQ")
    plt.show()
except IOError:
    print("error")