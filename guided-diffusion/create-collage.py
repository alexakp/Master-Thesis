from PIL import Image
import glob


files = glob.glob("generated-intepolation/*.jpg")
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

files.sort(key=natural_keys)

def create_collage(width, height, listofimages):
    cols = 11
    rows = 9
    thumbnail_width = width//cols
    thumbnail_height = height//rows
    size = thumbnail_width, thumbnail_height
    new_im = Image.new('RGB', (width, height))
    ims = []
    for p in listofimages:
        im = Image.open(p)
        im.thumbnail(size)
        ims.append(im)
    i = 0
    x = 0
    y = 0
    for row in range(rows):
        for col in range(cols):
            new_im.paste(ims[i], (y, height-thumbnail_height-x))
            i += 1
            y += thumbnail_height
        x += thumbnail_width
        y = 0

    new_im.save("Collage.jpg")

create_collage(1408, 1152, files)