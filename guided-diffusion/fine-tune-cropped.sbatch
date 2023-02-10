#!/bin/sh

#SBATCH -t 13-23:59
#SBATCH -p dgx2q
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

MODEL_FLAGS="--attention_resolutions 32,16,8 --dropout 0.3 --image_size 128 --num_channels 128 --num_heads 4 --num_res_blocks 2 --learn_sigma True --resblock_updown True --use_fp16 True --use_scale_shift_norm True"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule cosine --rescale_learned_sigmas False --rescale_timesteps True"
TRAIN_FLAGS="--lr 1e-4 --batch_size 32 --resume_checkpoint /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-01-28-19-10-16-936640/ema_0.9999_300000.pt"

srun python scripts/image_train.py --data_dir /home/alexakp/D1/Master_Thesis/Images_data/cropped/polyps-1 $MODEL_FLAGS $DIFFUSION_FLAGS $TRAIN_FLAGS