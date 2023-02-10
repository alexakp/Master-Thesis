MODEL_FLAGS="--attention_resolutions 32,16,8 --image_size 128 --num_channels 128 --num_heads 4 --num_res_blocks 2 --learn_sigma True --resblock_updown True --use_fp16 True --use_scale_shift_norm True"
DIFFUSION_FLAGS="--diffusion_steps 1000 --noise_schedule cosine --rescale_learned_sigmas False --rescale_timesteps False"

for i in {022000..040000..002000}
do
  echo Model nr: $i
  python scripts/image_sample.py --model_path /d/Simula_data/Models/Temp/openai-2023-02-07-01-23-35-801204/ema_0.9999_$i.pt $MODEL_FLAGS $DIFFUSION_FLAGS
done
