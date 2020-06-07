from guizero import Box, App, Text, TextBox, PushButton, Slider, Combo, CheckBox, ButtonGroup, info, Window

cevaplar = {"s1_cevap": "",
            "s2_cevap": "",
            "s3_cevap": "",
            "s4_cevap": "",
            "s5_cevap": ""}


def geri_bir():
    print(cevaplar)
    sb1window.hide()
    app.show()


def geri_iki():
    print(cevaplar)
    sb2window.hide()
    sb1window.show()


def geri_uc():
    print(cevaplar)
    sb3window.hide()
    sb2window.show()


def geri_dort():
    print(cevaplar)
    sb4window.hide()
    sb3window.show()


def geri_bes():
    print(cevaplar)
    sb5window.hide()
    sb4window.show()


def manuel_sterilizasyon_view():
    print(cevaplar)
    sb1window.show()
    app.hide()


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
    app.show()


app = App(title="Ana Sayfa", layout="grid")

welcome_message = Text(app, text="Sterilizasyon Şeklini şeçiniz.\n", grid=[0, 0])
manuel_buton = PushButton(app, text="Manuel Sterilizasyon", command=manuel_sterilizasyon_view, grid=[0, 1])
oto_buton = PushButton(app, text="Otomatik Sterizlizasyon", command=manuel_sterilizasyon_view, grid=[1, 1],
                       enabled=False)
str = '\n\n'
cevap_text = Text(app, text=str, grid=[0, 2], visible=False, align='left')

sb1window = Window(app, title="Soru 1", visible=False)

soru_bir = Text(sb1window, text="Sterilizasyon esnasında ortamda insan/hayvan bulunacak mı?\n")
evet_bir = PushButton(sb1window, text="Evet ", command=close_window_bir_e)
hayir_bir = PushButton(sb1window, text="Hayır", command=close_window_bir_h)
geri_bir = PushButton(sb1window, text="Geri Dön", command=geri_bir)

sb2window = Window(app, title="Soru 2", visible=False)

soru_iki = Text(sb2window, text="Sterilizasyon yapılacak yerde ozona/paslanmaya\n dayanıksız malzeme var mı?\n")
evet_iki = PushButton(sb2window, text="Evet ", command=close_window_iki_e)
hayir_iki = PushButton(sb2window, text="Hayır", command=close_window_iki_h)
geri_iki = PushButton(sb2window, text="Geri Dön", command=geri_iki)

sb3window = Window(app, title="Soru 3", visible=False)

soru_uc = Text(sb3window, text="Sterilizasyon yapılacak yerde hava akımı var mı?\n")
evet_uc = PushButton(sb3window, text="Evet ", command=close_window_uc_e)
hayir_uc = PushButton(sb3window, text="Hayır", command=close_window_uc_h)
geri_uc = PushButton(sb3window, text="Geri Dön", command=geri_uc)

sb4window = Window(app, title="Soru 4", visible=False)
soru_dort = Text(sb4window, text="Sterilizasyon yapılacak yerin alanı - m\u00b2 \n")
alan = TextBox(sb4window, text="50")
alan_kaydet = PushButton(sb4window, text="Kaydet", command=close_window_dort)
geri_dort = PushButton(sb4window, text="Geri Dön", command=geri_dort)

sb5window = Window(app, title="Soru 5", visible=False)
soru_bes = Text(sb5window, text="Sterilizasyon yapılacak yerin yüksekliği - m\n")
yukseklik = TextBox(sb5window, text="50")
yukseklik_kaydet = PushButton(sb5window, text="Kaydet ", command=close_window_bes)
geri_bes = PushButton(sb5window, text="Geri Dön", command=geri_bes)

app.display()
