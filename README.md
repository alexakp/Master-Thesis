# Master Thesis for Image Synthesis 

## ~~GAN and~~ Diffusion models :heart:
- ~~Pix2Pix (GAN)~~ :satisfied::wave: 
- Diffusion based models, to see how to train a custom dataset look at https://github.com/openai/improved-diffusion

## Datasets used
https://datasets.simula.no/hyper-kvasir/
### Unlabeled part of Hyper-Kvasir 99,417 :raised_hands:
### Kvasir-SEG 1000 polyp images with their corresponding mask :mag_right:

# Step-by-step guide for generating complete polyp images

We hold out 4971 unlabeled images and 200 polyps that we use in step 2 and 4 to compute FID.

1. We train our diffusion model on a large part of the unlabeled dataset in Hyperkvasir.

2. Generate samples and pick the model with best FID(Cosine 500K - 25.66).

3. Fine tune the model on 800 polyp images from Kvasir-SEG.

4. Pick the model with best FID score(0.3 dropout 26K - 80.55).

5. Compare our generated polyp images against Kvasir-SEG polyp images that are downsampled to 128x128 and center cropped.

## Polyp Images 128x128
Our best model generated polyps             |  Real polyp images from Kvasir-SEG 
:-------------------------:|:-------------------------:
![](github-images/our_polyps.png)  |  ![](github-images/kvasir_polyps.png)

Link to all our generated images from 026000 model: https://www.dropbox.com/sh/3iz0rirrn9k22f3/AABZn4EA7Lb3BW4ocb8ect2qa?dl=0

## Diffusion of polyp using 1000 steps with DDPM.
![](github-images/fp_out2.gif)