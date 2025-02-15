export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export dataset_name="umesh16071973/New_Floorplan_demo_dataset"

accelerate launch --mixed_precision="fp16" /home/tfe/tfm/giovan/testes/Dreambooth/Model/diffusers/examples/text_to_image/train_text_to_image.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --dataset_name=$dataset_name \
  --resolution=256 \
  --center_crop \
  --random_flip \
  --train_batch_size=1 \
  --gradient_accumulation_steps=8 \
  --max_train_steps=5 \
  --learning_rate=1e-05 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --output_dir="model_Test" \
  --push_to_hub \
  --caption_column="text"