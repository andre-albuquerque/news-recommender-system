import streamlit as st
import mysql.connector
import webbrowser
import pandas as pd
from recommender import recommender
import os

st.set_page_config(
     page_title="Sistema de recomendação de notícias",
     page_icon="https://freepngimg.com/thumb/newspaper/8-2-newspaper-png.png",
     layout="centered",
     initial_sidebar_state="auto")

st.markdown("<h1 style='text-align: center; color: red;'>Sistema de recomendação de notícias</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Criado por André de Albuquerque</h4>", unsafe_allow_html=True)
st.markdown("[Linkedin](https://www.linkedin.com/in/andr%C3%A9-albuquerque-/)")
st.markdown("[Código do projeto](https://github.com/andre-albuquerque/recommender-system)")
for linha in range(3):
    st.write(" ")


st.subheader("Manchetes mais recentes")
st.write("___")

host = os.environ.get("DB_HOST")
user= os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")
db = os.environ.get("DB_DATABASE")

# Comandos para conectar criar o database e as tabelas no MySQL se não existir

mydb = mysql.connector.connect(
host=host,
user=user,
passwd=password,
database=db
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM noticias.news;")

rows = mycursor.fetchall()

def noticias_recom(id=None):

    st.sidebar.header("Notícias recomendadas:")
    st.sidebar.write('___')

    nr = recommender(id)

    df = pd.DataFrame(rows)
    
    p = 1
    for j in nr[0]:
        if df.loc[j][5] == "":
            st.sidebar.markdown(f"## {df.loc[j][1]}", unsafe_allow_html=True)
            if (df.loc[j][2]) == "":
                pass
            else:
                st.sidebar.markdown(df.loc[j][2])
            st.sidebar.markdown(f"###### ***{df.loc[j][6]}*** - {df.loc[j][3]}")   
            st.sidebar.write(" ")
            if st.sidebar.button("Clique aqui para acessar a notícia", key=str(1+p)):
                webbrowser.open_new_tab(df.loc[j][4])         

            st.sidebar.markdown("___")

        else:
            st.sidebar.markdown(f"## {df.loc[j][1]}", unsafe_allow_html=True)
            st.sidebar.image(f"{df.loc[j][5]}", use_column_width="always")
            if df.loc[j][2] == "":
                st.sidebar.write(" ")
                pass
            else:
                st.sidebar.markdown(df.loc[j][2])
            st.sidebar.markdown(f"###### ***{df.loc[j][6]}*** - {df.loc[j][3]}")
            st.sidebar.write(" ")
            if st.sidebar.button("Clique aqui para acessar a notícia", key=str(100+p)):
                webbrowser.open_new_tab(df.loc[j][4])    
            st.sidebar.markdown("___")

        p += 1


def dados(inicio=None, fim=None):
    n = 0
    for row in rows[(inicio):(fim)]:        
        if row[5] == "":
            st.markdown(f"## {row[1]}", unsafe_allow_html=True)
            if row[2] == "":
                pass
            else:
                st.markdown(row[2])
            st.markdown(f"###### ***{row[6]}*** - {row[3]}") 
            st.write('')
            if st.button("Clique aqui para acessar a notícia", key=str(10+n)):
                webbrowser.open_new_tab(row[4])
                noticias_recom(id=row[0])
            st.markdown("___")  
        else:
            col1, col2 = st.beta_columns(2)
            with col1:
                st.write(" ")
                st.image(f"{row[5]}", use_column_width='always')
            with col2:
                st.markdown(f"## {row[1]}", unsafe_allow_html=True)
                if row[2] == "":
                    st.write(" ")
                    pass
                else:
                    st.markdown(row[2])
                st.markdown(f"###### ***{row[6]}*** - {row[3]}")
                st.write('')
                if st.button("Clique aqui para acessar a notícia", key=str(200+n)):
                    webbrowser.open_new_tab(row[4])  
                    noticias_recom(id=row[0])        
            st.markdown("___")

        n += 1
    return None


dados(inicio = 0, fim=int(len(rows)))