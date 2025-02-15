from datasets import load_dataset
import subprocess
import os
from PIL import Image

# Build Hugging Face CLI login command
huggingface_hub_token = "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"
os.environ["HUGGINGFACE_HUB_TOKEN"] = huggingface_hub_token
command_HugginFace_login = ["huggingface-cli", "login", "--token", huggingface_hub_token, "--add-to-git-credential"]
subprocess.run(command_HugginFace_login)

# Load the dataset
dataset = load_dataset("umesh16071973/New_Floorplan_demo_dataset")

# Create a directory to save the images
save_dir = 'Dataset'
os.makedirs(save_dir, exist_ok=True)

# Desired resolution for resizing
new_resolution = (512, 512)

# Iterate through the dataset and resize/save each image
for idx, item in enumerate(dataset['train']):
    image = item['image']  # Adjust this if your images are in a different field
    resized_image = image.resize(new_resolution, Image.LANCZOS)
    save_path = os.path.join(save_dir, f"image_{idx}.jpg")
    resized_image.save(save_path)
    print(f"Saved resized image to {save_path}")

print("All images have been resized and downloaded.")


