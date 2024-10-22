from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Cargue la canalización con el modelo entrenado
pipeline = StableDiffusionPipeline.from_pretrained("My_Model_Trained", torch_dtype=torch.float16, use_safetensors=True).to("cuda")

# Establecer el mensaje
prompt = "Floor Plan 2D, 2 Bedroom, 1 Kitchen, 2 Bathroom, 1 Living room"

# Genera y guarda 4 imágenes
for i in range(4):
    image = pipeline(prompt=prompt).images[0]
    image.save(f"Pruebas/Model_2/Prompt_2/output_Teste_{i+1}.png")