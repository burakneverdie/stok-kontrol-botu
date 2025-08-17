from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    )
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def check_stock_bershka(driver, url, sizes_to_check):
    """
    Belirtilen bedenlerin stokta olup olmadığını kontrol eder.
    Dönen değer: stokta olan bedenin adı (ör: "M") veya None
    """
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 15)

        # Cookie popup varsa kapat
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            accept_cookies_button.click()
        except TimeoutException:
            pass

        # Beden listesinin yüklenmesini bekle
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-qa-anchor='productDetailSize']")))
        time.sleep(2)  # JS yüklemesini bekle

        size_buttons = driver.find_elements(By.CSS_SELECTOR, "button[data-qa-anchor='sizeListItem']")
        for button in size_buttons:
            try:
                size_label_elem = button.find_element(By.CSS_SELECTOR, "span.text__label")
                size_label = size_label_elem.text.strip()

                if size_label in sizes_to_check:
                    class_attr = button.get_attribute("class")
                    if "is-disabled" in class_attr:
                        print(f"{size_label} stokta değil.")
                        return None
                    else:
                        return size_label  # Stokta olan bedeni döndür
            except Exception:
                continue

    except Exception as e:
        print(f"Bershka scraper error: {e}")

    return None  # stok yoksa None döndür
