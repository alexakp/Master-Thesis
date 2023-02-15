#!/bin/bash

echo "Bash version ${BASH_VERSION}..."
for i in {002000..020000..2000}
do
  echo Model nr: $i
  python -m pytorch_fid D:/Simula_data/transformed_clean_train_val/val C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_fine-tuned-clean-0.3-dropout/$i
done
# python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_fine-tuned_2000_step/002000


