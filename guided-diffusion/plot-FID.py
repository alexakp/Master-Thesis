import matplotlib.pyplot as plt
import numpy as np

import csv

y_1 = []
y_2 = []

x_1 = []
x_2 = []

with open('C:/Users/Alexander-PC-hjemme/Desktop/FID-unlabeled.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count < 2:
            line_count += 1
        else:
            x_1.append(int(row[0]))
            y_1.append(float(row[1]))
            x_2.append(int(row[3]))
            y_2.append(float(row[4]))
            line_count += 1


print(y_1)
plt.plot(x_1, y_1, label = "Linear")
plt.plot(x_2, y_2, label = "Cosine")
plt.legend()
plt.show()