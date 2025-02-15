from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import os

Test_01_LoRa_Files = ["output_Test_1.png", "output_Test_2.png", "output_Test_3.png", "output_Test_4.png"]
Path_Test_01_LoRa = "path"

Test_02_LoRa_Files = ["output_Test_1.png", "output_Test_2.png", "output_Test_3.png", "output_Test_4.png"]
Path_Test_02_LoRa = "path"

Complete_Files_Test_1 = [os.path.join(Path_Test_01_LoRa, file) for file in Test_01_LoRa_Files]
Image_Counter_Test_1 = int(0)

Complete_Files_Test_2 = [os.path.join(Path_Test_02_LoRa, file) for file in Test_02_LoRa_Files]
Image_Counter_Test_2 = int(0)

for Open_Files in Complete_Files_Test_1: 
    
    Image_Counter_Test_1 += 1

    image = Image.open(Open_Files)

    texts1 = ["Floor Plan 2D, 1 bedroom, 1 kitchen, 1 bathroom, 1 living room"]

    # Load the CLIP model and processor
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    # Preprocess the image and text
    inputs = processor(text=texts1, images=image, return_tensors="pt", padding=True)

    # Pass the inputs through the model
    outputs = model(**inputs)

    # Extract image and text embeddings
    image_embeddings = outputs.image_embeds
    text_embeddings = outputs.text_embeds

    # Calculate similarity (cosine similarity)
    similarity = torch.nn.functional.cosine_similarity(image_embeddings, text_embeddings)

    # Display similarity score
    print("CLIP Score Value Test 1, Figure "+ str(Image_Counter_Test_1) +": " + str(similarity))

for Open_Files2 in Complete_Files_Test_2: 
    
    Image_Counter_Test_2 += 1

    image = Image.open(Open_Files2)

    texts2 = ["Floor Plan 2D, 2 bedrooms, 1 kitchen, 2 bathrooms, 1 living room"]

    # Load the CLIP model and processor
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    # Preprocess the image and text
    inputs = processor(text=texts2, images=image, return_tensors="pt", padding=True)

    # Pass the inputs through the model
    outputs = model(**inputs)

    # Extract image and text embeddings
    image_embeddings = outputs.image_embeds
    text_embeddings = outputs.text_embeds

    # Calculate similarity (cosine similarity)
    similarity = torch.nn.functional.cosine_similarity(image_embeddings, text_embeddings)

    # Display similarity score
    print("CLIP Score Value Test 2, Figure "+ str(Image_Counter_Test_2) +": " + str(similarity))
