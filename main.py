import time
import random
from scraper import create_driver, check_stock_bershka
from notifier import send_telegram_message
from config import PRODUCTS  # config.py'deki PRODUCTS listesini kullan

sleep_min_seconds = 15  # Örnek: minimum bekleme 1 dk
sleep_max_seconds = 30  # Örnek: maksimum bekleme 2 dk

while True:
    driver = create_driver()
    try:
        for item in PRODUCTS:
            url = item.get("url")
            sizes_to_check = [item.get("size")]
            size_in_stock = check_stock_bershka(driver, url, sizes_to_check)
            if size_in_stock:
                message = f"🛍️ {size_in_stock} beden stokta!\nLink: {url}"
                print(message)
                send_telegram_message(message)
                break
            else:
                print(f"No stock found for {url} sizes {', '.join(sizes_to_check)}")
        else:
            # Eğer hiçbir ürün bulunmadıysa bekleyip tekrar kontrol
            sleep_time = random.randint(sleep_min_seconds, sleep_max_seconds)
            print(f"Sleeping for {sleep_time} seconds...")
            time.sleep(sleep_time)
            continue  # while döngüsüne devam

            # break ile buraya gelirse, ürün bulundu ve program sonlanacak

        break
    finally:
        driver.quit()