import subprocess
import os
import wandb

# Build Hugging Face CLI login command
huggingface_hub_token = "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"
os.environ["HUGGINGFACE_HUB_TOKEN"] = huggingface_hub_token
command_HugginFace_login = ["huggingface-cli", "login", "--token", huggingface_hub_token, "--add-to-git-credential"]
subprocess.run(command_HugginFace_login)

# Initialize wandb
wandb.init(project="dreambooth-lora", entity="giovaneeufrasio")

# Define the training command
command_train = [
    "accelerate", "launch", "/home/data/giovan/testes/Dreambooth/Model/diffusers/examples/dreambooth/train_dreambooth_lora.py",
    "--pretrained_model_name_or_path=runwayml/stable-diffusion-v1-5",
    "--instance_data_dir=/home/data/giovan/testes/LoRas/Model/Dataset",
    "--output_dir=/home/data/giovan/testes/LoRas/Model/Model_Test",
    "--instance_prompt=floor plan 2D",
    "--resolution=512",
    "--train_batch_size=3",
    "--gradient_accumulation_steps=3",
    "--checkpointing_steps=100",
    "--learning_rate=5e-5",
    "--report_to=wandb",
    "--lr_scheduler=constant",
    "--lr_warmup_steps=0",
    "--num_train_epochs=100",
    "--max_train_steps=1000",
    "--validation_prompt=floor plan 2D",
    "--validation_epochs=50",
    "--seed=0",
    "--push_to_hub",
    "--mixed_precision=fp16",
    "--gradient_checkpointing"
]

# Run the training command
subprocess.run(command_train)