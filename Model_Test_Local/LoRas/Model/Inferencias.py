import os
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from safetensors.torch import load_file

# Path to the directory where the LoRa weights are located
model_path = "Model_Test"
lora_weights_path = os.path.join(model_path, "pytorch_lora_weights.safetensors")

# Check if the LoRa weights file exists
if not os.path.exists(lora_weights_path):
    raise ValueError(f"O arquivo necessário '{lora_weights_path}' não existe no diretório '{model_path}'.")

# Load the stable diffusion pipeline using the base model
pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16).to("cuda")

# Load LoRa weights
lora_weights = load_file(lora_weights_path)

# Apply LoRa weights to the base model
for name, param in pipeline.unet.named_parameters():
    if name in lora_weights:
        param.data += lora_weights[name].data

# Define the scheduler if necessary
pipeline.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config)

# Set the prompt to generate images
prompt = "floor plan 2D without colors, just drawn"

# Generate images
num_images = 2  # Number of images to be generated
for i in range(num_images):
    with torch.cuda.amp.autocast():
        image = pipeline(prompt).images[0]
        image.save(f"generated_image_{i}.png")
        torch.cuda.empty_cache()

print("Imagens geradas e salvas com sucesso!")