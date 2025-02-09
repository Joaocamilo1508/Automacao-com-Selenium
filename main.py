from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver
from datetime import datetime
from time import sleep
import pandas as pd

drive = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

drive.get('https://economia.uol.com.br/cotacoes/bolsas/')

empresas = ['PETR3.SA', 'MGLU3.SA', 'VIVT3.SA']
valor = list()
data_hora = list()

for empresa in empresas:
    input_busca = driver.find_element(By.ID, 'filled-normal')
    input_busca.send_keys(empresa)
    sleep(5)

    input_busca.send_keys(Keys.ENTER)
    sleep(5)

    span_val = driver.find_element(By.XPATH, '//span[@class="chart-info-val ng-binding"]')
    cotacao_valor = span_val.text

    valor.append(cotacao_valor)
    data_hora.append(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))


dados = {
    'empresas': empresas,
    'valor': valor,
    'data_hora': data_hora
}

dataframe = pd.DataFrame(dados)
dataframe.to_excel('./empresas.xlsx')





input('')