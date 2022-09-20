from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
# import csv

exe_path = GeckoDriverManager().install()
service=Service(exe_path)
browser = webdriver.Firefox(service=service)
# browser = webdriver.Chrome(service=service)

URLS_Pesquisa = [
    "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A2022-01-31%20since%3A2022-01-01&src=typed_query",
    "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A2022-02-28%20since%3A2022-02-01&src=typed_query",
    "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A2022-03-31%20since%3A2022-03-01&src=typed_query",
    "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A2022-04-30%20since%3A2022-04-01&src=typed_query",
    "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A2022-05-31%20since%3A2022-05-01&src=typed_query",
    "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A2022-06-30%20since%3A2022-06-01&src=typed_query",
    "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A2022-07-31%20since%3A2022-07-01&src=typed_query",
    "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A2022-08-31%20since%3A2022-08-01&src=typed_query",
    "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A2022-09-06%20since%3A2022-09-01&src=typed_query"
]

Meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro"]

def busca_avancada(url):
    try:
        url_busca_avancada = url
        browser.get(url_busca_avancada)
        print("Iniciou a busca avançada")
        sleep(8)
    except Exception as excpt:
        print(f"Tivemos uma falha: {excpt}")
        browser.quit()
        exit(1)
# --------------------

def gerador_url_diaria(mes):
    parte1 = "https://twitter.com/search?q=(elei%C3%A7%C3%A3o%20OR%20elei%C3%A7%C3%B5es%20OR%20presidente%20OR%20candidato%20OR%20candidatos)%20lang%3Apt%20until%3A"
    parte2 = "%20since%3A"
    parte3 = "&src=typed_query"
    numero_do_mes_escolhido = mes
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
    # print(urls)
    return urls
# --------------------


# Essa função pode ser utilizada para exportar para CSV caso seja necessário 
''' 
  ┌──────────────────────────────────────────────────────────────────────────┐
  │ # WRITE CSV                                                              │
  │ def write_csv(date,tweet,name):                                          │
  │     with open("twitterData.csv", "a+") as csv_file:                      │
  │         fieldnames = ['Date', 'Name', 'Tweets','Tags']                   │
  │         writer = DictWriter(csv_file, fieldnames=fieldnames)             │
  │         #writer.writeheader()                                            │
  │         writer.writerow({'Date': date,'Name': name,'Tweets': tweet})     │
  │ # --------------------                                                   │
  └──────────────────────────────────────────────────────────────────────────┘
 '''

# usuario = input("Usuário do Twitter: ")
# senha = input("Senha do Twitter: ")

usuario = "PI445204567"
senha = "projetointegradoriv"

browser.get("https://twitter.com/login")
print("Acessou o Twitter...")
sleep(5)

# LOGIN 
try:
    campo_nome_usuario = browser.find_element(by=By.XPATH, value="//input[contains(@name,'text')]")    
    campo_nome_usuario.click()
    campo_nome_usuario.send_keys(usuario)
    campo_nome_usuario.send_keys(Keys.RETURN)
    print("Entrou com o nome de usuário...")
    sleep(5)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)
# --------------------

# SENHA
try:
    campo_senha = browser.find_element(by=By.XPATH, value="//input[contains(@name,'password')]")    
    # campo_senha.click()
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)
    print("Entrou com a senha de usuário...")
    sleep(6)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)
# --------------------

for url in URLS_Pesquisa:
    busca_avancada(url)

    try:
        index = 0
        last_height = 0
        aux = ''
        for i in range(1, 10):
            
            # SCRAPING
            try:
                tweet_divs = browser.page_source
                obj = BeautifulSoup(tweet_divs, "html.parser")
                
                try:
                    content = obj.find_all("div", {"data-testid": "cellInnerDiv"})
                    # content = browser.find_element(by=By.XPATH, value="//div[contains(@data-testid,'cellInnerDiv')]")
                    
                    for c in content:
                        if (c != aux):
                            try:
                                aux = c
                                tweets = c.find("div", {"data-testid": "tweetText"}).strings
                                tweet_text = "".join(tweets)
                                print(tweet_text)
                                print("-----------")
                                index += 1

                                try:
                                    # WRITE TO .TXT
                                    file_name = f"tweet_{Meses[URLS_Pesquisa.index(url)]}_{index}.txt"
                                    myfile = open(f"tweets/{file_name}", 'w')
                                    myfile.write(tweet_text)

                                    # WRITE TO CSV
                                    # with open('tweets-teste.csv', 'w') as csv_file:
                                        # csv_file.write(tweet_text)

                                except Exception as e:
                                    print(f"Tivemos uma falha: {e}")
                                finally:
                                    # SCROLL DOWN
                                    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                                    # WAIT FOR THE PAGE TO LOAD
                                    sleep(3)

                                    # CALCULATE NEW SCROLL HEIGHT
                                    new_height = browser.execute_script("return document.body.scrollHeight")

                                    if new_height == last_height:
                                        break
                                    last_height = new_height
                                    # --------------------

                            except Exception as e:
                                print("Erro ao achar tweets")
                                print(f"Tivemos uma falha: {e}")
                        else:
                            print("-- TWEET REPETIDO --")
                        
                except Exception as e:
                    print('Erro ao procurar content')
                    print(f"Tivemos uma falha: {e}")

            except Exception as e:
                print("Erro ao iniciar scraping!")
                print(f"Tivemos uma falha: {e}")
                browser.quit()
            # --------------------
            
    except Exception as e:
        print(f"Tivemos um problema: {e}")

print("Script finalizado!")
browser.quit()
print("Fim...")