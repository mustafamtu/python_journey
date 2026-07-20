title = "Python ile Programlama Dersleri"

print("S1 - 'title' değişkeni içerisindeki karakter sayısı kaçtır? ")
print(str(len(title)))

print("S2 - 'title' değişkeni içerisindeki Python kelimesini yazdırın")
print(title[0:6])

print("S3 - 'title' değişkeninin ilk 5 ve son 5 karakterini alın.")
print(title[0:5])
print(title[-5:])

print("S4 - 'title' değişkenini tersten yazdırınız.")
print(title[::-1])

print("S5 - # 5- Klavyeden girilen öğrenci bilgisine göre örnek verilen cümleyi yazdırınız.")
# Örnek: Çınar Turan isimli öğrencinin 1.notu 60, 2.notu 60 ve not ortalaması 60 olarak hesaplanmıştır.

print("Ad Giriniz: ")
ad = input()
print("Soyad Giriniz: ")
soyad = input()
print("1. Notu Giriniz: ")
not1 = input()
print("2. Notu Giriniz: ")
not2 = input()

ortalama = (float(not1) + float(not2)) / 2
print(f"{ad} {soyad} isimli öğrencinin 1. notu {not1}, 2. notu {not2} ve not ortalaması {ortalama} olarak hesaplanmıştır.")