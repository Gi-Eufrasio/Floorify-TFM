import gradio as gr
from diffusers import StableDiffusionPipeline
import torch

# Load the trained model for inference
output_dir = ".././Model_Test_Local/Text_to_Image_Testes/Model/My_Model_Trained"
pipeline = StableDiffusionPipeline.from_pretrained(output_dir, torch_dtype=torch.float16).to("cuda")

# Function to generate images
def generate_images(prompt, width, height, num_steps, num_images=4):
    images = []
    for _ in range(num_images):
        result = pipeline(prompt, num_inference_steps=num_steps, height=height, width=width)
        if "images" in result:
            image = result["images"][0]
        else:
            raise ValueError("Unexpected output format from pipeline")
        images.append(image)
    return images

# Gradio interface for generating images.
interface = gr.Interface(
    fn=generate_images,
    inputs=[
        gr.Textbox(lines=2, placeholder="Escribe tu mensaje aquí...", label="Prompt"),
        gr.Slider(minimum=256, maximum=1024, step=64, value=512, label="Ancho de la imagen"),
        gr.Slider(minimum=256, maximum=1024, step=64, value=512, label="Altura de imagen"),
        gr.Slider(minimum=10, maximum=100, step=10, value=50, label="Numero de pasos")
    ],
    outputs=[gr.Image(type="pil", label=f"Imagen {i+1}") for i in range(4)],
    title="Generador de Planos - Floorify",
    description="Ingrese un mensaje de texto y el modelo generará cuatro imágenes basadas en él."
)

# Start the interface
interface.launch()
