import cv2
import glob
import itertools
from PIL import Image
import sys
import numpy


for x in range(80):
    model_nr = '050000'
    in_img = f"log\inpaint_anatomical-and-pathological\inpainted\img_{x}.png"
    template = cv2.imread(in_img, 0)
    template_horz = cv2.flip(template,1)
    files = glob.glob("transformed_dataset_128_cecum/*.png")

    max_conf = 0
    out_name = ""
    name_score = {}
    for name in files:
        img = cv2.imread(name, 0)
        name_score[name] = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED).max()
        if (cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED).max() > max_conf):
            max_conf = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED).max()
            out_name = name
        if (cv2.matchTemplate(img, template_horz, cv2.TM_CCOEFF_NORMED).max() > max_conf):
            max_conf = cv2.matchTemplate(img, template_horz, cv2.TM_CCOEFF_NORMED).max()
            out_name = name
            name_score[name] = cv2.matchTemplate(img, template_horz, cv2.TM_CCOEFF_NORMED).max()

    sorted_x = dict(sorted(name_score.items(), key=lambda item: item[1]))
    sorted_x = dict(reversed(sorted_x.items()))
    N = 5
    top_N = dict(itertools.islice(sorted_x.items(),N))
    keysList = list(top_N.keys())
    """
    # Print only orginal name of imgs
    ch = 'clean_'
    for item in keysList:
        listOfWords = item.split(ch, 1)
        print(listOfWords[1])
    print(keysList)"""
    print('---------------')
    print(max_conf)
    print(out_name)
    print(top_N)
    print(f'File number: {x}')
    print(f'log\inpaint_anatomical-and-pathological\inpainted/img_{x}.png')