# Importar bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# Navegar até o whats web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
sleep(30)
# Definir mensagens e pessoas/grupos a ser enviadas
contatos = ['', ''] # Coloque o nome do contato ou grupo entre as aspas, caso queira colocar apenas um nome apegue um par de aspas e a vírgula
mensagem = 'Teste do BOT'
# Buscar pelo nome do grupo/pessoa
def buscar_contato(contato):
    pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    sleep(3)
    pesquisa.click()
    pesquisa.send_keys(contato)
    pesquisa.send_keys(Keys.ENTER)
    sleep(3)


def enviar_mensagem(mensagem):
    msg = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    msg[1].click()
    sleep(3)
    msg[1].send_keys(mensagem)
    msg[1].send_keys(Keys.ENTER)
    sleep(3)


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
    # Campo de pesquisa: copyable-text selectable-text
    # Campo de mensagem: copyable-text selectable-text
# Enviar mensagem para o grupo/pessoa
