import glob
import random


files = glob.glob("transformed_dataset_128/images/*.png", recursive=True)
random.shuffle(files)


i = 0
for filen in files:

    name = filen.split('\\', 1)
    print(f'"{name[1]}" OR ',end='')
    i+=1
    if(i%8==0):
        input()
        print()
print(f'\n{i}')
