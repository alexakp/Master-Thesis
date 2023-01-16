from numpy import load
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import sys
import os

classcond = False

data = ('D:\Simula_data\Models\Temp\openai-2023-01-15-00-23-49-646190')
print(data)
log_file = data + '\log.txt'


model_nr = 'NAN'
with open(log_file) as f:
    lines = f.readlines()
    model_nr = (lines[1].split('ema_0.9999_', 1)[1])
model_nr = (model_nr.split('.pt', 1)[0])
print(model_nr)

data = data +'\samples_100x128x128x3.npz'


data = load(data)
print(data)


lst = data.files

if(classcond):
    imgs = data[lst[0]]

    obj = imgs.shape[0]
    for i in range(obj):
        img = imgs[i]
        img = Image.fromarray(img.astype('uint8'), 'RGB')
        img.save(f'generated_dataset/250_respace/img_class_cond_{i}_class_{data[lst[1]][i]}.png')
        #plt.figure()
        #plt.imshow(img, interpolation='none')
        #plt.show()
    #plt.show()

else:

    try: 
        os.mkdir(f"C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_dataset/{model_nr}_32_flip")
    except OSError as error: 
        print(error)  

    print(data[lst[0]].shape)
    for item in lst:
        print(data[item].shape)
        data = data[item]
        obj = data.shape[0]
        print(obj)
        for i in range(obj):
            img = data[i]
            img = Image.fromarray(img.astype('uint8'), 'RGB')
            img.save(f"C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_dataset/{model_nr}_32_flip/img_{i}.png")
            #plt.figure()
            #plt.imshow(img, interpolation='none')
            #plt.show()
        #plt.show()