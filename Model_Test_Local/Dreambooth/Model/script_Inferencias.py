import torch
from diffusers import StableDiffusionPipeline

# Caminho para o diretório onde o modelo treinado foi salvo
model_path = "My_Model_Trained"

# Carregar o pipeline de difusão estável usando o modelo treinado
pipeline = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16).to("cuda")

# Definir o prompt para gerar imagens
prompt = "Floor Plan 2D"

# Gerar imagens
num_images = 5  # Número de imagens a serem geradas
images = pipeline(prompt, num_inference_steps=50, guidance_scale=7.5, num_images_per_prompt=num_images).images

# Salvar as imagens geradas
for i, image in enumerate(images):
    image.save(f"Pruebas/generated_image_{i}.png")

print("Imagens geradas e salvas com sucesso!")
