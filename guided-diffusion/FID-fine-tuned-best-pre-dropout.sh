#!/bin/bash


for i in {002000..040000..2000}
do
  #echo Model nr: $i
  python -m pytorch_fid D:/Simula_data/Images_data/images/polyps-3 C:/Users/Alexander-PC-hjemme/Desktop/UiO/Master_Thesis/guided-diffusion/generated-fine-tuned-best-pre-0.3-dropout/$i
done
