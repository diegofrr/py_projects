from PIL import Image
from tkinter import messagebox
import math

formato = input("Formato da imagem (PNG, JPG, JPEG, TIFF, RAW, WEBP)\n")

nome = "img." + formato

im = Image.open(nome)
print(f'Proporções originais da imagem: \n\n{im.size[0]}x{im.size[1]} \n')
proporcoes = input("Digite as novas proporções separadas por ',' (x,y)\n").split(',')

x = int(proporcoes[0])
y = int(proporcoes[1])


new_img = im.resize((x,y))
new_img.save("img_resize.png")

print("Imagem redimensionada!\n")


input("ENTER para sair\n")
