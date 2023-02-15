#!/bin/bash

#SBATCH -t 13-23:59
#SBATCH -p dgx2q
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1

MODEL_FLAGS="--attention_resolutions 32,16,8 --image_size 128 --num_channels 128 --num_heads 4 --num_res_blocks 2 --learn_sigma True --resblock_updown True --use_fp16 True --use_scale_shift_norm True"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps True"

for i in {002000..020000..002000}
do
  echo Model nr: $i
  srun python scripts/image_sample.py --model_path /home/alexakp/D1/Master_Thesis/guided-diffusion/Temp/openai-2023-02-13-14-51-31-991054/ema_0.9999_$i.pt $MODEL_FLAGS $DIFFUSION_FLAGS
done

