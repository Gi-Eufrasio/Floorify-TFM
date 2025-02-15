import torch
from diffusers import StableDiffusionPipeline

# The best experimental model download - Huggingface
pipeline = StableDiffusionPipeline.from_pretrained("gigio-br/Experiment_Fine_Tuning_Model_Diffusion_Text_to_Image_Floor_Plan_Project", torch_dtype=torch.float16, low_cpu_mem_usage=True).to("cuda")
pipeline.save_pretrained(".././Model_Test_Local/Text_to_Image_Testes/Model/Experiment_Fine_Tuning_Model_Diffusion_Text_to_Image_Floor_Plan_Project")  # Salvar modelo corretamente
