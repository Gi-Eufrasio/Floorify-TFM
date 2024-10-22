import os
import json

# Script que verifica imágenes que existen en el directorio del conjunto de datos, pero que no están contenidas en el archivo Json Metadata, ya que tuvieron un error en la detección de texto.
# Con esto, el script excluye las imágenes que no están contenidas en el json.

# Rutas al archivo JSON y a la carpeta con imágenes.
jsonl_file_path = 'metadata.jsonl'
images_folder_path  = 'Imagen_Personalizadas'

if not os.path.isfile(jsonl_file_path):
    raise FileNotFoundError(f"Arquivo JSONL não encontrado: {jsonl_file_path}")

# Cargar datos desde JSONL
data = []
with open(jsonl_file_path, 'r') as file:
    for line in file:
        try:
            data.append(json.loads(line))
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar a linha: {line.strip()}")
            print(f"Erro: {e}")
            continue 

# Extraer los nombres de las imágenes listadas en JSON
listed_images = {item['file_name'] for item in data}

# Listar los archivos en la carpeta de imágenes.
folder_images = set(os.listdir(images_folder_path))

# Compruebe qué imágenes de la carpeta no aparecen en JSON
unlisted_images = folder_images - listed_images

# Ver resultados y eliminar imágenes
print("Imagens na pasta que não estão listadas no JSON:")
for img in unlisted_images:
    print(img)
    img_path = os.path.join(images_folder_path, img)
    try:
        os.remove(img_path)
        print(f"Imagem excluída: {img}")
    except OSError as e:
        print(f"Erro ao excluir a imagem {img}: {e}")