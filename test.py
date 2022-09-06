from PIL import Image
import numpy as np
from matplotlib import pyplot as plt

def cover_img(img,mask):
    polyp_cropped = img.copy()
    for x in range(mask.shape[0]):
        for y in range(mask.shape[1]):
            if (mask[x,y] > 128):
                img[x,y] = [255]*3 # rgb, white color
            elif(mask[x,y]< 128):
                polyp_cropped[x,y] = [255]*3
    return img, polyp_cropped



if __name__ == '__main__':

    # TO GET ALL IMAGES ONE FOR LOOP AND USE GLOB MODULE...
    # https://stackoverflow.com/questions/26392336/importing-images-from-a-directory-python-to-list-or-dictionary

    im = Image.open("Kvasir-SEG\images\cju0qkwl35piu0993l0dewei2.jpg")
    mask = np.asanyarray(Image.open("Kvasir-SEG\masks\cju0qkwl35piu0993l0dewei2.jpg").convert('L'))
    # print(np.unique(mask)) # OUTPUT [  0   1   2   3   4   5   6   7   8 247 248 249 250 251 252 253 254 255]

    img_array = np.asarray(im)
    covered_img, polyp_cropped = cover_img(img_array, mask)
    
    covered_img = Image.fromarray(covered_img)
    covered_img.save('out_imgs/covered_img.png')

    polyp_cropped = Image.fromarray(polyp_cropped)
    polyp_cropped.save('out_imgs/polyp_cropped.png')

    fig = plt.figure(figsize=(10, 7))
    fig.add_subplot(2, 2, 1)

    plt.imshow(im)
    plt.title('Original Image')

    fig.add_subplot(2, 2, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('Mask')

    fig.add_subplot(2, 2, 3)
    plt.imshow(covered_img)
    plt.title('Masked Image')

    fig.add_subplot(2, 2, 4)
    plt.imshow(polyp_cropped)
    plt.title('Polyp')

    plt.show()
  