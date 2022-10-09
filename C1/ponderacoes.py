from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.cluster import KMeans
import pandas as pd
import glob
import os
import numpy as np

def checkIfFileExists():
    index = 1
    exists = True
    newFileName = ''
    while (exists == True):
        exists = os.path.exists(f'./df_valorado/df_valorado_{index}.csv')
        if (exists == True):
             index += 1
        else:
            newFileName = f'./df_valorado/df_valorado_{index}.csv'
    return newFileName
# --------------------

# INÍCIO ----->

# Apagar se o arquivo existe:
if os.path.exists("tweets.csv"):
    os.remove("tweets.csv")

# Cria um csv novo:
f = open("tweets.csv", "x")

# Abre a pasta tweets, lê todos os arquivos com a extensão txt e faz um csv:
with open(file='tweets.csv', mode='a', encoding='utf-8') as csv_file:
    for path in glob.glob('./C1/tweets/*.txt'):
        with open(path) as txt_file:
            txt = txt_file.read() + '\n'
            csv_file.write(txt)

# Criação do dataframe:
df = pd.read_csv('tweets.csv', encoding='utf-8', on_bad_lines='skip')
df = df.drop_duplicates()
df_csv = df.to_csv('tweets_drop_duplicates.csv')
cv = CountVectorizer()

# Realização do TF:
word_count_vector = cv.fit_transform(df)
print("TF")
print(word_count_vector.toarray().sum(axis=0))

# Realização do IDF:
word_count_vector = cv.fit_transform(df)
idf_transformer = TfidfTransformer(smooth_idf=True,use_idf=True)
idf_transformer.fit(word_count_vector)
idf = pd.DataFrame(idf_transformer.idf_, index=cv.get_feature_names_out(), columns=["IDF"]) 
idf.sort_values(by=['IDF'])
print(idf)

# Realização do TF-IDF:
count_vector = cv.transform(df)
tf_idf_vector = idf_transformer.transform(count_vector)
feature_names = cv.get_feature_names_out()
first_document_vector = tf_idf_vector[0]
tfidf = pd.DataFrame(first_document_vector.T.todense(), index=feature_names, columns=["TF-IDF"]) 
tfidf.sort_values(by=["TF-IDF"],ascending=False)
print(tfidf)

tf_idf_vectorizer = TfidfVectorizer()
X = tf_idf_vectorizer.fit_transform(df.iloc[:, 0])

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42).fit(X)

teste = kmeans.predict(tf_idf_vectorizer.transform(df.iloc[:, 0]))
print(teste)

df_valorado = pd.DataFrame(data = {'Texto': df.iloc[:, 0], 'Valor': teste})
df_valorado = df_valorado.sort_values(by=['Valor'])
df_valorado = df_valorado.reset_index(drop=True)
print(df_valorado)

df_valorado.to_csv(checkIfFileExists(), sep=';', index=True)