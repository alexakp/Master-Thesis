import os
import warnings

import torch
from torchvision import datasets
from torchvision import io
from torchvision import models
from torchvision import ops
from torchvision import transforms
from torchvision import utils
import glob
import sys



import torchvision.transforms as T

from PIL import Image
from matplotlib import pyplot as plt

#img = Image.open('images/cju0qkwl35piu0993l0dewei2.jpg')

preprocess = T.Compose([
   T.Resize(128),
   T.CenterCrop(128),
])

#x = preprocess(img)
files = glob.glob("D:\Simula_data\hyper-kvasir\labeled-images\lower-gi-tract\\anatomical-landmarks\cecum/**/*.jpg", recursive=True)
for path in files:
   img = preprocess(Image.open(path))
   name = path.split('\\', 1)
   imgs = name[1].split('\\',1)
   imgs[1] =  imgs[1].split('.jpg', 1)[0]
   imgs[1] =  imgs[1].split('cecum\\', 1)[1]
    ### MASKS should be mono either 255 or 0.
   if(imgs[0]=='masks'):
      threshold = 128
      image_file = img.convert('L')
      # Threshold
      image_file = image_file.point( lambda p: 255 if p > threshold else 0 )
      img = image_file.convert('1')
   # save as png and not jpg to avoid compression for pixel values
   img.save(f'transformed_dataset_128_cecum/{imgs[1]}.png')