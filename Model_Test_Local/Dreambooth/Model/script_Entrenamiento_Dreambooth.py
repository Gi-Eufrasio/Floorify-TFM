import subprocess
import os
from PIL import Image

# Construa o comando de login do Hugging Face CLI
huggingface_hub_token = "XXX" #Token to Hugging Face
os.environ["HUGGINGFACE_HUB_TOKEN"] = huggingface_hub_token
command_HugginFace_login = ["huggingface-cli", "login", "--token", huggingface_hub_token, "--add-to-git-credential"]
subprocess.run(command_HugginFace_login)

def resize_images(input_dir, output_dir, size=(512, 512)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp", ".tiff")):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            
            output_path = os.path.join(output_dir, filename)
            img.save(output_path)
            print(f"Resized and saved {filename} to {output_path}")

input_directory = "./Floor_Plan_2D_Dataset"
output_directory = "./Floor_Plan_2D_Dataset/Floor_Plan_2D_Dataset_Resize"


resize_images(input_directory, output_directory, size=(512, 512))


command = [
        "accelerate", "launch", "../../../default_diffusers_model/diffusers/examples/dreambooth/train_dreambooth.py",
        "--pretrained_model_name_or_path=CompVis/stable-diffusion-v1-4",
        "--instance_data_dir=./Floor_Plan_2D_Dataset/Floor_Plan_2D_Dataset_Resize",
        "--output_dir=/home/tfe/tfm/giovan/data/testes/Dreambooth/Model/My_Model_Trained",
        "--instance_prompt=Floor Plan 2D",
        "--resolution=512",
        "--train_batch_size=1",
        "--gradient_accumulation_steps=1",
        "--learning_rate=5e-6",
        "--lr_scheduler=constant",
        "--lr_warmup_steps=0",
        "--max_train_steps=300",
        "--push_to_hub"
    ]

subprocess.run(command)