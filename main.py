#Importação das libs necessarias
#Importing the necessary libs
import requests
from bs4 import BeautifulSoup
from PIL import Image

#Definição da URL a ser requisitada e utilização do BeaultifulSoup para o parse da response
#Definition of the URL to be requested and using BeaultifulSoup for the response parse
url = 'http://www.uol.com.br'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

#Criação de uma lista que irá conter todas as URLs de imagem obtidas, utilizando um filtro para inserir somente arquivos jpg
#Creating a list that will contain all the retrieved image URLs, using a filter to insert only jpg files
imgUrlList = []
tags = soup('img')
for tag in tags:
  try:
    if(tag.get('src').find('jpg') !=-1):
      imgUrlList.append(tag.get('src', None))
  except:
    pass

#Criação de uma lista que irá conter todas as descrições das imagens
#Creating a list that will contain all image descriptions
imgDescription = []
for i in range(len(imgUrlList)):
  strings = imgUrlList[i].split('/')
  text = strings[-1]
  imgDescription.append(text[0:-29].replace('-',' '))

#Salva as imagens no disco rígido, com a respectiva descição
#Saving all the images with their respective description in the hard drive
for i in range(len(imgUrlList)):
  Image_url = imgUrlList[i]
  im = Image.open(requests.get(Image_url, stream=True).raw);
  im.save(r"C:\Users\dev\Desktop\ImgStuff\\" + imgDescription[i] + ".png");

