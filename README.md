# Master Thesis for image synthesis 

## GAN and Diffusion models 
- Pix2Pix (GAN) (probably not gonna be used) 
- Guided Diffusion, to see how to train a custom dataset look at https://github.com/openai/improved-diffusion

# Step-by-step guide for the methodology used (Training)

1. Prepare the data you want to generate we have used 1000 polyp images from Kvasir-SEG with only polyps and black background. One dataset for polyp images and one dataset for clean colon images.
2. Train diffusion model on polyp data to generate realistic-looking polyps with a black background, we can then create a corresponding mask easily with thresholding. Create a synthetic polyp dataset.
3. Train diffusion model on clean colon data which will be used to inpaint the background for our generated polyps.
4. Feed the synthetic polyp dataset and clean colon diffusion model into the RePaint framework. 

# Deprecated section

## Diffusion of polyp using 1000 steps (not looped).
![](fp_out2.gif)

## Diffusion of polyp using 250 steps, and 148 interpolated images between noise img1 and noise img 2 (total 150 images).
![](polyp.gif)


## Update after meeting 16.11.2022

D:/Simula_data/Models/Temp/openai-2022-11-14-23-44-04-807734/ema_0.9999_020000.pt is an example of a diffusion model only trained on clean images. 
