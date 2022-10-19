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
if os.path.exists('tweets.csv'):
    os.remove('tweets.csv')
# --------------------

# Abre o arquivo tweets, lê linha por linha, organiza os tweets no csv:
with open('tweets.txt') as txt_file:
    # lines = txt_file.read().splitlines(keepends=True)
    lines = txt_file.readlines()
    for index, line in enumerate(lines):
        if (not line.__len__() >= 2):
            lines.pop(index)
        
    with open('tweets.csv', 'x') as csv_parsed:
        length = len(lines)
        index = 0
        while (index <= length):
            try:
                current_line = lines[index].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                current_line = ''

            try:
                next_first_line = lines[index + 1].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_first_line = ''

            try:
                next_second_line = lines[index + 2].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_second_line = ''

            try:
                next_third_line = lines[index + 3].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_third_line = ''

            try:
                next_fourth_line = lines[index + 4].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_fourth_line = ''

            try:
                next_fifth_line = lines[index + 5].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_fifth_line = ''

            try:
                next_sixth_line = lines[index + 6].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_sixth_line = ''

            try:
                next_seventh_line = lines[index + 7].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_seventh_line = ''

            final_line = ''

            # print(f'---------current_line----------- {current_line}')
            # print(f'---------next_first_line----------- {next_first_line}')
            # print(f'---------next_second_line----------- {next_second_line}')
            # print(f'---------next_third_line----------- {next_third_line}')
            # print(f'---------next_fourth_line----------- {next_fourth_line}')
            # print(f'---------next_fifth_line----------- {next_fifth_line}')
            # print(f'---------next_sixth_line----------- {next_sixth_line}')
            # print(f'---------next_seventh_line----------- {next_seventh_line}')

            if (current_line.endswith(';')):
                final_line = current_line
                index = index + 1
            elif (next_first_line.endswith(';')):
                final_line = f'{current_line} {next_first_line}'
                index = index + 2
            elif (next_second_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line}'
                index = index + 3
            elif (next_third_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line}'
                index = index + 4
            elif (next_fourth_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line}'
                index = index + 5
            elif (next_fifth_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line}'
                index = index + 6
            elif (next_sixth_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line}'
                index = index + 7
            elif (next_seventh_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line} {next_seventh_line}'
                index = index + 8

            csv_parsed.write(f'{final_line}\n')
            
            # print(f'final_line: {final_line}')
            # print(f'index: {index}')

            if (final_line == '' and next_first_line == '' and next_second_line == '' and next_third_line == '' and next_fourth_line == '' and next_fifth_line == '' and next_sixth_line == '' and next_seventh_line == ''):
                break
# --------------------

# Criação do dataframe:
df = pd.read_csv('tweets.csv', encoding='utf-8', on_bad_lines='skip')
df = df.drop_duplicates()
df_csv = df.to_csv('tweets_drop_duplicates.csv')
cv = CountVectorizer()
# --------------------

# Realização do TF:
word_count_vector = cv.fit_transform(df)
print("TF")
print(word_count_vector.toarray().sum(axis=0))
# --------------------

# Realização do IDF:
word_count_vector = cv.fit_transform(df)
idf_transformer = TfidfTransformer(smooth_idf=True,use_idf=True)
idf_transformer.fit(word_count_vector)
idf = pd.DataFrame(idf_transformer.idf_, index=cv.get_feature_names_out(), columns=["IDF"]) 
idf.sort_values(by=['IDF'])
print(idf)
# --------------------

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
# --------------------

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42).fit(X)

teste = kmeans.predict(tf_idf_vectorizer.transform(df.iloc[:, 0]))
print(teste)

df_valorado = pd.DataFrame(data = {'Texto': df.iloc[:, 0], 'Valor': teste})
df_valorado = df_valorado.sort_values(by=['Valor'])
df_valorado = df_valorado.reset_index(drop=True)
print(df_valorado)

df_valorado.to_csv(checkIfFileExists(), sep=';', index=True)
# --------------------