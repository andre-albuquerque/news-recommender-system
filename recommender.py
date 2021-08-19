import mysql.connector
import pandas as pd
from nltk.corpus import stopwords
import nltk
import gensim
from sklearn.neighbors import NearestNeighbors
from fuzzywuzzy import process
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())


#variáveis de ambiente com os dados para se conectar ao banco de dados MySQL no AWS
host = os.environ.get("DB_HOST")
user= os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")
db = os.environ.get("DB_DATABASE")

# Comandos para conectar ao MySQL
mydb = mysql.connector.connect(
host=host,
user=user,
passwd=password,
database=db
)

#obter a lista de noticias do banco de dados
cursor = mydb.cursor()
query = ("SELECT * FROM heroku_576c1dba8f92409.news")
cursor.execute(query)
records = cursor.fetchall()
mydb.close()

#comando para realizar o download dos stopwords (Exigido pela plataforma Heroku)
nltk.download('stopwords')

#cria dataframe com as noticias obtidas do banco de dados
news_df = pd.DataFrame(records, columns=['id','titulo','subtitulo','hora','link','img', 'fonte'])
news_df = news_df.drop(columns=['id'])

#função para processar o texto
def process_texto(s):
    
    # seleciona apenas letras (lembrando que o texto está em português e as letras possuem acento)
    texto_limpo = gensim.utils.simple_preprocess(s)
    
    # remove stopwords
    sw = stopwords.words('portuguese')
    sem_stopwords = [word for word in texto_limpo if word not in sw]
    
    return sem_stopwords

#processa o texto no título das notícias
news_df['titulo_sw'] = news_df['titulo'].apply(lambda s: process_texto(s)).apply(lambda x: ' '.join(x))

#transforma o texto em uma matriz
bow_transformer = CountVectorizer().fit_transform(news_df['titulo_sw'])

#Distribui pesos aos termos, com maiores pesos para os termos com maiores frequências
news_tfidf = TfidfTransformer().fit_transform(bow_transformer)

#instancia o modelo de machine learning para agrupar as notícias
nn = NearestNeighbors(metric='cosine', n_neighbors=4)

lista = []

#função para recomendar as notícias
def recommender(id):
    lista.clear()

    #treina o modelo na base de dados
    nn.fit(news_tfidf)

    #encontra o título da notícia que melhor se assemelha ao título selecionado
    idx=process.extractOne(news_df['titulo'][id-1], news_df['titulo'])[2]
    print('Notícias recomendadas: ')

    #agrupa as 4 notícias mais semelhantes
    distances, indices=nn.kneighbors(news_tfidf[idx], n_neighbors=4)

    #adiciona as notícias semelhantes a lista. Sendo a primeira notícia igual a noticia selecionada, adiciona-se apenas as três últimas
    for i in indices:
        lista.append(i[1:])

    return lista
