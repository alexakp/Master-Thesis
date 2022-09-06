import numpy as np
import cv2
 
from pathlib import Path
 
imageFilesDir = Path(r'Kvasir-SEG/images')
files = list(imageFilesDir.rglob('*.jpg'))
 
print(len(files))
 
mean = np.array([0.,0.,0.])
stdTemp = np.array([0.,0.,0.])
std = np.array([0.,0.,0.])
 
numSamples = len(files)
 
for i in range(numSamples):
    im = cv2.imread(str(files[i]))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im = im.astype(float) / 255.
     
    for j in range(3):
        mean[j] += np.mean(im[:,:,j])
       
mean = (mean/numSamples)
 
print(mean) #[0.55716495 0.32165295 0.23576912]

for i in range(numSamples):
    im = cv2.imread(str(files[i]))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    im = im.astype(float) / 255.
    for j in range(3):
        stdTemp[j] += ((im[:,:,j] - mean[j])**2).sum()/(im.shape[0]*im.shape[1])
 
std = np.sqrt(stdTemp/numSamples)
 
print(std) #[0.31903088 0.22265271 0.18867239]