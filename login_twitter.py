from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

exe_path = GeckoDriverManager().install()
service=Service(exe_path)
browser = webdriver.Firefox(service=service)

# usuario = input("Usuário do Twitter: ")
# senha = input("Senha do Twitter: ")

usuario = "PI445204567"
senha = "projetointegradoriv"

browser.get("https://twitter.com/login")
print("Acessou o Twitter...")
sleep(3)

try:
    campo_nome_usuario = browser.find_element(by=By.XPATH, value="//input[contains(@name,'text')]")    
    campo_nome_usuario.click()
    campo_nome_usuario.send_keys(usuario)
    campo_nome_usuario.send_keys(Keys.RETURN)
    print("Entrou com o nome de usuário...")
    sleep(2)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)

try:
    campo_senha = browser.find_element(by=By.XPATH, value="//input[contains(@name,'password')]")    
    # campo_senha.click()
    campo_senha.send_keys(senha)
    campo_senha.send_keys(Keys.RETURN)
    print("Entrou com a senha de usuário...")
    sleep(1)
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)

try:
    botao_pesquisa = browser.find_element(by=By.XPATH, value="//a[contains(@data-testid, 'AppTabBar_Explore_Link')]")
    sleep(2)
    botao_pesquisa.click()
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)

try:
    botao_pesquisa_avancada = browser.find_element(by=By.XPATH, value="//a[contains(@data-testid, 'settingsAppBar')]")
    sleep(2)
    botao_pesquisa_avancada.click()
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)

try:
    input_pesquisa = browser.find_element(by=By.XPATH, value="//input[contains(@data-testid, 'SearchBox_Search_Input')]")
    input_pesquisa.click()
    input_pesquisa.send_keys("Eleições 2022")
    input_pesquisa.send_keys(Keys.RETURN)
    print("Entrou com o input")
    sleep(2)    
except Exception as excpt:
    print(f"Tivemos uma falha: {excpt}")
    browser.quit()
    exit(1)



print("Pronto!")
input("Pressione enter para sair...")
browser.quit()
print("Fim...")