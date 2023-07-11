from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Opciones de navegación
options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

# Instalar automáticamente el ChromeDriver
ChromeDriverManager().install()

# Inicializar el navegador
driver = webdriver.Chrome(options=options)

driver.get('https://www.windy.com/es/-Presi%C3%B3n-pressure?pressure,42.163,-64.863,3,m:eM0adx7')

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
textarea.send_keys(latitud + ',' + longitud)
textarea.send_keys(Keys.ENTER)
time.sleep(2)
textarea.send_keys(Keys.ENTER)
time.sleep(2)
textarea.send_keys(Keys.ENTER)
time.sleep(3)

# ciudad = driver.find_element_by_xpath('//div[@data-label="Bogotá" and @class="city-1"]')

# ciudad.click()

# Dar click en el boton buscar
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.gNO89b'))
)

button.click()

# Dar click en el link de CODALTEC
link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'h3.LC20lb'))
)

link.click()


# Pausa de 5 segundos para visualizar el resultado
time.sleep(10)