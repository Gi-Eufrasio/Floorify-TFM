import os
import shutil
from PIL import Image, ImageDraw
import cairosvg

# Script para listar el contenido del Dataset CubiCasa5K
# Script enumera y recopila imágenes vectoriales de planos arquitectónicos de casas, filtrando solo con imágenes de planos de casas con solo 1 plano

def listar_conteudos_diretorio_Excluir_Casas_Sobrado(caminho):
    
    if os.path.isdir(caminho):
        try:
            conteudos = os.listdir(caminho)
            print(f"Conteúdos do diretório {caminho}:")
            
            for conteudo in conteudos:

                caminho_subpasta = caminho + "/" + conteudo

                arquivos_png = [arquivo for arquivo in os.listdir(caminho_subpasta) if arquivo.lower().endswith('.png')]

                if len(arquivos_png) > 2:
                    shutil.rmtree(caminho_subpasta)
                    print(f"O diretório {caminho_subpasta} foi excluído porque contém mais de três arquivos .png.")
                else:
                    print(f"O diretório {caminho_subpasta} contém {len(arquivos_png)} arquivos .png e não será excluído.")

        except Exception as e:
            print(f"Não foi possível listar os conteúdos do diretório {caminho}. Erro: {e}")
    else:
        print(f"O caminho {caminho} não é um diretório válido.")

def listar_conteudos_diretorio(caminho):

    lista_caminho = []
    
    if os.path.isdir(caminho):
        try:
            conteudos = os.listdir(caminho)
            print(f"Conteúdos do diretório {caminho}:")
            
            for conteudo in conteudos:
                lista_caminho.append(conteudo)

            return lista_caminho

        except Exception as e:
            print(f"Não foi possível listar os conteúdos do diretório {caminho}. Erro: {e}")
    else:
        print(f"O caminho {caminho} não é um diretório válido.")


def renomear_e_mover_arquivo(caminho_atual, novo_diretorio, novo_nome):
    if os.path.isfile(caminho_atual):
        if os.path.isdir(novo_diretorio):
            try:
                novo_caminho = os.path.join(novo_diretorio, novo_nome)
                os.rename(caminho_atual, novo_caminho)
                print(f"Arquivo {caminho_atual} foi renomeado e movido para {novo_caminho}.")
            except Exception as e:
                print(f"Não foi possível renomear e mover o arquivo {caminho_atual}. Erro: {e}")
        else:
            print(f"O caminho {novo_diretorio} não é um diretório válido.")
    else:
        print(f"O caminho {caminho_atual} não é um arquivo válido.")

if __name__ == "__main__":


    Lista_caminho = "Imagen_Integra"

    listar_conteudos_diretorio_Excluir_Casas_Sobrado(Lista_caminho)
    
    list_camino = listar_conteudos_diretorio(Lista_caminho)

    for arquivos in list_camino:

        caminho_atual = "Imagen_Integra/" + arquivos + "/model.svg"
        novo_diretorio = "Dataset"
        novo_nome = "Imagen_id_" + arquivos + ".svg"
        renomear_e_mover_arquivo(caminho_atual, novo_diretorio, novo_nome)