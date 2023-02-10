#!/bin/bash


for i in {002000..020000..2000}
do
  #echo Model nr: $i
  python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated-fine-tuned-best-pre/$i
done
