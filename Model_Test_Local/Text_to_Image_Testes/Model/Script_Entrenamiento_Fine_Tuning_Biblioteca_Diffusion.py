import os
import subprocess
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Defina o token de autenticação do Hugging Face
huggingface_hub_token = "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"
os.environ["HUGGINGFACE_HUB_TOKEN"] = huggingface_hub_token

# Comando de login do Hugging Face CLI
command_HugginFace_login = ["huggingface-cli", "login", "--token", huggingface_hub_token]
subprocess.run(command_HugginFace_login)

# Defina os caminhos e parâmetros
model_name = "runwayml/stable-diffusion-v1-5"
train_dir = "/home/data/giovan/testes/Text_to_Image_Testes/Model/Dataset_Resize_Cubi_Casa_5K/train/Floor_Plan_Imagenes"
output_dir = "My_Model_Trained"

# Comando para treinar o modelo
command_train = [
    "accelerate", "launch", "/home/data/giovan/testes/Dreambooth/Model/diffusers/examples/text_to_image/train_text_to_image.py",
    "--pretrained_model_name_or_path", model_name,
    "--train_data_dir", train_dir,
    "--use_ema",
    "--resolution", "512", "--center_crop", "--random_flip",
    "--train_batch_size", "4",
    "--gradient_accumulation_steps", "2",
    "--gradient_checkpointing",
    "--mixed_precision", "fp16",
    "--max_train_steps", "1500",
    "--learning_rate", "1e-05",
    "--max_grad_norm", "1",
    "--lr_scheduler", "cosine",
    "--lr_warmup_steps", "500",
    "--output_dir", output_dir,
    "--logging_dir", "output_log1"
]

# Execute o comando de treinamento
subprocess.run(command_train)

# Carregar o modelo treinado para inferência
pipeline = StableDiffusionPipeline.from_pretrained(output_dir, torch_dtype=torch.float16).to("cuda")

# Função para gerar imagens
def generate_image(prompt, width, height, num_steps):
    images = pipeline(prompt, num_inference_steps=num_steps, height=height, width=width)["sample"]
    return images[0]

# Exemplo de uso da função de inferência
prompt = "Floor Plan 2D, 2 bedroom, 1 kitchen, 2 bathroom, 1 living room"
width = 512
height = 512
num_steps = 50

# Gera a imagem
image = generate_image(prompt, width, height, num_steps)

# Salva a imagem gerada
image.save("generated_image.png")

# Exibe a imagem gerada
image.show()
