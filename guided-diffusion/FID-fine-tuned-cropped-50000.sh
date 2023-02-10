#!/bin/bash

echo "Bash version ${BASH_VERSION}..."
for i in {005000..050000..5000}
do
  echo Model nr: $i
  python -m pytorch_fid D:/Simula_data/Images_data/cropped/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_fine-tuned-cropped-50000/$i
done
# python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_fine-tuned_2000_step/002000


