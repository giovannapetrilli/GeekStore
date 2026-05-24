from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_compra_e2e():

    options = webdriver.ChromeOptions()

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

    driver.get("http://localhost:8000")

    driver.find_element(By.ID, "input-produto").send_keys("teclado")

    driver.find_element(By.ID, "input-cartao").send_keys("1234")

    driver.find_element(By.ID, "input-cupom").send_keys("GEEK20")

    driver.find_element(By.ID, "btn-comprar").click()

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, "mensagem"),
            "Compra aprovada"
        )
    )

    mensagem = driver.find_element(By.ID, "mensagem")

    assert "Compra aprovada" in mensagem.text

    driver.quit()