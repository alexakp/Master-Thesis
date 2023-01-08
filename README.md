# Master Thesis for Image Synthesis 

## ~~GAN and~~ Diffusion models 
- ~~Pix2Pix (GAN) (probably not gonna be used)~~ 
- Diffusion based models, to see how to train a custom dataset look at https://github.com/openai/improved-diffusion

# Step-by-step guide for the methodology used (Training)

1. Prepare the data you want to generate we have used 1000 polyp images from Kvasir-SEG with only polyps and black background. One dataset for polyp images and one dataset for clean colon images.
2. Train diffusion model on polyp data to generate realistic-looking polyps with a black background, we can then create a corresponding mask easily with thresholding. Create a synthetic polyp dataset.
3. Train diffusion model on clean colon data which will be used to inpaint the background for our generated polyps.
4. Feed the synthetic polyp dataset and clean colon diffusion model into the RePaint framework. 

## Diffusion of polyp using 1000 steps with DDPM.
![](diffusion_looped.gif)

# Old section

## Diffusion of polyp using 250 steps, and 148 interpolated images between noise img1 and noise img 2 (total 150 images).
![](polyp.gif) 
