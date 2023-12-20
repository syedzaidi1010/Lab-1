from rasterio.plot import show
from PIL import Image


# reading tiff file
Q1 = Image.open(r"C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\bt\bt hh.tif")
Q2 = Image.open(r"C:\Users\ASFAR\Desktop\DIP Labs\MyLabs\bt\bt hv.tif")
show(Q1)
pixels = Q1.load()
show(Q2)
pixels = Q2.load()