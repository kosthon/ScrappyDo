from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
import json
from datetime import datetime

# Opciones de navegación
options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

# Instalar automáticamente el ChromeDriver
ChromeDriverManager().install()

# Inicializar el navegador
driver = webdriver.Chrome(options=options)

driver.get(
    'https://www.windy.com/es/-Presi%C3%B3n-pressure?pressure,4.971,-71.785,7,m:dMwad5M')

# Obtener información de la página

# Esperar a que el elemento de temperatura sea visible
temperatura_element = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'big[data-do="changeMetric"]'))
)
temperatura = temperatura_element.text

humedad = "70%"
presion = "25°C"
# Guardar información en un archivo

# Ruta del archivo
ruta_archivo = "datos.csv"

# Abrir el archivo en modo escritura, utilizando el modo "append"
with open(ruta_archivo, "a", newline="") as archivo_csv:
    # Crear un objeto escritor CSV
    escritor_csv = csv.writer(archivo_csv, dialect='excel-tab')

    # Escribir los titulos
    escritor_csv.writerow([temperatura, humedad, presion])
print("Datos guardados en el archivo:", ruta_archivo)

# Crear un diccionario con los datos
datos = {
    "temperatura": temperatura,
    "humedad": humedad,
    "presion": presion
}

# Ruta del archivo JSON
ruta_archivojson = "datos.json"

try:
    with open(ruta_archivojson, "r") as archivo_json:
        consultas_previas = json.load(archivo_json)
except FileNotFoundError:
    consultas_previas = []

# Generar un identificador único para la nueva consulta
identificador = len(consultas_previas) + 1

# Agregar los datos de la consulta actual al diccionario existente
consulta_actual = {
    "temperatura": temperatura,
    "humedad": humedad,
    "presion": presion
}

consultas_previas[identificador] = consulta_actual

# Guardar el diccionario actualizado en el archivo JSON
with open(ruta_archivojson, "w") as archivo_json:
    json.dump(consultas_previas, archivo_json)

print("Datos guardados en el archivo JSON:", ruta_archivojson)

# Cerrar el navegador
driver.quit()
