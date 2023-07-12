from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
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
    # latitud = input("Ingresa la latitud: ")
    # longitud = input("Ingresa la longitud: ")

# Esperar a que el elemento sea clickable
textarea = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#q'))
)

# Hacer clic en el elemento
textarea.click()

time.sleep(3)

# Escribir en el elemento
textarea.send_keys("6.1622, -73.8117")
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
print(numberGrades)

# Pausa de 5 segundos para visualizar el resultado
time.sleep(10)
