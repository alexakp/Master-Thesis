import glob
import sys
import numpy as np
from PIL import Image

def invert_color(mask):
    val = []
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if(mask[i,j]):
                mask[i,j] = 255
            else:
                mask[i,j] = 0
    #print(np.mean(val, axis=(0)))
    #print(np.std(val, axis=(0)))
    return mask

#images = glob.glob("transformed_dataset_128/images/*.png")
masked = glob.glob("random-HyperKvasir-samples/masked/*.png")
#print(len(images))
print(len(masked))

i = 0
for mask in (masked):
    path = mask.split('\\', 1)
    
    mask = np.array(Image.open(mask).convert('L'))
    cropped_polyp = invert_color(mask)
    im = Image.fromarray(cropped_polyp)
    im.save("random-HyperKvasir-samples/masks/"+path[1])
    
sys.exit()