from paddleocr import PaddleOCR
import cv2
import os
import json

# Script que realiza reconocimiento de texto sobre imágenes filtradas de CubiCasa5k para definir los metadatos Json para realizar FineTuning.
# El script también crea imágenes de identificación json y sus respectivos ID y textos que detallan los planos arquitectónicos.

def detect_h_and_others(image_path):

    Objetos_Detectados = []

    try:
        
        # Inicializar PaddleOCR
        ocr = PaddleOCR(use_angle_cls=True, lang='en')

        # Leer la imagen usando OpenCV
        image = cv2.imread(image_path)

        # Realizar OCR en la imagen
        result = ocr.ocr(image, cls=True)

        # Extraer el texto detectado
        detected_texts = [line[1][0] for line in result[0]]

        
        # Contar ocurrencias
        habitacion_solo_count = detected_texts.count('H')
        habitacion2_solo_count = detected_texts.count('MH')
        cozina_solo_count = detected_texts.count('K')
        bano_solo_count = detected_texts.count('KPH')
        bano2_solo_count = detected_texts.count('WC')
        Salon_solo_count = detected_texts.count('OH')
        Undefined = detected_texts.count('UNDEFINED')

        if habitacion_solo_count == 0 and habitacion2_solo_count == 0 and cozina_solo_count == 0 and bano_solo_count == 0 and bano2_solo_count == 0 and Salon_solo_count == 0 and Undefined == 0:
            Objetos_Detectados.append(0)
            print(Objetos_Detectados)

        elif habitacion_solo_count == 0 and habitacion2_solo_count == 0 and cozina_solo_count == 0 and bano_solo_count == 0 and bano2_solo_count == 0 and Salon_solo_count == 0 and Undefined > 0:
            Objetos_Detectados.append(str(Undefined) + " Undefined")
            print(Objetos_Detectados)
        
        else:

            if habitacion_solo_count > 0:
                if habitacion2_solo_count > 0:

                    Objetos_Detectados.append(str(habitacion_solo_count + habitacion2_solo_count) + " Bedroom")
                    print(Objetos_Detectados)

                else: 
                    Objetos_Detectados.append(str(habitacion_solo_count) + " Bedroom")
                    print(Objetos_Detectados)

            elif habitacion2_solo_count > 0:
                
                if habitacion_solo_count > 0:

                    Objetos_Detectados.append(str(habitacion_solo_count + habitacion2_solo_count) + " Bedroom")
                    print(Objetos_Detectados)

                else: 
                    Objetos_Detectados.append(str(habitacion2_solo_count) + " Bedroom")
                    print(Objetos_Detectados)

            else:

                Habitacion_solo_count_Undefined = detected_texts.count('UNDEFINED')
                
                if Habitacion_solo_count_Undefined:
                    if Habitacion_solo_count_Undefined > 2:

                        habitacion_limite = 2
                        Objetos_Detectados.append(str(habitacion_limite) + " Bedroom")
                        print(Objetos_Detectados)

                    else: Objetos_Detectados.append(str(Habitacion_solo_count_Undefined) + " Bedroom")
                else: Objetos_Detectados.append(str(1) + " Bedroom")


            if cozina_solo_count > 0:
                Objetos_Detectados.append(str(cozina_solo_count) + " Kitchen")
                print(Objetos_Detectados)

            elif cozina_solo_count <= 0:
                Objetos_Detectados.append(str(cozina_solo_count + 1) + " Kitchen")
                print(Objetos_Detectados)



            if bano_solo_count > 0:
                if bano2_solo_count > 0:

                    Objetos_Detectados.append(str(bano_solo_count + bano2_solo_count) + " Bathroom")
                    print(Objetos_Detectados)
                    print("Objetos_Detectados1")

                else: Objetos_Detectados.append(str(bano_solo_count) + " Bathroom")

            elif bano2_solo_count > 0:
                if bano_solo_count > 0:

                    Objetos_Detectados.append(str(bano_solo_count + bano2_solo_count) + " Bathroom")
                    print(Objetos_Detectados)
                    print("Objetos_Detectados2")

                else: Objetos_Detectados2.append(str(bano_solo_count) + " Bathroom")

            else:

                bano_solo_count_Undefined = detected_texts.count('UNDEFINED')
                
                if bano_solo_count_Undefined:
                    if bano_solo_count_Undefined > 2:

                        bano_limite = 2
                        Objetos_Detectados.append(str(bano_limite) + " Bathroom")
                        print(Objetos_Detectados)

                    else: Objetos_Detectados.append(str(bano_solo_count_Undefined) + " Bathroom")
                else: Objetos_Detectados.append(str(1) + " Bathroom")


            if Salon_solo_count > 0:
                Objetos_Detectados.append(str(Salon_solo_count) + " Living room")
                print(Objetos_Detectados)

            else: Objetos_Detectados.append(str(1) + " Living room")
        
        # Crear un resumen de palabras detectadas
        detected_texts_summary = "\n".join(detected_texts)
        
        # Crea el mensaje de resultado
        result_message = (
            f"The text contains the following words:\n\n{detected_texts_summary}\n\n"
            f"'Bedroom' detected alone in the image {habitacion_solo_count + habitacion2_solo_count} time(s).\n\n"
            f"'Kitchen' detected alone in the image {cozina_solo_count} time(s).\n\n"
            f"'Bathroom' detected alone in the image {bano_solo_count + bano2_solo_count} time(s).\n\n"
            f"'Living room' detected alone in the image {Salon_solo_count} time(s).\n\n"
        )
        
        return Objetos_Detectados
    except Exception as e:
        return str(e)

# Directorio que contiene archivos de imagen
directory = 'Imagen_Personalizadas'

# Lista para almacenar datos
data = []

# Iterar sobre los archivos en el directorio
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):  

        result_message = detect_h_and_others(str(directory + "/" + filename))
        print(result_message)

        # Combina todos los elementos en una sola cadena usando un bucle
        json_format = "Floor Plan 2D, "
        for item in result_message:
            json_format += str(item) + ", "

        # Elimina la última coma y el espacio extra.
        json_format = json_format.rstrip(", ")

        print(json_format)

        entry = {
            "Img": filename,
            "text": json_format
        }
        data.append(entry)

# Nombre del archivo JSONL
output_filename = 'metadata.jsonl'

# Crear y escribir en un archivo JSONL
with open(output_filename, 'w') as file:
    for entry in data:
        json_record = json.dumps(entry)
        file.write(json_record + '\n')

print(f"Arquivo {output_filename} criado com sucesso!")



