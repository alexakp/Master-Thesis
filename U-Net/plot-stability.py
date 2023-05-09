import cv2
import glob
from PIL import Image
import numpy as np
from numpy import asarray
from matplotlib import pyplot as plt
import sys
import csv

"""with open('potenial_models/basev2.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} {row[1]}')
            line_count += 1
    print(f'Processed {line_count} lines.')"""



files = ['base','base+800']
markers = ['o','^']
for items,marker in zip(files,markers):
    black_images =[]
    x_range = []
    with open(f'etis-validation/{items}.csv') as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=',')
         line_count = 0
         for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                #row = row[1].split('(', 1)
                #row = row[1].split(')', 1)
                row = row[3]
                print(f'\t{row}')
                print(line_count-2)
                line_count += 1
                x_range.append(line_count-2)
                #black_images.append(float(row[0]))
                black_images.append(float(row))

    plt.plot(x_range,black_images, marker=marker)
plt.xlabel('Epochs')
plt.ylabel('Dice Score')
plt.xticks(np.arange(min(x_range), max(x_range)+1, 2.0))
plt.legend(files, loc ="lower right")
plt.savefig("etis-validation/DICE-etis.png")
plt.show()
