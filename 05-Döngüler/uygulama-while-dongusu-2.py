# Klavyeden girilen n sayıdaki öğrenci bilgisini liste içerisinde saklayınız.
# ** dictionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun.
# ** öğrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.


devammi = ""
ogrenciler = []

while (devammi != "h"):
    ogrenciNo = input("Öğrenci No Giriniz: ")
    ogrenciAd = input("Öğrenci Adı Giriniz: ")
    ogrenciSoyad = input("Ögrenci Soyadı Giriniz: ")

    ogrenciler.append({
        "ogrenciNo": ogrenciNo,
        "ogrenciAd": ogrenciAd,
        "ogrenciSoyad":ogrenciSoyad
    })
    devammi = input("Devam mı? (e/h): ")

for ogrenci in ogrenciler:
    print(f"{ogrenci["ogrenciNo"]} numaralı öğrencinin adı {ogrenci["ogrenciAd"]} {ogrenci["ogrenciSoyad"]}")


