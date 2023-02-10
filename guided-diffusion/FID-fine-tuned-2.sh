#!/bin/bash

echo 800 real images vs 200 real images
python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 D:/Simula_data/Images_data/images/polyps-1
#echo Unlabeled images 150 000
#python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_unlabeled/150000
#echo Unlabeled images 500 000
#python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_unlabeled/500000

for i in {002000..016000..2000}
do
  echo Model nr: $i
  python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_fine-tuned_2000_step/$i
done

echo Model nr: 020000
python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_fine-tuned/020000
echo Model nr: 030000
python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_fine-tuned/030000
echo Model nr: 040000
python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_fine-tuned/040000
echo Model nr: 050000
python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_fine-tuned/050000