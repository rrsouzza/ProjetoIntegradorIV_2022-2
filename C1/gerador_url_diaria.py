parte1 = "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A"
parte2 = "%20since%3A"
parte3 = "&src=typed_query"
datas = []
numero_do_mes_escolhido = 7
urls = []
start = 0

if (numero_do_mes_escolhido == 2):
    start = 28
elif ((numero_do_mes_escolhido == 4) or (numero_do_mes_escolhido == 6) or (numero_do_mes_escolhido == 9) or (numero_do_mes_escolhido == 11)):
    start = 30
else:
    start = 31
    
if (numero_do_mes_escolhido < 10):
    mes = "0" + str(numero_do_mes_escolhido)
else:
    mes = numero_do_mes_escolhido
    
for i in range(start, 0, -1):
    # Desconsiderando se é ano bissexto
    dia = ""
    dia_mais_um = ""
    if (i < 10):
        dia = "0" + str(i)
        dia_mais_um = "0" + str(i + 1)
    else:
        dia = i
        dia_mais_um = str(i + 1)
    # if (i == 28):

    if ((start == 28 and i == 28) or (start == 30 and i == 30) or (start == 31 and i == 31)):
        urls.append(parte1 + "2022-" + "0" + str(int(mes) + 1) + "-01" + parte2 + "2022-" + str(mes) + "-" + str(dia) + parte3)    
    else:
        urls.append(parte1 + "2022-" + str(mes) + "-" + str(dia_mais_um) + parte2 + "2022-" + str(mes) + "-" + str(dia) + parte3)
print(urls)
