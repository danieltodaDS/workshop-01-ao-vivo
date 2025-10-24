from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True # Executar em modo headless 
    driver = webdriver.Firefox(options = options)
    # Iniciar o Webdriver usando GeckoDriver
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o Webdriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):
    driver.get("http://localhost:8501")
    sleep(2)

def test_check_title_is (driver): 
    # Verifica se a pagina abre
    driver.get("http://localhost:8501")
    
    sleep(2)
    page_title = driver.title

    expected_title = "Validador de schema excel"
    assert page_title == expected_title

def test_check_streamlit_h1 (driver): 
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(2)  # Espera 5 segundos

    # Capturar o primeiro elemento <h1> da página
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verificar se o texto do elemento <h1> é o esperado
    expected_text = "Validador de schema excel"
    assert h1_element.text == expected_text