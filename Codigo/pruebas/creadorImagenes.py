from PIL import Image, ImageDraw
import os

def crearCuadradoColor (directorio,nombre,tamanio,color):
    '''
    param: directorio = ruta de almacenamiento
    param: nombre = nombre con que se almacenara
    param: tamaño = tupla (x,y)
    param: color = tupla de color (r,g,b,a)

    crea una imagen de color pleno y la almacena
    '''
    img = Image.new ('RGBA',tamanio,color)
    dibujo = ImageDraw.Draw(img)
    img.save(f'{directorio} {nombre}.png')
    return img

nombre = 'sinJugar'
directorio = os.path.join ('multimedia','')
tamanio = (30,30)
color = (100,100,100,255)
imagen1 = crearCuadradoColor(directorio,nombre,tamanio,color)