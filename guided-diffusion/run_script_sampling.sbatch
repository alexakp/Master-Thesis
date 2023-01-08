#!/bin/sh

#SBATCH -t 13-23:59
#SBATCH -p dgx2q
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear"
MODEL_FLAGS="--image_size 128 --num_channels 128 --num_heads 4 --num_res_blocks 2 --learn_sigma True --resblock_updown True --use_fp16 True --use_scale_shift_norm True --rescale_learned_sigmas False"


srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2022-11-12-20-15-52-059253/ema_0.9999_090000.pt $MODEL_FLAGS $DIFFUSION_FLAGS
srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2022-11-12-20-15-52-059253/ema_0.9999_100000.pt $MODEL_FLAGS $DIFFUSION_FLAGS
