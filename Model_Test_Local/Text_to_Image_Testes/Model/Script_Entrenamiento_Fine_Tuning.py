import subprocess
import os
from datasets import load_dataset
from PIL import Image
from torchvision import transforms
import datasets
import torch
from torch.utils.data import DataLoader, Dataset
from torchvision.datasets import ImageFolder
import glob
from datasets import Dataset as HFDataset, DatasetDict, Features, Value, Array3D
import pandas as pd
from datasets import load_dataset

# Métodos de aplicación de ajuste fino en difusión estable

# Crear comando de inicio de sesión CLI de Hugging Face
huggingface_hub_token = "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"
os.environ["HUGGINGFACE_HUB_TOKEN"] = huggingface_hub_token
command_HugginFace_login = ["huggingface-cli", "login", "--token", huggingface_hub_token, "--add-to-git-credential"]
subprocess.run(command_HugginFace_login)

model_name = "runwayml/stable-diffusion-v1-5"  
train_dir = "/home/data/giovan/testes/Text_to_Image_Testes/Model/Dataset_Resize_Cubi_Casa_5K/train/Floor_Plan_Imagenes"
output_dir = "My_Model_Trained" 

# Build the command
command_train  = [
    "accelerate", "launch", "/home/data/giovan/testes/Dreambooth/Model/diffusers/examples/text_to_image/train_text_to_image.py",
    "--pretrained_model_name_or_path", model_name,
    "--train_data_dir", train_dir,
    "--use_ema",
    "--resolution", "512", "--center_crop", "--random_flip",
    "--train_batch_size", "4",
    "--gradient_accumulation_steps", "4",
    "--gradient_checkpointing",
    "--mixed_precision", "fp16",
    "--max_train_steps", "1500",
    "--learning_rate", "5e-6",
    "--max_grad_norm", "4",
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

