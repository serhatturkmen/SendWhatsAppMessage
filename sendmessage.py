from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# Qr Code un okutulması için 10 saniye beklwtiliyor.
time.sleep(10)

names = input('Kullanıcı Adı veya Grup Adını giriniz (birden fazla ise virgül ile ayırınız) : ')
name =[]

# Girilen isimler vigüller ile ayrılarak bir diziye ekleniyor
for data in names.split(','):
    name.append(data)

msg = input('Mesajını gir : ')
count = int(input('Mesajınız kaç kere atılsın : '))
wait = WebDriverWait(driver = driver, timeout = 900)

# Kişi listesi döngüsü
for dataname in name:
    # Kişinin sohbet butonu bulunuyor
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(dataname))
    
    # Sohbet butonuna basılıp sohbeti açılıyor
    user.click()

    # Mesaj yazma inputunu bul
    msg_box = driver.find_element_by_xpath('//div[@data-tab=6]')

    # Mesaj Gönderme Tekrar Döngüsü
    for i in range(count):
            # mesak Giriliyor
            msg_box.send_keys(msg)
            # Gönder butonu bulunuyor
            button = driver.find_element_by_class_name('_2Ujuu')
            # Gönder butonuna bas
            button.click()

wait = WebDriverWait(driver = driver, timeout = 600)
# Tarayıcı kapatılıyor
driver.close()
