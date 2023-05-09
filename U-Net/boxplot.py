import cv2
import glob
from PIL import Image
import numpy as np
from numpy import asarray
from matplotlib import pyplot as plt
import sys
import csv
import scipy.stats as stats

IoU = []
mIoU = []
DSC = []




#markers = ['o','^']
name = 'CVC'
with open(f'data-boxplot-{name}.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for  i in range(len(row)):
                if(i==1):
                    IoU.append(round(float(row[i]),3))
                elif(i==2):
                    mIoU.append(round(float(row[i]),3))
                elif(i==3):
                    DSC.append(round(float(row[i]),3))


            line_count += 1



print(stats.ttest_ind(a=IoU[5:], b=IoU[:5]))
print(stats.ttest_ind(a=mIoU[5:], b=mIoU[:5]))
print(stats.ttest_ind(a=DSC[5:], b=DSC[:5]))

print(mIoU[5:])
print(mIoU[:5])

print(mIoU)

data = [IoU[5:], IoU[:5]] 
fig = plt.figure(figsize =(6, 5)) 

plt.boxplot(data)
plt.xticks([1, 2], ['Real','Mix'], size=28)
plt.yticks(np.arange(np.min(data), np.max(data), 0.01),size=28)
#plt.title('IoU', size=28)
plt.tight_layout()
plt.savefig(f"boxplots/{name}-IoU.eps")

#plt.show()


data = [mIoU[5:], mIoU[:5]] 
fig = plt.figure(figsize =(6, 5)) 

plt.boxplot(data)
plt.xticks([1, 2], ['Real','Mix'], size=28)
plt.yticks(np.arange(np.min(data), np.max(data), 0.03),size=28)
#plt.title('mIoU', size=28)
plt.tight_layout()
plt.savefig(f"boxplots/{name}-mIoU.eps")

#plt.show()

data = [DSC[5:], DSC[:5]] 
fig = plt.figure(figsize =(6, 5)) 

plt.boxplot(data)
plt.xticks([1, 2], ['Real','Mix'], size=28)
plt.yticks(np.arange(np.min(data)-0.001, np.max(data), 0.014),size=28)
#plt.title('DSC', size=28)
plt.tight_layout()
plt.savefig(f"boxplots/{name}-DSC.eps")


plt.show()
