import os
import glob
import torch
import datasets
import subprocess
import pandas as pd
from PIL import Image
from datasets import load_dataset
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, Dataset
from datasets import Dataset as HFDataset, DatasetDict, Features, Value, Array3D

# Fine-tuning application methods in stable broadcast

# Create Hugging Face CLI login command

huggingface_hub_token = "XXX" #Token to Hugging Face
os.environ["HUGGINGFACE_HUB_TOKEN"] = huggingface_hub_token
command_HugginFace_login = ["huggingface-cli", "login", "--token", huggingface_hub_token, "--add-to-git-credential"]
subprocess.run(command_HugginFace_login)
model_name = "runwayml/stable-diffusion-v1-5"  
train_dir = "./Dataset_Resize_Cubi_Casa_5K/train/Floor_Plan_Imagenes"
output_dir = "My_Model_Trained" 

# Build the command

command_train  = [
    "accelerate", "launch", "../../../default_diffusers_model/diffusers/examples/text_to_image/train_text_to_image.py",
    "--pretrained_model_name_or_path", model_name,
    "--train_data_dir", train_dir,
    "--use_ema",
    "--resolution", "512", "--center_crop", "--random_flip",
    "--train_batch_size", "2",
    "--gradient_accumulation_steps", "2",
    "--gradient_checkpointing",
    "--mixed_precision", "fp16",
    "--max_train_steps", "500",
    "--learning_rate", "5e-6",
    "--max_grad_norm", "2",
    "--lr_scheduler", "constant", "--lr_warmup_steps", "0",
    "--output_dir", output_dir,
    "--logging_dir", "output_log1"
]

try:
    subprocess.run(command_train, check=True)
except subprocess.CalledProcessError as e:
    print(f"Erro ao executar o comando: {e.cmd}")
    print(f"Código de saída: {e.returncode}")
    print(f"Saída: {e.output}")

