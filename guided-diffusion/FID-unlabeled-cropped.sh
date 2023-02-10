#!/bin/bash

echo "Bash version ${BASH_VERSION}..."

#echo train vs val
#python -m pytorch_fid D:/Simula_data/unlabeled-dataset-128x128/val/unlabeled_128 D:/Simula_data/unlabeled-dataset-128x128/train/unlabeled_128

for i in {050000..500000..050000}
do
  echo Model nr: $i
  python -m pytorch_fid unlabeled-dataset-128x128/val/masked_images C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated_unlabeled_cropped/$i
done