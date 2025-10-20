from PIL import Image
import matplotlib.pyplot as plt

# Abrir imagem original
imagem = Image.open('./img/img1.jpg')

# Converter para tons de cinza
imagem_cinza = imagem.convert('L')

# Converter para binário (preto e branco) aplicando um limiar simples
limiar = 170
imagem_pb = imagem_cinza.point(lambda p: 255 if p > limiar else 0)
imagem_pb = imagem_pb.convert('1') #Garante que apenas bits sejam guardados

# Obter dados raw em bytes
raw_rgb = imagem.tobytes()
raw_cinza = imagem_cinza.tobytes()
raw_pb = imagem_pb.tobytes()

# Tamanho em bytes dos dados raw
tamanho_rgb = len(raw_rgb)
tamanho_cinza = len(raw_cinza)
tamanho_pb = len(raw_pb)

print(f"Tamanho raw RGB: {tamanho_rgb} bytes")
print(f"Tamanho raw tons de cinza: {tamanho_cinza} bytes")
print(f"Tamanho raw preto e branco: {tamanho_pb} bytes")

# Plotar imagens
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].imshow(imagem)
axs[0].set_title('Original (RGB)')
axs[0].axis('off')

axs[1].imshow(imagem_cinza, cmap='gray')
axs[1].set_title('Tons de cinza')
axs[1].axis('off')

axs[2].imshow(imagem_pb, cmap='gray')
axs[2].set_title('Binária')
axs[2].axis('off')

plt.show()
