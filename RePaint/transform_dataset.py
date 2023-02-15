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
files = glob.glob("D:/Simula_data/hyper-kvasir/unlabeled-images/images/*.jpg", recursive=True)
for path in files:
   img = preprocess(Image.open(path))
   name = path.split('\\', 1)
   imgs = name[1].split('\\',1)
    ### MASKS should be mono either 255 or 0.

   img.save(f'D:/Simula_data/unlabeled_128/{imgs[0]}')