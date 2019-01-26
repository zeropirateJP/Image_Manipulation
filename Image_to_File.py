from PIL import Image
import numpy as np

def export_Image():
    image_dict = open("Pixcel_collections.txt",'a')
    numbers = range(0,10)
    versions = range(1,10)
    for eachNumber in numbers:
        for eachVersion in versions:
            #print str(eachNumber) + (".") + str(eachVersion)
            file_name = "numbers/" + str(eachNumber) + (".") + str(eachVersion) + ".png"
            pic = Image.open(file_name)
            picArray = np.asarray(pic)
            picArray = str(picArray.tolist())
            image_index = str(eachNumber) + "::" + picArray +"\n"
            image_dict.write(image_index)
            #print picArray

export_Image()