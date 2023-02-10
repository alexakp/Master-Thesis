#!/bin/sh

#SBATCH -t 13-23:59
#SBATCH -p dgx2q
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

MODEL_FLAGS="--attention_resolutions 32,16,8 --image_size 128 --num_channels 128 --num_heads 4 --num_res_blocks 2 --learn_sigma True --resblock_updown True --use_fp16 True --use_scale_shift_norm True"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False"

srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-01-23-20-01-54-790291/ema_0.9999_002000.pt $MODEL_FLAGS $DIFFUSION_FLAGS
srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-01-23-20-01-54-790291/ema_0.9999_004000.pt $MODEL_FLAGS $DIFFUSION_FLAGS
srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-01-23-20-01-54-790291/ema_0.9999_006000.pt $MODEL_FLAGS $DIFFUSION_FLAGS
srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-01-23-20-01-54-790291/ema_0.9999_008000.pt $MODEL_FLAGS $DIFFUSION_FLAGS
srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-01-23-20-01-54-790291/ema_0.9999_010000.pt $MODEL_FLAGS $DIFFUSION_FLAGS
srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-01-23-20-01-54-790291/ema_0.9999_012000.pt $MODEL_FLAGS $DIFFUSION_FLAGS
srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-01-23-20-01-54-790291/ema_0.9999_014000.pt $MODEL_FLAGS $DIFFUSION_FLAGS
srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-01-23-20-01-54-790291/ema_0.9999_016000.pt $MODEL_FLAGS $DIFFUSION_FLAGS