# 🛍️ Bershka Stock Notifier Bot

Bu proje, **Bershka web sitesindeki belirli ürünlerin stok durumunu otomatik olarak takip eden** bir Python botudur.  
Belirlenen ürün ve beden stokta bulunduğunda **Telegram üzerinden bildirim gönderir**.

---

## 🚀 Özellikler
- 🔍 Selenium ile otomatik web scraping  
- 👕 Belirli ürün URL’lerini ve bedenleri `config.py` üzerinden tanımlama  
- ⏳ Rastgele zaman aralıklarıyla (örn. 15-30 sn) tekrar kontrol  
- 📩 Stok bulunduğunda Telegram mesajı gönderme  
- 🖥️ Headless Chrome desteği (arka planda tarayıcı açmadan çalışır)  

---

## ⚙️ Kurulum

1. Bu projeyi klonla:
   ```bash
   git clone https://github.com/kullaniciadi/bershka-stock-bot.git
   cd bershka-stock-bot
   ```

2. Gerekli kütüphaneleri yükle:
   ```bash
   pip install -r requirements.txt
   ```

3. `config.py` dosyasını düzenle:
   ```python
   PRODUCTS = [
       {
           "url": "https://www.bershka.com/tr/erkek/pantalon-c0p102526285.html",
           "size": "M"
       },
       {
           "url": "https://www.bershka.com/tr/kadin/tshirt-c0p123456789.html",
           "size": "S"
       }
   ]

   TELEGRAM_BOT_TOKEN = "BOT_TOKENINIZ"
   TELEGRAM_CHAT_ID = "CHAT_IDINIZ"
   ```
## Telegram Üzerinden Bildirim Alabilmek İçin
-BotFather üzerinden /newbot ile bir bot oluşturun ve botunuza bir isim verin.
 Daha sonra bot size bir api key verecek bu api key'i kopyalayın ve telegram üzerinden botunuza bir mesaj gönderin örn(merhaba).
 Https://api.telegram.org/bot"apikey buraya yazılacak"/getUpdates vermiş olduğum bağlantı adresindeki belirli kısma api keyinizi girin ve tırnak işaretlerini silin.
Hazırlamış olduğunuz linki bir web tarayıcısına yapıştırın ve karşınıza çıkan telegram id'si botunuzun size vermiş olduğu api key'i config.py dosyasındaki ilgili kısıma yapıştırın böylelikle telegram üzerinden stok mevcut olduğunda bildirim alabilirsiniz.


---

## ▶️ Kullanım

Botu çalıştırmak için:
```bash
python main.py
```

Program belirlediğiniz ürünleri takip eder, stok bulunduğunda **Telegram üzerinden anlık bildirim gönderir.**

---

## 📸 Çalışma Mantığı

- Bot Selenium kullanarak ürün sayfasını açar  
- İlgili bedenin stok durumunu kontrol eder  
- Eğer stok bulunursa:  
  - Konsola mesaj basar  
  - Telegram’a bildirim yollar  
- Stok yoksa, belirlenen süre bekler ve tekrar dener   

---

## 🛠 Kullanılan Teknolojiler
- [Python 3](https://www.python.org/)  
- [Selenium](https://www.selenium.dev/)  
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)  
- [Telegram Bot API](https://core.telegram.org/bots/api)  

---

## 📄 Not
Bu proje kişisel kullanım için geliştirilmiştir ve herhangi bir ticari amacı yoktur. 
