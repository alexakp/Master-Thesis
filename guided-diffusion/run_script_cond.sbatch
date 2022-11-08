#!/bin/sh

#SBATCH -t 13-23:59
#SBATCH -p dgx2q
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

MODEL_FLAGS="--image_size 128 --num_channels 128 --num_heads 4 --num_res_blocks 2 --class_cond True --learn_sigma True --resblock_updown True --use_fp16 True --use_scale_shift_norm True"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False"
TRAIN_FLAGS="--lr 1e-4 --batch_size 32"

srun python scripts/image_train.py --data_dir class_cond_images $MODEL_FLAGS $DIFFUSION_FLAGS $TRAIN_FLAGS