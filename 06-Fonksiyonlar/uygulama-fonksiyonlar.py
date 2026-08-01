# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

# def ekranaYazdirma(text,adet):
#     return text * adet

# print(ekranaYazdirma("Beş Kere Beş ",5))

# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.


# def hesaplayici(kisa,uzun):
#     alan = kisa * uzun
#     cevre = 2 * (kisa + uzun)

#     return alan,cevre

# sonuc = hesaplayici(5,20)

# print(sonuc)


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

# def yaziTura():
#     import random
#     madeniPara = random.randint(0,1)
#     if(madeniPara == 0):
#         madeniPara = "Yazı"
#     else:
#         madeniPara = "Tura"
#     return madeniPara

# print(yaziTura())


# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

# def asalSayilariBul(sayi1,sayi2):
#     for sayi in range(sayi1,sayi2+1):
#         if sayi > 1:
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     break
#                 else:
#                     print(sayi)

# asalSayilariBul(20, 30)

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tamBolenBul(sayi):
    tamBolenler = []

    for i in range(2,sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)

    return tamBolenler

print(tamBolenBul(20))