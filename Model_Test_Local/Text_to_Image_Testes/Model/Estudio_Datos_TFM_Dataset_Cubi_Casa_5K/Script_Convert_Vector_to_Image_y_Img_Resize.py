import os
import cairosvg
from PIL import Image

# Script que transforma imágenes vectoriales filtradas en JPG y las cambia de tamaño a 512x512 para realizar entrenamiento Fine_Tuning

def convert_svg_to_jpg(input_dir, output_dir, target_size=(510, 510), scale=1.0):
    # Crear directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Itera sobre todos los archivos en el directorio de entrada.
    for filename in os.listdir(input_dir):
        if filename.endswith(".svg"):
            svg_path = os.path.join(input_dir, filename)
            png_filename = f"{os.path.splitext(filename)[0]}.png"
            png_path = os.path.join(output_dir, png_filename)
            jpg_filename = f"{os.path.splitext(filename)[0]}.jpg"
            jpg_path = os.path.join(output_dir, jpg_filename)
            
            # Convertir SVG a PNG
            cairosvg.svg2png(url=svg_path, write_to=png_path, scale=scale)
            print(f"Convertido para PNG: {svg_path} -> {png_path}")
            
            
            # Abra la imagen PNG, cambie su tamaño y conviértala a JPG con fondo blanco.
            with Image.open(png_path) as img:
                # Cambiar el tamaño de la imagen al tamaño objetivo
                img = img.resize(target_size, Image.LANCZOS)
                
                # Crea una imagen blanca del mismo tamaño.
                background = Image.new('RGB', img.size, (255, 255, 255))
                
                # Combina la imagen PNG con el fondo blanco.
                img_with_background = Image.alpha_composite(background.convert('RGBA'), img)
                
                # Guarda la imagen combinada como JPG
                img_with_background.convert('RGB').save(jpg_path, 'JPEG')
                print(f"Convertido para JPG: {png_path} -> {jpg_path}")
                
            # Eliminar archivo PNG temporal
            os.remove(png_path)

# Directorio de entrada y salida
input_dir  = "Dataset"
output_dir  = "Imagen_Personalizadas/"

# Llama a la función de conversión
convert_svg_to_jpg(input_dir, output_dir, target_size=(510, 510), scale=2.0)
