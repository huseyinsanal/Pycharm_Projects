
toplam = int()
girisAdedi = int()

while True:
    sayi = int(input("Lütfen bir sayı giriniz: \t"))
    if sayi == 0:
        break
    girisAdedi += 1
    toplam += sayi
    ortalama = toplam / girisAdedi



print("Sayıların Toplam:\t", toplam)
print("Sayıların Ortalaması: \t", ortalama)
print(f"{girisAdedi} Adet Sayı Girdiniz.")

'''

while True:
    kullaniciAdi = input("Kullanıcı Adınız: \t")
    parola = input("Parolanız: \t")

    if kullaniciAdi == "admin":
        if parola == "1234":
            print("Giriş Başarılıdır..! \nHoşgeldiniz", kullaniciAdi)
            break
        elif parola == "x":
            break
        else:
            print("Hatalı Kullanıcı Adı veya Parola")
    elif kullaniciAdi == "x":
        print("Çıkış Yapılmıştır")
        break
    else:
        print("Hatalı Kullanıcı Adı veya Parola")
