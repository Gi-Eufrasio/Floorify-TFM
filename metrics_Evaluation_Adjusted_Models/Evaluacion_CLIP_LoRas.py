from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch
import os

# List of test images for Test 01 - LoRa
Test_01_LoRa_Files = [
    "media_images_test_50_04de4f2c6ac994025289.png", 
    "media_images_test_500_5d2bb0a72b86f6a1dfa6.png", 
    "media_images_test_500_3275dc8faae9438ad8b7.png", 
    "media_images_test_500_cf7e41fa7ca7572e8de9.png"
]
Test_01_LoRa_Path = "path"

# List of test images for Test 02 - LoRa
Test_02_LoRa_Files = [
    "media_images_test_404_5d74138428c7445f8b30.png", 
    "media_images_test_404_f220d75b7a4d17c36125.png", 
    "media_images_test_500_2ec9d452a4113832e558.png", 
    "media_images_test_500_57a716310d3c78cd4acc.png", 
    "media_images_test_500_b2dc980e87a29e4c1b42.png"
]
Test_02_LoRa_Path = "path"

# Complete paths for Test 01 images
Complete_Files_Test_1 = [os.path.join(Test_01_LoRa_Path, file) for file in Test_01_LoRa_Files]
Image_Counter_Test_1 = 0

# Complete paths for Test 02 images
Complete_Files_Test_2 = [os.path.join(Test_02_LoRa_Path, file) for file in Test_02_LoRa_Files]
Image_Counter_Test_2 = 0

# Iterate over Test 01 images
for Open_File in Complete_Files_Test_1: 
    
    Image_Counter_Test_1 += 1

    image = Image.open(Open_File)

    texts = ["Floor Plan 2D"]

    # Load the CLIP model and processor
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    # Preprocess the image and text
    inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)

    # Pass the inputs through the model
    outputs = model(**inputs)

    # Extract embeddings from the image and text
    image_embeddings = outputs.image_embeds
    text_embeddings = outputs.text_embeds

    # Compute similarity (cosine similarity)
    similarity = torch.nn.functional.cosine_similarity(image_embeddings, text_embeddings)

    # Display similarity score
    print("CLIP Score Value - Test 1, Image "+ str(Image_Counter_Test_1) +": " + str(similarity))

# Iterate over Test 02 images
for Open_File_2 in Complete_Files_Test_2: 
    
    Image_Counter_Test_2 += 1

    image = Image.open(Open_File_2)

    texts = ["Floor Plan 2D"]

    # Load the CLIP model and processor
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    # Preprocess the image and text
    inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)

    # Pass the inputs through the model
    outputs = model(**inputs)

    # Extract embeddings from the image and text
    image_embeddings = outputs.image_embeds
    text_embeddings = outputs.text_embeds

    # Compute similarity (cosine similarity)
    similarity = torch.nn.functional.cosine_similarity(image_embeddings, text_embeddings)

    # Display similarity score
    print("CLIP Score Value - Test 2, Image "+ str(Image_Counter_Test_2) +": " + str(similarity))
