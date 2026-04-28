import os
import shutil

# Caminho da pasta (coloca a sua pasta aqui)
pasta = r"c:\Users\José Victor\Downloads"

# Tipos de arquivos
tipos = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "PDFs": [".pdf"],
    "Documentos": [".docx", ".txt"],
    "Planilhas": [".xlsx"]
}

# Criar pastas
for pasta_nome in tipos:
    caminho = os.path.join(pasta, pasta_nome)
    if not os.path.exists(caminho):
        os.mkdir(caminho)

# Organizar arquivos
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_arquivo):
        for pasta_nome, extensoes in tipos.items():
            for ext in extensoes:
                if arquivo.lower().endswith(ext):
                    destino = os.path.join(pasta, pasta_nome, arquivo)
                    shutil.move(caminho_arquivo, destino)
                    print(f"Movido: {arquivo} → {pasta_nome}")