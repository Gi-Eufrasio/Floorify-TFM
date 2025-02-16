from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load an image and a phrase
image = Image.open("./Dreambooth_Tests_for_assessment/generated_image_0.png")
texts = ["Floor Plan 2D"]

# Preprocess the image and text
inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)

# Pass the inputs through the model
outputs = model(**inputs)

# Extract embeddings from the image and text
image_embeddings = outputs.image_embeds
text_embeddings = outputs.text_embeds

# Compute similarity (cosine similarity)
similarity = torch.nn.functional.cosine_similarity(image_embeddings, text_embeddings)

# Display the similarity score
print("CLIP Score Value: " + str(similarity))
