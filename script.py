import pandas as pd
from genericpath import exists
import os
import time
import pandas as pd
import sys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
from webdriver_manager.chrome import ChromeDriverManager
from win10toast_click import ToastNotifier
import win32com.client as win32


options = Options()
options.page_load_strategy = 'eager'
options.headless = False
options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

pesquisa = input('O que deseja pesquisar? ')

driver.get('https://google.com.br')

driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(pesquisa)
driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

quer_ir = int(input('Até que página você quer ir?'))

pag_atual = driver.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div/div[6]/span[1]/table/tbody/tr/td[2]').text

pag_atual = int(pag_atual)

lista_resultados = []

while pag_atual <= quer_ir:

    divs = driver.find_elements(By.CLASS_NAME,'g')

    i = 1

    for elemento in divs:
        try:
            titulo = elemento.find_element(By.TAG_NAME,'h3').text
        except:
            ...

        try:
            link = elemento.find_element(By.TAG_NAME,'a').get_attribute('href')
        except:
            ...
        resultados = "%s '---------' %s" % (titulo,link)
        lista_resultados.append(resultados)
        


    driver.find_element(By.XPATH,'/html/body/div[7]/div/div[10]/div/div[6]/span[1]/table/tbody/tr/td[11]/a').click()
    
    pag_atual += 1 

with open("resultados.txt", "w") as arquivo:
    for resultados in lista_resultados:
        arquivo.write("%s\n" % resultados)

driver.close()