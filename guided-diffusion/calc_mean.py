from numpy import load
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import sys
from torchvision import transforms

img =  np.array(Image.open('New Project (1).png').convert('RGB'))


def calc_mean_and_std(img):
    val = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if((img[i,j]!=0).all()):
                val.append(img[i,j])
    print(np.mean(val, axis=(0)))
    print(np.std(val, axis=(0)))

#print(np.mean(img, axis=(0, 1)))
#print(np.std(img, axis=(0,1)))


print(img.shape)
calc_mean_and_std(img)