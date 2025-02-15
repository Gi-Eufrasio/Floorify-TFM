import os
import torch
from pytorch_fid import fid_score

def main():
    # Define the paths to the folders containing the reference and generated images
    real_images_path = "path"
    fake_images_path = "path"

    # Calculate the FID score
    fid_value = fid_score.calculate_fid_given_paths(
        [real_images_path, fake_images_path], 
        batch_size=16, 
        dims=2048, 
        device='cuda' if torch.cuda.is_available() else 'cpu'
    )

    print(f'FID: {fid_value}')

main()
