from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(options=options,service=service)
nav.get("https://web.whatsapp.com")
sleep(30)
message = """Ola, a AFC TECHNOLOGY Store está com promoções imperdíveis, produtos a partir de R$:50,00 e taxa de entrega gratuita para o bairro do São Cristóvão, João de Deus e Vila Brasil, para outros bairros, consultar taxa. 
"""
lista_contatos = ["Grupo teste1","Amadeu Chaves","Grupo teste2","Grupo teste3","REMINDER z", "REMINDER demandas ENOVA"]

#Clicar na lupa:
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys("AFC TECHNOLOGY STORE")
nav.find_element('xpath','//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
pyperclip.copy(message)
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.CONTROL + "v")
nav.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p').send_keys(Keys.ENTER)
sleep(5)

qtde_contatos = len(lista_contatos)

if qtde_contatos % 5 == 0:
    qtd_blocos = qtde_contatos / 5
else:
    qtd_blocos = int(qtde_contatos / 5) + 1

for i in range(qtd_blocos):
    i_inicial = i * 5 
    i_final = (i + 1) * 5 
    lista_envio = lista_contatos[i_inicial:i_final]

    lista_elementos = nav.find_elements('class name', '_2AOIt')
    for item in lista_elementos:
        message = message.replace("\n","")
        texto = item.text.replace("\n","")
        if message in texto:
            caixa = item

    ActionChains(nav).move_to_element(item).perform()
    item.find_element('class name', '_3u9t-').click()
    sleep(0.5)
    nav.find_element('xpath','//*[@id="app"]/div/span[4]/div/ul/div/li[4]/div').click()
    sleep(0.5)
    nav.find_element('xpath','//*[@id="main"]/span[2]/div/button[5]/span').click()
    sleep(1)

    for nome in lista_envio:
        nav.find_element('xpath','//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(nome)
        sleep(1)
        nav.find_element('xpath','//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        sleep(1)
        nav.find_element('xpath','//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[1]/p').send_keys(Keys.BACKSPACE)
        sleep(1)
    nav.find_element('xpath','//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    sleep(3)
