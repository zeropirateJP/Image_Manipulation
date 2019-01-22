import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

pic = Image.open('img.png')
par = np.array(pic)
print (par)
plt.imshow(par)
plt.show()




