from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
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

driver.get('https://google.com')

# Esperar a que el elemento sea clickable
textarea = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea.gLFyf'))
)

# Hacer clic en el elemento
textarea.click()

# Escribir en el elemento
textarea.send_keys('CODALTEC')

# Dar click en el boton buscar
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.gNO89b'))
)

button.click()

# Pausa de 5 segundos para visualizar el resultado
time.sleep(5)