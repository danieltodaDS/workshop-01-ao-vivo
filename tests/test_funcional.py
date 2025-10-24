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
