from PIL import Image

url="lib/false.png"

# Abra a imagem
imagem = Image.open(url)

# Defina a largura e altura desejadas
largura_desejada = 120
altura_desejada = 80

# Redimensione a imagem
imagem_redimensionada = imagem.resize((largura_desejada, altura_desejada))

# Salve a imagem redimensionada
imagem_redimensionada.save(url)