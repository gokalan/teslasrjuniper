import requests
import time
import os

TOKEN = os.getenv('TOKEN')  # Bot token'ınızı çevresel değişkenlerden alıyoruz
CHAT_ID = os.getenv('CHAT_ID')  # Chat ID'yi çevresel değişkenlerden alıyoruz
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

def send_message(text):
    params = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.get(URL, params=params)
    return response.json()

while True:
    send_message("Test mesajı - Bot çalışıyor!")  # Her 5 dakikada bir mesaj gönder
    time.sleep(300)  # 5 dakika bekle
