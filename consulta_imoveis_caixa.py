from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Atualize aqui o caminho completo para o ChromeDriver
CAMINHO_DRIVER = "chromedriver.exe"

# URL do site da Caixa
URL_CAIXA = "https://venda-imoveis.caixa.gov.br/sistema/busca-imovel.asp"

# Estado que você deseja consultar
ESTADO = "SP"

# Função para automatizar o download
def baixar_arquivo_com_selenium(estado):
    driver = None
    try:
        # Configurando o WebDriver usando Service
        service = Service(executable_path= CAMINHO_DRIVER)
        driver = webdriver.Chrome(service=service)
        driver.get(URL_CAIXA)

        # Esperar o site carregar
        time.sleep(3)

        # Selecionar o estado no dropdown
        dropdown = Select(driver.find_element(By.ID, "sltBuscaUF"))
        dropdown.select_by_value(estado)
        print(f"Estado {estado} selecionado.")

        # Submeter o formulário para gerar o arquivo
        botao_buscar = driver.find_element(By.ID, "btnBuscar")
        botao_buscar.click()
        print("Requisição enviada para gerar o arquivo.")

        # Esperar pelo download do arquivo (ajuste o tempo, se necessário)
        time.sleep(10)

        print("Verifique se o arquivo foi baixado com sucesso na pasta de downloads.")
    except Exception as e:
        print(f"Erro durante o processo: {e}")
    finally:
        # Fechar o navegador apenas se ele foi iniciado
        if driver:
            driver.quit()

# Executar o processo
if __name__ == "__main__":
    baixar_arquivo_com_selenium(ESTADO)
