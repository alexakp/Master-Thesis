from numpy.random import randint
import numpy as np
import cv2
import torchvision
import torch
import torch.nn as nn
from PIL import Image
import os
import sys
import albumentations

def cover_img(img,mask):
    polyp_cropped = img.copy()
    for x in range(mask.shape[0]):
        for y in range(mask.shape[1]):
            if (mask[x,y] > 128):
                img[x,y] = [255]*3 # rgb, white color
            elif(mask[x,y]< 128):
                polyp_cropped[x,y] = [255]*3
    return img, polyp_cropped

"""def random_mask(height, width, channels = 3):
    img = np.zeros((height, width, channels), np.uint8)
    
    # Set scale
    size = int((width + height) * 0.007)
    if width < 64 or height < 64:
        raise Exception("Width and Height of mask must be at least 64")
    
    # Draw Random Lines
    for _ in range(randint(1, 20)):
        x1, x2 = randint(1, width), randint(1, width)
        y1, y2 = randint(1, height), randint(1, height)
        thickness = randint(1, size)
        cv2.line(img, (x1, y1), (x2, y2), (1, 1, 1), thickness)
    
    # Draw Random Circles
    for _ in range(randint(1, 20)):
        x1, y1 = randint(1, width), randint(1, height)
        radius = randint(1, size)
        cv2.circle(img, (x1, y1), radius, (1, 1, 1), -1)
    
    # Draw Random Ellipses
    for _ in range(randint(1, 20)):
        x1, y1 = randint(1, width), randint(1, height)
        s1, s2 = randint(1, width), randint(1, height)
        a1, a2, a3 = randint(1, 180), randint(1, 180), randint(1, 180)
        thickness = randint(1, size)
        cv2.ellipse(img, (x1, y1), (s1, s2), a1, a2, a3, (1, 1, 1), thickness)

    return 1 - img
"""     
def save_image_from_dataloader3c(image,imagesavefolder,prefix,indx):
    inv_aug = albumentations.Compose(
            [
                albumentations.Normalize(mean=(-0.55716495/0.31903088,-0.32165295/0.22265271,-0.23576912/0.18867239),
                std=(1/0.31903088,1/0.22265271,1/0.18867239), max_pixel_value=1, always_apply=True),
            ]
        )
    image=image.cpu()
    image = torchvision.utils.make_grid(image)
    image = np.transpose(image.numpy().astype(np.float),(1,2,0))
    image2 = inv_aug(image=image)["image"]
    image=(image+1)/2 # [0.1] after this
    image=(image*255).astype(np.uint8)
    image2 = (image2*255).astype(np.uint8)

    image_pil=Image.fromarray(image2.astype(np.uint8))
    image=(image*255).astype(np.uint8)
    #image_pil=Image.fromarray(image)
    image_pil=Image.fromarray(image2.astype(np.uint8))
    image_pil.save(os.path.join(imagesavefolder,f"{prefix}_{indx}.jpg"))