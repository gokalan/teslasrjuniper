
import requests
import time

# Ayarlar
TOKEN = '7565925742:AAHHs2rTaHtiPFojuSa7OZo-shlzFanWg5g'
CHAT_ID = KENDI_CHAT_IDINI_YAZ  # Buraya kendi chat_id’ni yaz

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

# Sürekli mesaj gönderme testi (5 dakikada bir örnek mesaj gönderir)
if __name__ == "__main__":
    while True:
        send_message("Merhaba! Bot çalışıyor.")
        time.sleep(300)  # 5 dakika bekle
