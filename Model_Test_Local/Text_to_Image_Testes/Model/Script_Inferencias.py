from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Load the pipeline with the trained model
pipeline = StableDiffusionPipeline.from_pretrained("Experiment_Fine_Tuning_Model_Diffusion_Text_to_Image_Floor_Plan_Project", torch_dtype=torch.float16, use_safetensors=True).to("cuda")

# Set the message
prompt = "Floor Plan 2D, 2 Bedroom, 1 Kitchen, 2 Bathroom, 1 Living room"

# Generate and save 4 images
for i in range(4):
    image = pipeline(prompt=prompt).images[0]
    image.save(f"Pruebas/Model_xx/Prompt_1/output_Teste_{i+1}.png")