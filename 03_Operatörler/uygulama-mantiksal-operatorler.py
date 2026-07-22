# 1- Yaşı 18' den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.

# veli_izni = True
# yas = 17
# sonuc = (yas >= 18) or (veli_izni == True)

# 2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.

# dersNotu = int(input("Ders Notu Giriniz: "))

# sonuc = (dersNotu >= 50) and (dersNotu <= 100) 
# print(f"Ders Notu {dersNotu} ve öğrenci geçti {sonuc}")

# 3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durumunu kontrol ediniz.

# not1 = int(input("1. Notu Giriniz: "))
# not2 = int(input("2. Notu Giriniz: "))

# ortalama = (not1 +not2)/2

# sonuc = (ortalama >= 70) and (not1 >= 50) and (not2 > 50)

# print(f"Öğrencinin not ortalaması {ortalama}, Teşekkür alabilir {sonuc}.")

# 4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.

# egitim = "önlisans"
# sigara = True

# sonuc = (egitim == "lisans" or egitim == "önlisans") and (not(sigara))

# 5- Uygulamaya giriş kontrolünü "username yada email" ve "parola" için yapalım.

email = "info@sadikturan.com"
username = "sadikturan"
password = "12345"

sonuc = (email == "info@sadikturan.com" or username ==  "sadikturan") and (password == "12345")

print(sonuc)
