from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import os
import re
import json
import pandas as pd
import pyautogui

# Opciones de navegación
options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_argument('--incognito') 

# Instalar automáticamente el ChromeDriver
ChromeDriverManager().install()

# Inicializar el navegador
driver = webdriver.Chrome(options=options)

driver.get('https://www.windy.com/es/-Temperatura-temp?temp')

# Digitar coordenadas
latitud = input("Ingresa la latitud: ")
longitud = input("Ingresa la longitud: ")

# Esperar a que el elemento sea clickable
textarea = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#q'))
)

# Hacer clic en el elemento
textarea.click()

time.sleep(3)

# Escribir en el elemento
textarea.send_keys(latitud + ', ' + longitud)
textarea.send_keys(Keys.ENTER)
time.sleep(3)
textarea.send_keys(Keys.ENTER)
time.sleep(5)

# Dar click en el dot del punto en el mapa
# Realizar la acción de clic derecho utilizando pyautogui
dotElement = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.leaflet-marker-icon.icon-dot'))
)

def perform_right_click(element):
    # Obtener la posición del elemento en la ventana del navegador
    location = element.location
    x = location['x']
    y = location['y'] + 120

    # Simular el clic derecho utilizando pyautogui
    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')
    

perform_right_click(dotElement)
time.sleep(3)

temperatureOption = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-do="picker"]'))
)

temperatureOption.click()
time.sleep(3)

# Tomar los grados del picker
pickerGrades = driver.find_element(By.CSS_SELECTOR, 'div.picker-content span[data-ref="content"] big[data-do="changeMetric"]')
numberGrades = pickerGrades.text.split()[0]
print('Grados: ' + numberGrades)

# Pausa de 5 segundos para visualizar el resultado
time.sleep(5)


# CAPTURA DE DATOS DE PRESIÓN ATMÓSFERICA
driver.get('https://www.windy.com/es/-Presi%C3%B3n-pressure?pressure')

# Esperar a que el elemento sea clickable
textarea = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#q'))
)

# Hacer clic en el elemento
textarea.click()
time.sleep(3)

# Escribir en el elemento
textarea.send_keys(latitud + ', ' + longitud)
textarea.send_keys(Keys.ENTER)
time.sleep(3)
textarea.send_keys(Keys.ENTER)
time.sleep(5)

# Dar click en el dot del punto en el mapa
# Realizar la acción de clic derecho utilizando pyautogui
dotElement = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.leaflet-marker-icon.icon-dot'))
)

def perform_right_click(element):
    # Obtener la posición del elemento en la ventana del navegador
    location = element.location
    x = location['x']
    y = location['y'] + 120

    # Simular el clic derecho utilizando pyautogui
    pyautogui.moveTo(x, y)
    pyautogui.click(button='right')
    

perform_right_click(dotElement)
time.sleep(3)

presionOption = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-do="picker"]'))
)

presionOption.click()
time.sleep(3)

# Tomar la presion del picker
pickerPresion = driver.find_element(By.CSS_SELECTOR, 'div.picker-content span[data-ref="content"] big[data-do="changeMetric"]')
numberPresion = pickerPresion.text.split()[0]
print('Presion: ' + numberPresion)

time.sleep(5)


# CAPTURAR DATOS DE CELASTRAK
driver.get('https://celestrak.org/NORAD/elements/gp.php?CATNR=56205')

# Esperar a que el elemento sea clickable
celastrak_element = driver.find_element(By.CSS_SELECTOR, 'pre')
textoCelastrak = celastrak_element.text
time.sleep(3)
textoCelastrak = textoCelastrak.replace("FACSAT-2", "")
textoCelastrak = re.sub(r"^\d\s", "", textoCelastrak, flags=re.MULTILINE)
textoCelastrak = textoCelastrak.strip()
print('Celastrak: ' + textoCelastrak)
time.sleep(5)


# CAPTURA DE DATOS DE UNIXTIMESTAMP
driver.get('https://www.unixtimestamp.com/')

inputTimestamp = driver.find_element(By.CSS_SELECTOR, 'input#timestamp')

hora_juliana_element = driver.find_element(By.CSS_SELECTOR, 'div.epoch')
hora_juliana = hora_juliana_element.text
inputTimestamp.click()
time.sleep(3)
inputTimestamp.send_keys(hora_juliana)
time.sleep(1)
inputTimestamp.send_keys(Keys.ENTER)
time.sleep(3)

hora_element = driver.find_element(By.CSS_SELECTOR, 'span#hour1')
minuto_element = driver.find_element(By.CSS_SELECTOR, 'span#minute1')
segundo_element = driver.find_element(By.CSS_SELECTOR, 'span#second1')
hora_local_element = driver.find_element(By.CSS_SELECTOR, 'td.local')

hora = hora_element.text
minuto = minuto_element.text
segundo = segundo_element.text
horaUTC = hora + ':' + minuto + ':' + segundo

horaLocal = hora_local_element.text

print('Hora local: ' + horaLocal)
print('Hora Juliana: ' + hora_juliana)
print('Hora UTC: ' + horaUTC)

time.sleep(5)

# CAPTURA DE DATOS DESDE N2YO
driver.get('https://www.n2yo.com/?s=56205')

altitud_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#sataltkm'))
)
elevation_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#satel'))
)

altitud = altitud_element.text
elevation = elevation_element.text

time.sleep(5)

# 5.934299471956952, -73.61576533067957

# EXPORTACIÓN DE DATA A ARCHIVOS EXCEL
# Ruta del archivo
ruta_archivo = "datos.csv"
# Crear una lista con los elementos individuales a escribir en cada columna
fila = [numberGrades, numberPresion, textoCelastrak, horaLocal, hora_juliana, horaUTC, altitud, elevation]
# Abrir el archivo CSV en modo escritura, utilizando el modo "append"
with open(ruta_archivo, "a", newline="") as archivo_csv:
    # Crear un objeto escritor CSV con el delimitador de coma
    escritor_csv = csv.writer(archivo_csv, delimiter=',')
    # Escribir la fila en el archivo CSV
    escritor_csv.writerow(fila)
print("Datos guardados en el archivo:", ruta_archivo)

time.sleep(5)

