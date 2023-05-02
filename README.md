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

 ## Interpolation 
To interpolate between two images using your DDPM can you use the following flags in the guided-diffusion folder. Make sure you use the same flags as the model you trained, for example same amount attention_resolutions etc. --rescale_timesteps needs to be True. Interpolation should create 99 images a example of interpolation between two polyps is shown below with t intervals of [0,125,250,375,500,625,750,875,999]. Images from left to right are [reconstructed src1, λ=0.1,λ=0.2,...,λ=0.9,reconstructed src2]
```
MODEL_FLAGS="--attention_resolutions 32,16,8 --image_size 128 --num_channels 128 --num_heads 4 --num_res_blocks 2 --learn_sigma True --resblock_updown True --use_fp16 True --use_scale_shift_norm True"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps True --interpolate True --src1 images/img1.jpg --src2 images/img2.jpg"

python scripts/image_sample.py --model_path your/model/path.pt $MODEL_FLAGS $DIFFUSION_FLAGS
 
```
![](github-images/interpolation/interpolation-collage.jpg)

# Polyps with masks

## Validation 200 Kvasir-SEG images
| Dataset  | IoU            | mIoU           | DSC            | Precision      | Recall         |
|----------|----------------|----------------|----------------|----------------|----------------|
| Baseline | 0.762          | 0.732          | 0.840          | 0.871          | 0.821          |
| +800     | **0.785** | **0.766** | **0.857** | **0.913** | **0.826** |


## Validation ETIS Larib Polyp DB
| Dataset  | IoU            | mIoU           | DSC            | Precision      | Recall         |
|----------|----------------|----------------|----------------|----------------|----------------|
| Baseline | 0.351          | 0.470          | 0.408          | 0.583          | 0.709          |
| +800     | **0.396** | **0.492** | **0.451** | **0.604** | **0.727** |

## Validation CVC-ClinicDB 
| Dataset  | IoU            | mIoU          | DSC            | Precision      | Recall         |
|----------|----------------|---------------|----------------|----------------|----------------|
| Baseline | 0.642          | 0.628         | 0.735          | 0.831          | 0.720          |
| +800     | **0.654** | **0.66** | **0.738** | **0.869** | **0.733** |

## Polyp Images 128x128
Generated polyp images             |  Real polyp images from Kvasir-SEG 
:-------------------------:|:-------------------------:
![](github-images/Generated/images/img_90.png) ![](github-images/Generated/masks/img_90.png) | ![](github-images/Kvasir-SEG/images/cju2s9g11pnra0993gn4eh793.png) ![](github-images/Kvasir-SEG/masks/cju2s9g11pnra0993gn4eh793.png)
 ![](github-images/Generated/images/img_102.png) ![](github-images/Generated/masks/img_102.png) | ![](github-images/Kvasir-SEG/images/cju5wqonpm0e60801z88ewmy1.png) ![](github-images/Kvasir-SEG/masks/cju5wqonpm0e60801z88ewmy1.png)
 ![](github-images/Generated/images/img_184.png) ![](github-images/Generated/masks/img_184.png) | ![](github-images/Kvasir-SEG/images/cju8a1jtvpt9m081712iwkca7.png) ![](github-images/Kvasir-SEG/masks/cju8a1jtvpt9m081712iwkca7.png)
 
