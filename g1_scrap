import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
import mysql.connector
import re

options = Options()
options.add_argument('--headless')
options.add_argument('windows size = 400,800')

driver = webdriver.Chrome(options=options)
driver.get("https://g1.globo.com/")
sleep(2)

element = driver.find_element_by_xpath("//*[@id='feed-placeholder']/div/div/div[3]/a")

for j in range (3):
    for i in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5) #Aguardando 5 segundos para ter todos os dados carregados

    element.click()


site = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234"
)

print(mydb)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE noticias")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="noticias"
)
print(mydb)

# mycursor = mydb.cursor()

# tabela_g1 = """CREATE TABLE g1 (titulo VARCHAR(255), subtitulo VARCHAR(255), tempo VARCHAR(100), 
#                  link VARCHAR(255), img VARCHAR(500))"""

# mycursor.execute(tabela_g1)

mycursor = mydb.cursor()
mycursor.execute("TRUNCATE TABLE g1")


noticias = site.find_all('div', attrs={'class': "feed-post-body"})

lista_noticias = []

mycursor = mydb.cursor()

for noticia in noticias:    
    dados_noticias = []
    
    titulo = noticia.find('div', attrs={'class': 'feed-post-body-title gui-color-primary gui-color-hover'})   
    img = noticia.find('img', attrs={'class':'bstn-fd-picture-image'})
    link = noticia.find('div', attrs={'class':'_b'}).find('a')
    resumo = noticia.find('div', attrs={'class':'feed-post-body-resumo'})
    tempo = noticia.find('span', attrs={'class':'feed-post-datetime'})
 
    dados_noticias.append(titulo.text) 
    
    if (resumo):
        dados_noticias.append(resumo.text)
    else:
        dados_noticias.append("")
        
    try:
        dados_noticias.append(tempo.text)
    except:
        dados_noticias.append("")
    
    dados_noticias.append(link['href'])

    
    try:
        dados_noticias.append(img['src'])
    except: 
        dados_noticias.append("")
    
        
    lista_noticias.append(dados_noticias)
    
    
    
comando_sql = """INSERT INTO g1 (titulo, subtitulo, tempo, link, img) 
               VALUES (%s, %s, %s, %s, %s)"""

dados = lista_noticias 

mycursor.executemany(comando_sql, dados)

mydb.commit()

mydb.close()

print(mydb)

