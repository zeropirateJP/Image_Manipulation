from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time

pic = Image.open("tick.png")
iar =  np.array(pic)
balancedArray =[]
def threshold(imageArray):
    newImageArray = imageArray
    for eachRow in imageArray:
        for eachPixel in eachRow:
         for eachPixel in eachRow:
            print(eachPixel)
            #print len(eachPixel[:3])
            # adding RGB and averaging for each pixel in a row
            avg = int(reduce(lambda x,y:x+y,eachPixel[:3]/len(eachPixel[:3]))) #pixels are uint8 data type and cant go beyond 255
            balancedArray.append(avg)
            #print (avg)
            #time.sleep(500)
    #print balancedArray
    # average value
    balance = reduce(lambda x,y: x+y , balancedArray)/len(balancedArray)
    #print balance

    #assigning 0 and 1 to new image array using the threshold
    for eachRow in newImageArray:
        for eachPixel in eachRow:
            if reduce(lambda x,y:x+y,eachPixel[:3]/len(eachPixel[:3])) > balance:
                eachPixel[:3] = 255
            else:
                eachPixel[:3] = 0
    return newImageArray
final_pic = threshold(iar)
#print iar
plt.imshow(final_pic)
plt.show()