from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

style.use("fivethirtyeight")
test_Image = Image.open("9.3.png",'r')
test_iar = np.array(test_Image)
balancedArray =[]
def threshold(imageArray):
    newImageArray = imageArray
    for eachRow in imageArray:

         for eachPixel in eachRow:
            #print(eachPixel)
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

threshold_img = threshold(test_iar)
threshold_img = str(threshold_img.tolist())
#print threshold_img
final_img = threshold_img.split("],")
#print final_img

image_dict = open("Pixcel_collections.txt",'r').read()
image_dict = image_dict.split("\n")
match= []

for eachLine in image_dict:
    if len(eachLine) > 3:
        splited = eachLine.split("::")
        digit = splited[0]
        pixcels = splited[1]

        eachPixcel = pixcels.split("],")
        #print len(eachPixcel)
        #print eachPixcel[0]
        #print final_img[0]

        x= 0
        while(x< len(eachPixcel)):
           # print eachPixcel[x]
            if eachPixcel[x] == final_img[x]:
                match.append(int(digit))
            x +=1
        #print x
counts = Counter(match)
print counts

x_axis =[]
y_axis =[]
for eachPixcel in counts:
    #print eachPixcel
    x_axis.append(eachPixcel)
    y_axis.append(counts[eachPixcel])
    #print counts[eachPixcel]

fig =plt.figure()

axis1 = fig.add_subplot(211)
axis2 = fig.add_subplot(212)
#axis1.legend("Given Image")
#axis2.legend("OCR Prediction")
#plt.ylim(400)
x_points = plt.MaxNLocator(12)
axis2.xaxis.set_major_locator(x_points)
axis1.imshow(test_iar,label="Given Image")
axis2.bar(x_axis,y_axis,label="OCR Prediction")
axis2.set_ylim(350)
axis1.legend()
axis2.legend()
plt.show()

#a =one[1].split("],")
#print one[0]
#print len(eachPixcel)

