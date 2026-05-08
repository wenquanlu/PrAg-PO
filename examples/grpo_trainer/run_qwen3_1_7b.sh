#!/bin/bash

#SBATCH -n 1
#SBATCH -c 16
#SBATCH --mem-per-cpu=16G
#SBATCH --gres=gpu:h100:4
#SBATCH --nodes=1
#SBATCH -t 96:00:00
#SBATCH -p YOUR_PARTITION
#SBATCH --output=./slurm/%x-%j.out
#SBATCH --error=./slurm/%x-%j.err

#source ~/anaconda3/etc/profile.d/conda.sh
#conda activate verl
#unset ROCR_VISIBLE_DEVICES
export VERBOSE=1
export TMPDIR=/tmp
export RAY_TMPDIR=$TMPDIR
set -x

echo $CUDA_VISIBLE_DEVICES
nvidia-smi
python3 -c "import torch; print(torch.cuda.device_count())"

PYTHONUNBUFFERED=1 python3 -m verl.trainer.main_ppo \
    algorithm.adv_estimator=grpo \
    data.train_files=./data/math_level3to5/SimpleRL-simplelr_qwen_level3to5.train.parquet \
    data.val_files=./data/math_level3to5/SimpleRL-simplelr_qwen_level3to5.test.parquet \
    data.train_batch_size=128 \
    data.max_prompt_length=1024 \
    data.max_response_length=3072 \
    data.filter_overlong_prompts=True \
    data.truncation='left' \
    data.seed=42 \
    actor_rollout_ref.model.path=Qwen/Qwen3-1.7B \
    actor_rollout_ref.actor.optim.lr=1e-6 \
    actor_rollout_ref.model.use_remove_padding=True \
    actor_rollout_ref.actor.ppo_mini_batch_size=32 \
    actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=8 \
    actor_rollout_ref.actor.use_kl_loss=False \
    actor_rollout_ref.actor.kl_loss_coef=0.0 \
    actor_rollout_ref.actor.entropy_coeff=0 \
    actor_rollout_ref.actor.clip_ratio_low=0.2 \
    actor_rollout_ref.actor.clip_ratio_high=0.28 \
    actor_rollout_ref.model.enable_gradient_checkpointing=True \
    actor_rollout_ref.actor.fsdp_config.param_offload=False \
    actor_rollout_ref.actor.fsdp_config.optimizer_offload=False \
    actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=32 \
    actor_rollout_ref.rollout.tensor_model_parallel_size=1 \
    actor_rollout_ref.rollout.name=vllm \
    actor_rollout_ref.rollout.gpu_memory_utilization=0.6 \
    actor_rollout_ref.rollout.n=8 \
    actor_rollout_ref.ref.log_prob_micro_batch_size_per_gpu=32 \
    actor_rollout_ref.ref.fsdp_config.param_offload=True \
    algorithm.use_kl_in_reward=False \
    trainer.critic_warmup=0 \
    trainer.logger='["console","wandb"]' \
    trainer.project_name='verl_dapo_math_lvl3to5' \
    trainer.experiment_name='qwen3_1_7b_dapo_prompt_aug' \
    trainer.n_gpus_per_node=4 \
    trainer.nnodes=1 \
    trainer.save_freq=40 \
    trainer.test_freq=40 \
    trainer.total_epochs=40 $@
