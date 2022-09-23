import glob
import os
from os.path import basename, splitext
if __name__ == '__main__':
    imageFile = glob.glob("/home/nsl50/Desktop/tanvir/json_augmentation/Augmentated_Image/*.")
    l = len(imageFile)
    for i in range(l):                          
        imageName = imageFile[i]
        a, b, c, d, e = imageName.split('.jpg')

        if d == 'pre':
            d = '' # Replace with string you require
            os.rename(imageName, "/path_to_folder/" + a + "_" + b + "_" + c + "_" + d + e)