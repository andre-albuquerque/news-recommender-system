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


mydb = mysql.connector.connect(
host="database-1.c4f75fob2no8.us-west-2.rds.amazonaws.com",
port=3306,
user="admin",
password="Andre.2021",
database = "noticias"
)

cursor = mydb.cursor()
query = ("SELECT * FROM noticias.news")
cursor.execute(query)
records = cursor.fetchall()
mydb.close()

nltk.download('stopwords')

news_df = pd.DataFrame(records, columns=['id','titulo','subtitulo','hora','link','img', 'fonte'])
news_df = news_df.drop(columns=['id'])

def process_texto(s):
    
    # seleciona apenas letras (lembrando que o texto está em português e as letras possuem acento)
    texto_limpo = gensim.utils.simple_preprocess(s)
    
    # remove stopwords
    sw = stopwords.words('portuguese')
    sem_stopwords = [word for word in texto_limpo if word not in sw]
    
    return sem_stopwords

news_df['titulo_sw'] = news_df['titulo'].apply(lambda s: process_texto(s)).apply(lambda x: ' '.join(x))

bow_transformer = CountVectorizer().fit_transform(news_df['titulo_sw'])

news_tfidf = TfidfTransformer().fit_transform(bow_transformer)

nn = NearestNeighbors(metric='cosine', n_neighbors=4)

lista = []
lista_news = []

def recommender(id):
    lista.clear()
    nn.fit(news_tfidf)
    idx=process.extractOne(news_df['titulo'][id-1], news_df['titulo'])[2]
    print('Notícias recomendadas: ')
    distances, indices=nn.kneighbors(news_tfidf[idx], n_neighbors=4)
    n=0
    for i in indices:
        lista.append(i[1:])

    return lista
