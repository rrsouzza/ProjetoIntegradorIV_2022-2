import csv
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn.cluster import KMeans
import pandas as pd
import os

# 0 = Neutro
# 1 = Positivo
# 2 = Negativo

# Essa função verifica se já existe um arquivo chamado df_valorado*index*. Assim sempre salva como df_valorado_1, df_valorado_2, etc.
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

# Essa função procura e retorna o texto entre duas strings/caracteres dentro de uma string.
# Pode ser usada para, por exemplo, retornar o texto que esteja dentro de aspas ""
def find_between(string, first, last):
    # Exemplo -> 
    try:
        start = string.index(first) + len(first)
        end = string.index(last, start)
        return string[start:end]
    except ValueError:
        return ""
# --------------------

# Essa função pega um .csv que contenha tweets valorados pelo k-means com 0, 1 e 2, e salva cada valor separadamente em um .csv.
def export_separate_data():
    
    # Lê o .csv escolhido, salva num DataFrame
    df_kmeans = pd.read_csv('./kmeans_manual/3ª Avaliação/df_original-2-2.csv', sep=';', index_col=0)
    print(f'df_kmeans: {df_kmeans}')

    # Seleciona todas as linhas que possuam valor 0 na coluna Valor, e armazena em outro DataFrame
    df_kmeans0 = df_kmeans.loc[df_kmeans['Valor'] == 0]
    # Exporta o DataFrame para um .csv
    df_kmeans0.to_csv('./kmeans_manual/3ª Avaliação/2-2-0.csv', sep=';', index=True)

    # Seleciona todas as linhas que possuam valor 1 na coluna Valor, e armazena em outro DataFrame
    df_kmeans1 = df_kmeans.loc[df_kmeans['Valor'] == 1]
    # Exporta o DataFrame para um .csv
    df_kmeans1.to_csv('./kmeans_manual/3ª Avaliação/2-2-1.csv', sep=';', index=True)

    # Seleciona todas as linhas que possuam valor 2 na coluna Valor, e armazena em outro DataFrame
    df_kmeans2 = df_kmeans.loc[df_kmeans['Valor'] == 2]
    # Exporta o DataFrame para um .csv
    df_kmeans2.to_csv('./kmeans_manual/3ª Avaliação/2-1-2.csv', sep=';', index=True)
# --------------------


# INÍCIO ----->

# Apagar se o arquivo existe:
if os.path.exists('tweets.csv'):
    os.remove('tweets.csv')
# --------------------

# Abre o arquivo tweets:
with open('tweets.txt', encoding='utf-8') as txt_file:
    # Lê todas as linhas do .txt dos tweets
    lines = txt_file.readlines()
    # Percorre todas as linhas do .txt e elimina as linhas que não possuem texto
    for index, line in enumerate(lines):
        if (not line.__len__() >= 2):
            lines.pop(index)

    print(len(lines))
        
    # Abre o arquivo onde será salvo um tweet por linha
    with open('tweets.csv', 'w', encoding='utf-8') as csv_parsed:
        writer = csv.writer(csv_parsed)

        length = len(lines)
        index = 0
        all_lines = ['']

        # O código a seguir funciona da seguinte maneira:
        # A cada loop, ele lê a linha_atual (current_line), a proxima_primeira_linha (next_first_line), a proxima_segunda_linha (next_second_line), até a proxima_setima_linha.
        # Assim o código lida com o caso onde um tweet possui quebras de linha, e ocupa mais de uma linha.
        # O código procura pelo caractere ';' no final de cada linha, que é o limitador do final do texto de um tweet.
        # Assim, a cada loop, ao ler as próximas 8 linhas, ele define em qual linha o tweet termina, e copia todo esse texto para a string_final (final_line)
        # No final, verifica se todas as linhas atuais estão vazias, e se positivo, encerra o loop.

        umaVez = False
        while (index <= length):
            if (index >= 2000):
                break
            
            final_line = ''
            
            # print(f'index: {index}')
            try:
                current_line = lines[index].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                current_line = ''

            # print(current_line)

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

            try:
                next_eighth_line = lines[index + 8].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_eighth_line = ''

            try:
                next_nineth_line = lines[index + 9].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_nineth_line = ''

            try:
                next_tenth_line = lines[index + 10].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_tenth_line = ''

            try:
                next_eleventh_line = lines[index + 11].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_eleventh_line = ''

            try:
                next_twelfth_line = lines[index + 12].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_twelfth_line = ''

            try:
                next_thirteenth_line = lines[index + 13].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_thirteenth_line = ''

            try:
                next_fourteenth_line = lines[index + 14].rstrip()
            except Exception as e:
                # print(f'Error: {e}')
                next_fourteenth_line = ''

            final_line = ''
            
            # if (index >= 600 and umaVez == False):
            #     if (index == 8000):
            #         umaVez = True
                    
            #     print(f'---------current_line----------- {current_line}')
            #     print(f'---------next_first_line----------- {next_first_line}')
            #     print(f'---------next_second_line----------- {next_second_line}')
            #     print(f'---------next_third_line----------- {next_third_line}')
            #     print(f'---------next_fourth_line----------- {next_fourth_line}')
            #     # print(f'---------next_fifth_line----------- {next_fifth_line}')
            #     # print(f'---------next_sixth_line----------- {next_sixth_line}')
            #     # print(f'---------next_seventh_line----------- {next_seventh_line}')
            #     # print(f'---------next_eighth_line----------- {next_eighth_line}')
            #     # print(f'---------next_nineth_line----------- {next_nineth_line}')
            #     # print(f'---------next_tenth_line----------- {next_tenth_line}')
            #     # print(f'---------next_eleventh_line----------- {next_eleventh_line}')
            #     # print(f'---------next_twelfth_line----------- {next_twelfth_line}')
            #     # print(f'---------next_thirteenth_line----------- {next_thirteenth_line}')
            #     # print(f'---------next_fourteenth_line----------- {next_fourteenth_line}')
            
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
            elif (next_eighth_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line} {next_seventh_line} {next_eighth_line}'
                index = index + 9
            elif (next_nineth_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line} {next_seventh_line} {next_eighth_line} {next_nineth_line}'
                index = index + 10
            elif (next_tenth_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line} {next_seventh_line} {next_eighth_line} {next_nineth_line} {next_tenth_line}'
                index = index + 11
            elif (next_eleventh_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line} {next_seventh_line} {next_eighth_line} {next_nineth_line} {next_tenth_line} {next_eleventh_line}'
                index = index + 12
            elif (next_twelfth_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line} {next_seventh_line} {next_eighth_line} {next_nineth_line} {next_tenth_line} {next_eleventh_line} {next_twelfth_line}'
                index = index + 13
            elif (next_thirteenth_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line} {next_seventh_line} {next_eighth_line} {next_nineth_line} {next_tenth_line} {next_eleventh_line} {next_twelfth_line} {next_thirteenth_line}'
                index = index + 14
            elif (next_fourteenth_line.endswith(';')):
                final_line = f'{current_line} {next_first_line} {next_second_line} {next_third_line} {next_fourth_line} {next_fifth_line} {next_sixth_line} {next_seventh_line} {next_eighth_line} {next_nineth_line} {next_tenth_line} {next_eleventh_line} {next_twelfth_line} {next_thirteenth_line} {next_fourteenth_line}'
                index = index + 15

            if len(final_line) > 2:
                all_lines.append(f'{final_line}')
            
            # print(f'final_line: {final_line}')
            # print(f'index: {index}')

            if (final_line == '' 
                and next_first_line == '' 
                and next_second_line == '' 
                and next_third_line == '' 
                and next_fourth_line == '' 
                and next_fifth_line == '' 
                and next_sixth_line == '' 
                and next_seventh_line == ''
                and next_eighth_line == ''
                and next_nineth_line == ''
                and next_tenth_line == ''
                and next_eleventh_line == ''
                and next_twelfth_line == ''
                and next_thirteenth_line == ''
                and next_fourteenth_line == ''
            ):
                break
        # ---- while
        
        indice = 1
        all_lines.pop(0)
        # Remove o primeiro elemento vazio inserido na hora da inicialização

        writer = csv.writer(csv_parsed)
        
        # Percorre todas as linhas preparadas para salvar no .csv
        print(f'allLines: {all_lines}')
        for line in all_lines:
            # text_between_double_quotes = find_between(line, '"', '"')
            # if text_between_double_quotes != '':
            #     line = line.replace(text_between_double_quotes, f'"{text_between_double_quotes}"')

            # Remove os números iniciais de cada linha ('1-', '2-', '3-', etc)
            tweet_index = f'{indice}-'
            if line.startswith(tweet_index):
                line = line.replace(tweet_index, '')

            # Remove o ';' do final de cada linha
            if line.endswith(';'):
                line = line[:-1]

            # Substitui a linha no array pela linha modificada
            all_lines[indice - 1] = line
            line_for_csv = [line]
            
            # Escreve a linha modificada no .csv
            # csv_parsed.write(f'{line}\n')
            writer.writerow(line_for_csv)
            
            indice += 1
# --------------------

# Criação do dataframe:

# Lê o .csv do qual deverá ser feito os cálculos
df = pd.read_csv('tweets.csv', encoding='utf-8', on_bad_lines='skip')
# df = pd.read_csv('./kmeans_manual/3ª Avaliação/2-2-1.csv', sep=';', index_col=0)

df = df.drop_duplicates()
# df_csv = df.to_csv('tweets_drop_duplicates.csv')
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

# export_separate_data()

line_for_csv = kmeans.predict(tf_idf_vectorizer.transform(df.iloc[:, 0]))
print(line_for_csv)

df_valorado = pd.DataFrame(data = {'Texto': df.iloc[:, 0], 'Valor': line_for_csv})
# df_valorado = df_valorado.sort_values(by=['Valor'])
df_valorado = df_valorado.reset_index(drop=True)
print(df_valorado)

df_valorado.to_csv(checkIfFileExists(), sep=';', index=True)
# df_valorado.to_csv('./kmeans_manual/3ª Avaliação/kmeans/2-2-1.csv', sep=';', index=True)
# --------------------