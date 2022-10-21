import numpy as np
import pandas as pd

df_000 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/0-0-0.csv', sep=';', index_col=0)
df_001 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/0-0-1.csv', sep=';', index_col=0)
df_002 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/0-0-2.csv', sep=';', index_col=0)
df_010 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/0-1-0.csv', sep=';', index_col=0)
df_011 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/0-1-1.csv', sep=';', index_col=0)
df_012 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/0-1-2.csv', sep=';', index_col=0)
df_020 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/0-2-0.csv', sep=';', index_col=0)
df_021 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/0-2-1.csv', sep=';', index_col=0)
df_101 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/1-0-1.csv', sep=';', index_col=0)
df_102 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/1-0-2.csv', sep=';', index_col=0)
df_111 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/1-1-1.csv', sep=';', index_col=0)
df_112 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/1-1-2.csv', sep=';', index_col=0)
df_120 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/1-2-0.csv', sep=';', index_col=0)
df_121 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/1-2-1.csv', sep=';', index_col=0)
df_122 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/1-2-2.csv', sep=';', index_col=0)
df_200 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/2-0-0.csv', sep=';', index_col=0)
df_201 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/2-0-1.csv', sep=';', index_col=0)
df_202 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/2-0-2.csv', sep=';', index_col=0)
df_210 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/2-1-0.csv', sep=';', index_col=0)
df_211 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/2-1-1.csv', sep=';', index_col=0)
df_212 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/2-1-2.csv', sep=';', index_col=0)
df_221 = pd.read_csv('./kmeans_manual/3ª Avaliação/kmeans/2-2-1.csv', sep=';', index_col=0)

df_02 = pd.read_csv('./kmeans_manual/3ª Avaliação/df_original-0-2.csv', sep=';', index_col=0)
df_02 = df_02.loc[df_02['Valor'] == 2]

df_10 = pd.read_csv('./kmeans_manual/3ª Avaliação/df_original-1-0.csv', sep=';', index_col=0)
df_10 = df_10.loc[df_10['Valor'] == 0]

df_11 = pd.read_csv('./kmeans_manual/3ª Avaliação/df_original-1-1.csv', sep=';', index_col=0)
df_11 = df_11.loc[df_11['Valor'] == 0]

df_22 = pd.read_csv('./kmeans_manual/3ª Avaliação/df_original-2-2.csv', sep=';', index_col=0)
df_22 = df_22.loc[df_22['Valor'] == 0]

df_22 = pd.read_csv('./kmeans_manual/3ª Avaliação/df_original-2-2.csv', sep=';', index_col=0)
df_22 = df_22.loc[df_22['Valor'] == 2]

df_resultado = pd.DataFrame(columns=['Texto', 'Valor'])

df_resultado = pd.concat([df_resultado, df_000], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_001], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_002], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_010], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_011], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_012], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_020], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_021], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_101], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_102], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_111], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_112], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_120], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_121], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_122], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_200], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_201], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_202], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_210], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_211], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_212], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_221], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_02], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_10], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_11], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_22], ignore_index=True)
df_resultado = pd.concat([df_resultado, df_22], ignore_index=True)
df_resultado = df_resultado.sort_values(by='Valor')
df_resultado = df_resultado.reset_index(drop='index')

df_resultado.to_csv('./kmeans_manual/df_resultado_final.csv', sep=';')
print(df_resultado)