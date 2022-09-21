#!/bin/sh

#SBATCH -t 13-23:59
#SBATCH -p dgx2q
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

MODEL_FLAGS="--image_size 64 --num_channels 128 --num_res_blocks 3 --learn_sigma True"
DIFFUSION_FLAGS="--diffusion_steps 4000 --noise_schedule cosine"
TRAIN_FLAGS="--lr 1e-4 --batch_size 32"

srun python scripts/image_train.py --data_dir images $MODEL_FLAGS $DIFFUSION_FLAGS $TRAIN_FLAGS