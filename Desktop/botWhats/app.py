import pandas as pd
import schedule
import re
import urllib.request
import requests
import os
from time import sleep, strftime, gmtime
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Solucionar erros do Chrome
options = Options()
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_experimental_option("useAutomationExtension",False)
driver = webdriver.Chrome(ChromeDriverManager().install())
options.add_experimental_option("useAutomationExtension", False)
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-certificate-errors') # Argumento para ignorar erro de certificado
options.add_argument('--ignore-ssl-errors') # Argumento para ignorar erro de ssl

# Entrar na url do WhatsApp Web
driver.get('https://web.whatsapp.com/')
WebDriverWait(driver, 30) # Espera a página carregar por 30 segundos
name = 'Anotações'
str(input("Depois de ter passado o QR Code dê um OK: "))