import cv2
import glob
from PIL import Image
import numpy as np
from numpy import asarray
from matplotlib import pyplot as plt
import sys





dropout = ['0','0.1','0.3']
markers = ['o','^','s']
marker = 0
for drops in dropout:
    black_images =[]
    x_range = []
    for int_i in range(30001):
        if(int_i%2000==0 and int_i!=0):
            x_range.append(int_i)
            model_nr = f"{int_i:06d}" 
            #print(model_nr)
            folder_ = f'generated-fine-tuned-cropped-{drops}-dropout'

            images = [asarray(Image.open(image).convert('L')) for image in glob.glob(f"{folder_}/{model_nr}/*.png")]

            names = [image for image in glob.glob(f"{folder_}/{model_nr}//*.png")]


            i=0
            for img,name in zip(images,names):
                mean = np.mean(img, axis=(0, 1))
                if (mean==0):
                    i+=1

            print(f"Total images that generates black image and not polyp: {i}")
            black_images.append(((i)*100)/len(names))
    plt.plot(x_range,black_images, marker=markers[marker],)
    marker+=1
plt.ylabel('% Failure')
plt.xlabel('Iterations')
plt.legend(["0 dropout","0.1 dropout", "0.3 dropout"], loc ="upper right")
plt.savefig("black-images.eps")
plt.savefig("black-images.png")
plt.show()

sys.exit()
dropout = ['0.3']
for drops in dropout:
    black_images =[]
    x_range = []
    model_nr = f"018000" 
    #print(model_nr)
    folder_ = f'generated-fine-tuned-cropped-{drops}-dropout'

    images = [asarray(Image.open(image).convert('L')) for image in glob.glob(f"{folder_}/{model_nr}/*.png")]

    names = [image for image in glob.glob(f"{folder_}/{model_nr}//*.png")]


    i=0
    for img,name in zip(images,names):
        mean = np.mean(img, axis=(0, 1))
        if (mean<0.01):
            i+=1
            print(name)

    print(f"Total images that generates black image and not polyp: {i}")
sys.exit()