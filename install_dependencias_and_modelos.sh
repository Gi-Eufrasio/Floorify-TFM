#!/bin/bash

# Exit script if any command fails
set -e

# Create directory for the Diffusers model
mkdir -p default_diffusers_model
mkdir -p Model_Test_Local\Text_to_Image_Testes\Model\My_Model_Trained

cd default_diffusers_model

# Install dependencies
pip install git+https://github.com/huggingface/diffusers
pip install git+https://github.com/huggingface/diffusers.git

# Install and upgrade Diffusers for Torch and Flax
pip install --upgrade 'diffusers[torch]'
pip install --upgrade 'diffusers[flax]'

# Clone the Diffusers repository
if [ ! -d "diffusers" ]; then
    git clone https://github.com/huggingface/diffusers
else
    echo "The 'diffusers' directory already exists. Skipping cloning."
fi

cd diffusers

# Install Diffusers from the cloned repository
pip install .

# Install additional packages
pip install 'diffusers[training]' accelerate datasets
pip install torchvision
pip install gradio

apt-get install zip

# Make the script executable automatically
chmod +x "$0"

# Success message
echo "Installation completed successfully!"