#!/bin/sh

#SBATCH -t 13-23:59
#SBATCH -p dgx2q
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12


srun python main.py