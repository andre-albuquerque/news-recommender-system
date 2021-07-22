import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
import mysql.connector
import keyring


# Comandos para criar o database e as tabelas no MySQL

""" mydb = mysql.connector.connect(
host="localhost",
user="root",
passwd= "1234",
database="noticias"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE noticias")"""


# tabela_gnews = """CREATE TABLE gnews (titulo VARCHAR(255), tempo VARCHAR(100), 
# link VARCHAR(1000), img VARCHAR(500))"""

# mycursor.execute(tabela_gnews)

# tabela_g1 = """CREATE TABLE g1 (titulo VARCHAR(255), subtitulo VARCHAR(255), tempo VARCHAR(100), 
#                  link VARCHAR(255), img VARCHAR(500))"""

# mycursor.execute(tabela_g1)

# tabela_gnews = """CREATE TABLE estadao (titulo VARCHAR(255), subtitulo VARCHAR(255), tempo VARCHAR(100), 
# link VARCHAR(1000), img VARCHAR(500))"""

# mycursor.execute(tabela_estadao)



def scraping():
    """
    Função para fazer scraping de notícias dos portais G1, Estadão e Google News salvando em banco de dados MySQL.

    Criado por André de Albuquerque (andrealbuquerqueleo@gmail.com)

    """
    print('Iniciando scraping do site G1. Isto pode demorar um pouco...')

    
    # opções do método Selenium | --headless não abre nagevador
    options = Options()
    options.add_argument('--headless')
    options.add_argument('windows size = 400,800')

    driver = webdriver.Chrome(options=options)
    driver.get("https://g1.globo.com/")
    sleep(2)

    # botão 'veja mais' do site G1
    element = driver.find_element_by_xpath("//*[@id='feed-placeholder']/div/div/div[3]/a")

    # loop para dar scroll na página e clicar no botão 'veja mais'
    for j in range (3):
        for i in range(4):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(5) #Aguardando 5 segundos para ter todos os dados carregados

        element.click()

    # obter o html do site com o BeautifulSoup
    site_g1 = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    print('Buscando notícias e salvando em lista...')

    # Busca todas as notícias na página principal
    noticias = site_g1.find_all('div', attrs={'class': "feed-post-body"})

    lista_noticias_g1 = []
    
    # Loop para obter todos os elementos de cada notícia
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
        
            
        lista_noticias_g1.append(dados_noticias)

    sleep(1.5)

    # scraping do google news
    print('Iniciando scraping do site Google News...')

    # acessa o site do Google News
    html = requests.get("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYQjBMVUpTR2dKQ1VpZ0FQAQ?hl=pt-BR&gl=BR&ceid=BR%3Apt-419")

    # obtem o html do site
    site_gnews = BeautifulSoup(html.content, "html.parser")

    print('Buscando notícias e salvando em lista...')

    # obtem todas as noticias do tipo 1 
    noticias_1 = site_gnews.find_all('div', attrs={'class':'xrnccd F6Welf R7GTQ keNKEd j7vNaf'})

    lista_noticias_gnews = []

    # Loop para obter todos os elementos de cada notícia
    for noticia in noticias_1:

        dados_noticias_1 = []

        titulo = noticia.find('a', attrs={'class':'DY5T1d RZIKme'}).text

        tempo = noticia.time

        link = noticia.a['href']
    
        img = noticia.img
            

        dados_noticias_1.append(titulo)    
        
        try:
            dados_noticias_1.append(tempo.text)
        except:
            dados_noticias_1.append("")
        
        dados_noticias_1.append('news.google.com' + link[1:])

        dados_noticias_1.append(img['src'])
        
            
        lista_noticias_gnews.append(dados_noticias_1)
        
    # obtem todas as notícias do tipo 2
    noticias_2 = site_gnews.find_all('div', attrs={'class':'NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc'})
    
    # Loop para obter todos os elementos de cada notícia
    for noticia in noticias_2:
        
        dados_noticias_2 = []

        titulo = noticia.find('a', attrs={'class':'DY5T1d RZIKme'}).text

        tempo = noticia.time

        link = noticia.a['href']
    
        img = noticia.img
            

        dados_noticias_2.append(titulo)    
        
        try:
            dados_noticias_2.append(tempo.text)
        except:
            dados_noticias_2.append("")
        
        dados_noticias_2.append('news.google.com' + link[1:])

        dados_noticias_2.append(img['src'])
        
            
        lista_noticias_gnews.append(dados_noticias_2)

    sleep(1.5)

    # scraping do site Estadão
    print('Iniciando scraping do site Estadão...')

    # acessa o site do Google News
    html_estadao = requests.get("https://www.estadao.com.br/ultimas")

    # obtem o html do site
    site_estadao = BeautifulSoup(html_estadao.content, "html.parser")

    print('Buscando notícias e salvando em lista...')

    # Obtendo todas as notícias da página
    noticias_est = site_estadao.find_all('section', attrs={'class':'col-md-12 col-sm-12 col-xs-12 init item-lista'})

    lista_noticias_estadao = []

    # Loop para obter todos os elementos de cada notícia e salvar em uma lista
    for noticia in noticias_est:

        dados_noticias_est = []

        titulo = noticia.find('h3', attrs={'class':'third'}).text

        tempo = noticia.find('span', attrs={'class':'data-posts'}) 

        link = noticia.find('a', attrs={'class':'link-title'})['href']

        
        dados_noticias_est.append(titulo)    
        
        try:
            dados_noticias_est.append(noticia.find('a', attrs={'class':'link-title'}).find('p').text)
        except:
            dados_noticias_est.append("")
        
        try:
            dados_noticias_est.append(tempo.text)
        except:
            dados_noticias_est.append("")

        dados_noticias_est.append(link)
        
        try:
            dados_noticias_est.append(noticia.find('figure', attrs={'class':'image-ultimas'}).img['data-src-desktop'])
        except:
            dados_noticias_est.append("")


        lista_noticias_estadao.append(dados_noticias_est)

    print('Salvando no banco de dados...')

    # salvando no banco de dados

    # realizando conexão com o banco de dados MySQL
    mydb = mysql.connector.connect(
    host="database-1.cpqjjsrzpykc.us-east-2.rds.amazonaws.com",
    user="admin",
    port="3306",
    passwd="Andre.2021",
    database="noticias"
    )

    mycursor = mydb.cursor()

    # apagando conteúdo anteriores nas tabelas para evitar noticias antigas ou repetidas
    mycursor.execute("TRUNCATE TABLE g1") 

    mycursor.execute("TRUNCATE TABLE gnews")

    mycursor.execute("TRUNCATE TABLE estadao") 


    # comando SQL para inserir os elementos das notícias nas tabelas
    comando_sql_g1 = """INSERT INTO g1 (titulo, subtitulo, tempo, link, img) 
            VALUES (%s, %s, %s, %s, %s)"""

    comando_sql_gnews = """INSERT INTO gnews (titulo, tempo, link, img) 
                        VALUES (%s, %s, %s, %s)"""

    comando_sql_estadao = """INSERT INTO estadao (titulo, subtitulo, tempo, link, img) 
                            VALUES (%s, %s, %s, %s, %s)"""

    mycursor = mydb.cursor()

    dados_g1  = lista_noticias_g1       

    dados_gnews = lista_noticias_gnews  

    dados_estadao = lista_noticias_estadao 

    mycursor.executemany(comando_sql_g1, dados_g1)

    mycursor.executemany(comando_sql_gnews, dados_gnews)

    mycursor.executemany(comando_sql_estadao, dados_estadao)

    mydb.commit()

    # fechando conexão com banco de dados
    mydb.close()

    sleep(1)
    print("Pronto.")
    sleep(1)

    print('Processo finalizado!')