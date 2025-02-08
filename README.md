# Project Floorify-TFM

## Descripción en Español:

Este repositorio tiene como objetivo almacenar los códigos y pruebas realizados en las fases de experimentación del proyecto Floorify.

El proyecto Floorify fue un objeto de investigación experimental, realizado en el marco del proceso de estancia I+D+i en informática con la empresa HP SCDS (España) y en el desarrollo del TFM (Trabajo Fin de Máster), con el propósito de obtener el título de máster en el curso de Ingeniería Informática de la Universidad de Valladolid, en España.

El propósito de la investigación realizada para este trabajo fue experimentar si sería posible crear un modelo inteligente capaz de generar imágenes de planos arquitectónicos (plantas bajas) a partir de una descripción textual con filtros proporcionada en el momento de la inferencia sobre el modelo.

Para la creación del modelo, utilizamos la técnica de Fine-Tuning sobre modelos ya entrenados de Stable Diffusion, empleando como base principal el modelo Diffusion de la plataforma Hugging Face, con los métodos Dreambooth, LoRa y Text_To_Image.

## English Description:

This repository aims to store the codes and tests conducted during the experimental phases of the Floorify project.

The Floorify project was an object of experimental research, carried out within the framework of the R&D+i process in computer science in collaboration with the company HP SCDS (Spain) and during the development of the Master's Final Project (TFM), with the purpose of obtaining the master's degree in the Computer Engineering program at the University of Valladolid, Spain.

The purpose of the research conducted for this work was to explore whether it would be possible to create an intelligent model capable of generating architectural floor plan images (ground plans) based on a textual description with filters provided at the time of inference.

For the model's creation, we used the Fine-Tuning technique on pre-trained Stable Diffusion models, leveraging the Diffusion model from the Hugging Face platform as the main foundation, along with the Dreambooth, LoRa, and Text_To_Image methods.

## Imagenes de Demonstracion de Pruebas Generados:

#### Inferencia con el Metodo Text_to_Image !["Inferencia con el Metodo Text_to_Image"](git_Img/Modelo2prompt2_TextToImage.png)

#### Inferencia con el Metodo LoRas/Dreambooth !["Inferencia con el Metodo LoRas/Dreambooth"](git_Img/Pruebas_02_LoRas.png)

## Demonstration Test Images Generated:

#### Inference with the Text_to_Image Method !["Inference with the Text_to_Image Method"](git_Img/Modelo2prompt2_TextToImage.png)

#### Inference with the LoRas/Dreambooth Method !["Inference with the LoRas/Dreambooth Method"](git_Img/Pruebas_02_LoRas.png)

## Instalación y Métodos para Utilizar el Proyecto

El proyecto almacenado en este repositorio fue generado a partir del lenguaje de programación Python, convirtiéndose en el requisito principal para cualquier persona que desee realizar pruebas y experimentos con el proyecto.
En el archivo "install_dependencias_and_modelos.sh", una vez ejecutado dentro del entorno operativo con Python, se instalan automáticamente todas las bibliotecas utilizadas en el proyecto, recordando que es necesario tener el proyecto ya bajado localmente y estar dentro del proyecto. Dejo el comando a continuación:

```bash
   chmod +x install_dependencias_and_modelos.sh
   ./install_dependencias_and_modelos.sh
```

Es necesario descargar la carpeta de algoritmos y modelos de Diffusion para realizar los fine-tunings si se desea. Todos estos se descargan automáticamente al ejecutar el archivo bash "install_dependencias". Para ejecutar cada fine-tuning, es necesario acceder a los scripts dentro de la carpeta: 📂 Floorify-TFM/Model_Test_Local/Text_to_Image_Testes/Model/Script_Entrenamiento_Fine_Tuning.py

Cada experimento cambia según el nombre de su modelo, pudiendo ser Dreambooth o LoRAs. Por lo tanto, queda a criterio del usuario modificar los parámetros experimentales dentro del código de cada ajuste fino o de las inferencias en los modelos ajustados.

Para poder realizar los fine-tunings, es necesario proporcionar tu token de Hugging Face, permitiendo que el script acceda a tus credenciales y realice el ajuste fino del modelo deseado de manera más segura. El comando que debe ser reemplazado en los métodos, en la cual siempre se encuentra en los scripts de entrenamiento. A continuación, se muestra un ejemplo:

```python
huggingface_hub_token = "XXX" #Token to Hugging Face
```

A continuación, dejo un ejemplo de los parámetros del experimento de ajuste fino de Text_to_Image:

```python
   command_train  = [
    "accelerate", "launch", "../../../default_diffusers_model/diffusers/examples/text_to_image/train_text_to_image.py",
    "--pretrained_model_name_or_path", model_name,
    "--train_data_dir", train_dir,
    "--use_ema",
    "--resolution", "512", "--center_crop", "--random_flip",
    "--train_batch_size", "4",
    "--gradient_accumulation_steps", "4",
    "--gradient_checkpointing",
    "--mixed_precision", "fp16",
    "--max_train_steps", "1500",
    "--learning_rate", "5e-6",
    "--max_grad_norm", "4",
    "--lr_scheduler", "constant", "--lr_warmup_steps", "0",
    "--output_dir", output_dir,
    "--logging_dir", "output_log1"
]
```

Para realizar las inferencias, puedes utilizar Gradio, que ya está configurado para ejecutar inferencias en modelos ajustados dentro del método text_to_image. Es importante recordar que, para esta acción, el modelo ajustado debe estar ubicado dentro de las carpetas del método text_to_image_testes, como se mencionó anteriormente en el proceso de fine-tuning. El siguiente comando permite ejecutar la interfaz de Gradio para realizar las inferencias:

```bash
   python3 interface_gradio.py
```

El proyecto no incluye, por defecto, un modelo prealmacenado en el método, por lo que es necesario utilizar el modelo base y estándar proporcionado en este proyecto, disponible en el siguiente enlace de Hugging Face: (https://huggingface.co/gigio-br/Experiment_Fine_Tuning_Model_Diffusion_Text_to_Image_Floor_Plan_Project) 

Otra opción para utilizar un modelo en Gradio es realizar un nuevo fine-tuning, siguiendo las especificaciones definidas en el script de entrenamiento. Este script ya está preparado para ejecutar el ajuste fino y generar un modelo dentro del método text_to_image.

## Installation and Methods to Use the Project

The project stored in this repository was developed using the Python programming language, making it a key requirement for anyone who wishes to conduct tests and experiments with this project.

In the "install_dependencias_and_modelos.sh" file, once executed in a Python-compatible operating environment, all the libraries used in the project are automatically installed. It is important to note that the project must already be downloaded locally, and you must be inside the project directory. Below is the command to execute it:

```bash
   chmod +x install_dependencias_and_modelos.sh
   ./install_dependencias_and_modelos.sh
```

It is necessary to download the Diffusion algorithms and model folder to perform fine-tunings if desired. These are all automatically downloaded when executing the bash script "install_dependencias". To run each fine-tuning, you need to access the scripts inside the following directory: 📂 Floorify-TFM/Model_Test_Local/Text_to_Image_Testes/Model/Script_Entrenamiento_Fine_Tuning.py

Each experiment varies based on the model name, which can be either Dreambooth or LoRAs. Therefore, the user is responsible for modifying the experimental parameters within the script, whether for fine-tuning or inference on the trained models.

To perform fine-tunings, you must provide your Hugging Face token, allowing the script to access your credentials and securely fine-tune the desired model. The command that needs to be replaced within the methods is always located in the training scripts. Below is an example:

```python
huggingface_hub_token = "XXX" #Token to Hugging Face
```

Below is an example of the fine-tuning parameters for Text_to_Image:

```python
      command_train  = [
    "accelerate", "launch", "../../../default_diffusers_model/diffusers/examples/text_to_image/train_text_to_image.py",
    "--pretrained_model_name_or_path", model_name,
    "--train_data_dir", train_dir,
    "--use_ema",
    "--resolution", "512", "--center_crop", "--random_flip",
    "--train_batch_size", "4",
    "--gradient_accumulation_steps", "4",
    "--gradient_checkpointing",
    "--mixed_precision", "fp16",
    "--max_train_steps", "1500",
    "--learning_rate", "5e-6",
    "--max_grad_norm", "4",
    "--lr_scheduler", "constant", "--lr_warmup_steps", "0",
    "--output_dir", output_dir,
    "--logging_dir", "output_log1"
]
```

To perform inferences, you can use Gradio, which is already configured to run inferences on fine-tuned models within the text_to_image method.

It is important to note that, for this process, the fine-tuned model must be located inside the text_to_image_testes directory, as mentioned earlier in the fine-tuning process.

The following command allows you to run the Gradio interface for performing inferences:

```bash
   python3 interface_gradio.py
```

By default, the project does not include a pre-stored model in the method. Therefore, it is necessary to use the default and standard model provided in this project, available at the following Hugging Face link: (https://huggingface.co/gigio-br/Experiment_Fine_Tuning_Model_Diffusion_Text_to_Image_Floor_Plan_Project) 

Another option to use a model in Gradio is to perform a new fine-tuning, following the specifications defined in the training script. This script is already prepared to execute the fine-tuning process and generate a model within the text_to_image method.

## Citation

```bibtex
@misc{eufrasio-etal-2025-floorify,
  author = {Giovane Eufrasio},
  title = {Proyecto Floorify: Generación de Planos Arquitectónicos Mediante Inteligencia Artificial Generativa},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Gi-Eufrasio/Floorify-TFM}}
}
```
