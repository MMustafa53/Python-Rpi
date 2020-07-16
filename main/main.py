from guizero import *
from gpiozero import LED

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)
pwm = GPIO.PWM(2, 100)
pwm.start(0)
freq = 0
sure = 15
cevaplar = {"s1_cevap": "",
            "s2_cevap": "",
            "s3_cevap": "",
            "s4_cevap": "",
            "s5_cevap": ""}
led = LED(17)

def geri_bir():
    sb1window.hide()
    app.show()


def geri_iki():
    sb2window.hide()
    sb1window.show()


def geri_uc():
    sb3window.hide()
    sb2window.show()


def geri_dort():
    sb4window.hide()
    sb3window.show()


def geri_bes():
    sb5window.hide()
    sb4window.show()


def ileri_view():
    app.hide()
    ileri_window.show()


def iptal_view():
    app.show()
    ileri_window.hide()


def islem_view():
    print('islem yapıldı')
    islem_text_sure.value = sure
    islem_text_sure.visible = True
    islem_text_sure.repeat(1000, count_islem)
    ileri_window.hide()
    islem_window.show()


def acil_islem():
    print('acil durum')
    islem_text_sure.value = int(islem_text_sure.value) + 10


def onay_view():
    onay_buton.enabled = False
    iptal_buton.enabled = False
    onay_sn_text.visible = True
    saniye = 2
    saniye_text.value = saniye
    saniye_text.repeat(1000, count_down)
    saniye_text.after(2000, islem_view)
    saniye_text.visible = True
    print(saniye)
    print(cevaplar)


def count_down():
    if int(saniye_text.value) > 0:
        saniye_text.value = int(saniye_text.value) - 1


def stop_app():
    app.destroy()


def count_islem():
    if int(islem_text_sure.value) > 0:
        islem_text_sure.value = int(islem_text_sure.value) - 1
    else:
        islem_window.hide()
        islem_son_window.show()
        islem_son_text.visible = True


def sterilizasyon_view():
    app.hide()
    oto_window.show()


def manuel_sterilizasyon_view():
    print(cevaplar)
    app.hide()
    sb1window.show()


def close_window_bir_e():
    cevaplar['s1_cevap'] = 'İnsan/Hayvan bulunacak mı? - Evet'
    print(cevaplar)
    sb1window.hide()
    sb2window.show()


def close_window_bir_h():
    cevaplar['s1_cevap'] = 'İnsan/Hayvan bulunacak mı? - Hayır'
    print(cevaplar)
    sb1window.hide()
    sb2window.show()


def close_window_iki_e():
    cevaplar['s2_cevap'] = 'Ozona dayanıksız malzeme var mı? - Evet'
    print(cevaplar)
    sb2window.hide()
    sb3window.show()


def close_window_iki_h():
    cevaplar['s2_cevap'] = 'Ozona dayanıksız malzeme var mı? - Hayır'
    print(cevaplar)
    sb2window.hide()
    sb3window.show()


def close_window_uc_e():
    cevaplar['s3_cevap'] = 'Hava akımı var mı? - Evet'
    print(cevaplar)
    sb3window.hide()
    sb4window.show()


def close_window_uc_h():
    cevaplar['s3_cevap'] = 'Hava akımı var mı? - Hayır'
    print(cevaplar)
    sb3window.hide()
    sb4window.show()


def close_window_dort():
    cevaplar['s4_cevap'] = 'Alan' + ' - ' + alan.value + ' m\u00b2'
    print(cevaplar)
    sb4window.hide()
    sb5window.show()


def close_window_bes():
    cevaplar['s5_cevap'] = 'Yükseklik' + ' - ' + yukseklik.value + ' m'
    print(cevaplar)
    sb5window.hide()
    cevap_text.clear()
    cevap_text.append('\n\n')
    str = ', \n'.join(list(cevaplar.values()))
    cevap_text.append(str)
    cevap_text.visible = True
    ileri_buton.visible = True
    app.show()


def st_oto_open():
    led.on()
    print("LED ON")


def st_oto_close():
    led.off()
    print("LED OFF")


def st_oto_back():
    oto_window.hide()
    app.show()


def set_pwm(freq):
    a = oto_son_text.value
    if int(a) >= 100:
        freq = 0
        a = 0
    freq = 20 + int(a)
    oto_son_text.value = freq
    print("PWM: ", freq)
    pwm.changeDutyCycle(freq)


app = App(title="Ana Sayfa", layout="grid")
# app.set_full_screen()
app.when_closed = stop_app

welcome_message = Text(app, text="Sterilizasyon Şeklini şeçiniz.\n", grid=[0, 0])
manuel_buton = PushButton(app, text="Manuel Sterilizasyon", command=manuel_sterilizasyon_view, grid=[0, 1])
oto_buton = PushButton(app, text="Sterizlizasyon", command=sterilizasyon_view, grid=[1, 1])

oto_window = Window(app, title="Sterilizasyon", visible=False)
oto_window.when_closed = stop_app
# oto_window.set_full_screen()

oto_open = PushButton(oto_window, text="Aç", command=st_oto_open)
oto_close = PushButton(oto_window, text="Kapat", command=st_oto_close)
oto_back = PushButton(oto_window, text="PWM +20", command=set_pwm, args=[freq])
oto_son_text = Text(oto_window, text= str(freq))

islem_son_window = Window(app, title="Sterilizasyon İşlemi Tamamlandı", visible=False)
islem_son_window.when_closed = stop_app
# islem_son_window.set_full_screen()
islem_son_text = Text(islem_son_window,
                      text="\n\nSterilizasyon işlemi tamamlandı.\n Havalandırma sistemi durduğunda cihazı kapatabilirsiniz.",
                      visible=False)

islem_window = Window(app, title="Sterilizasyon Yapılıyor", visible=False)
islem_window.when_closed = stop_app
# islem_window.set_full_screen()
islem_text = Text(islem_window, text="İşlem Süresi- Saniye")
islem_text_sure = Text(islem_window, text="", visible=False)
acil_buton = PushButton(islem_window, text="Acil Durum", command=acil_islem)

ileri_window = Window(app, title="Onaylıyor Musunuz?", visible=False)
ileri_window.when_closed = stop_app
# ileri_window.set_full_screen()
ileri_text = Text(ileri_window,
                  text="Seçtiğiniz kriterlere göre sterilizasyon işlemi 1 dakika sürecektir.\nOnaylıyor musunuz?\n")
onay_buton = PushButton(ileri_window, text="Onayla", command=onay_view)
iptal_buton = PushButton(ileri_window, text="İptal", command=iptal_view)
onay_sn_text = Text(ileri_window, text="\nSterilizasyon işlemi 60 sn içinde başlayacaktır.\n", visible=False)
saniye_text = Text(ileri_window, text="", visible=False)

str = '\n\n'

cevap_text = Text(app, text=str, grid=[0, 2], visible=False, align='left')
ileri_buton = PushButton(app, text="İleri", command=ileri_view, grid=[0, 8], visible=False)

sb1window = Window(app, title="Soru 1", visible=False)
sb1window.when_closed = stop_app
# sb1window.set_full_screen()

soru_bir = Text(sb1window, text="Sterilizasyon esnasında ortamda insan/hayvan bulunacak mı?\n")
evet_bir = PushButton(sb1window, text="Evet ", command=close_window_bir_e)
hayir_bir = PushButton(sb1window, text="Hayır", command=close_window_bir_h)
geri_bir = PushButton(sb1window, text="Geri Dön", command=geri_bir)

sb2window = Window(app, title="Soru 2", visible=False)
sb2window.when_closed = stop_app
# sb2window.set_full_screen()

soru_iki = Text(sb2window, text="Sterilizasyon yapılacak yerde ozona/paslanmaya\n dayanıksız malzeme var mı?\n")
evet_iki = PushButton(sb2window, text="Evet ", command=close_window_iki_e)
hayir_iki = PushButton(sb2window, text="Hayır", command=close_window_iki_h)
geri_iki = PushButton(sb2window, text="Geri Dön", command=geri_iki)

sb3window = Window(app, title="Soru 3", visible=False)
sb3window.when_closed = stop_app
# sb3window.set_full_screen()
soru_uc = Text(sb3window, text="Sterilizasyon yapılacak yerde hava akımı var mı?\n")
evet_uc = PushButton(sb3window, text="Evet ", command=close_window_uc_e)
hayir_uc = PushButton(sb3window, text="Hayır", command=close_window_uc_h)
geri_uc = PushButton(sb3window, text="Geri Dön", command=geri_uc)

sb4window = Window(app, title="Soru 4", visible=False)
sb4window.when_closed = stop_app
# sb4window.set_full_screen()
soru_dort = Text(sb4window, text="Sterilizasyon yapılacak yerin alanı - m\u00b2 \n")
alan = TextBox(sb4window, text="50")
alan_kaydet = PushButton(sb4window, text="Kaydet", command=close_window_dort)
geri_dort = PushButton(sb4window, text="Geri Dön", command=geri_dort)

sb5window = Window(app, title="Soru 5", visible=False)
sb5window.when_closed = stop_app
# sb5window.set_full_screen()
soru_bes = Text(sb5window, text="Sterilizasyon yapılacak yerin yüksekliği - m\n")
yukseklik = TextBox(sb5window, text="50")
yukseklik_kaydet = PushButton(sb5window, text="Kaydet ", command=close_window_bes)
geri_bes = PushButton(sb5window, text="Geri Dön", command=geri_bes)

app.display()
