import matplotlib.pyplot as plt
import cv2

#RGB of HHQ
Q1 = cv2.imread(r"C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\bt\bt hh.tif")
HHQ_rgb =cv2.cvtColor(Q1, cv2.COLOR_BGR2RGB)
plt.imshow(HHQ_rgb)
plt.axis('off')
plt.title("RGB of HHQ")
plt.show()

#RGB of HVQ
Q2 = cv2.imread(r"C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\bt\bt hv.tif")
HVQ_rgb =cv2.cvtColor(Q2, cv2.COLOR_BGR2RGB)
plt.imshow(HVQ_rgb)
plt.axis('off')
plt.title("RGB of HVQ")
plt.show()