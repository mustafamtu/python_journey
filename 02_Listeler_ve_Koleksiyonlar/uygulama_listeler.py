# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste olusturunuz.

markalar = ["Toyota","Bmw","Renault","Mercedes"]

# 2- Liste kaç elemanlıdır?

sonuc = len(markalar) # 4 elemanlı 

# 3- Listenin ilk ve son elemanı nedir?

sonuc = markalar[0]
sonuc = markalar[-1]

# 4- "Renault" markasını "Togg" ile güncelleyiniz.

markalar[2] = "Togg"
sonuc = markalar

# 5- "Togg" listenin bir elemanı mıdır?

"Togg" in markalar

# 6- Listenin ilk 2 elemanını alınız.

sonuc = markalar[0:2]

# 7- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.

markalar + ["Ford","Citroen"]

# 8- Listenin son elemanını siliniz.

del markalar[-1]

# 9- Aşağıdaki verileri liste içerisinde saklayınız.

# öğrenci1: Yiğit Bilgi 2010 [70,80,90]
# öğrenci2: Ada Bilgi 2011 [70,70,80]
# öğrenci3: Çınar Turan 2017 [60,60,90]

ogrenci1 = ["Yiğit", "Bilgi",2010,[70,80,90]]
ogrenci2 = ["Ada", "Bilgi",2011,[70,70,80]]
ogrenci3 = ["Çınar", "Turan",2017,[60,60,90]]

ogrenciler = [ogrenci1,ogrenci2,ogrenci3]


# 10- Öğrencilerin yaşlarını hesaplayınız.

yasYigit = 2026 - ogrenci1[2] 
yasAda = 2026 - ogrenci2[2]
yasCinar = 2026 - ogrenci3[2]

print(yasYigit,yasAda,yasCinar)
# 11- Ogrencilerin not ortalamalarını hesaplayınız.     

notYigit = (ogrenci1[3][0] + ogrenci1[3][1] + ogrenci1[3][2]) / 3
notAda = (ogrenci2[3][0] + ogrenci2[3][1] + ogrenci2[3][2]) / 3
notCinar = (ogrenci3[3][0] + ogrenci3[3][1] + ogrenci3[3][2]) / 3

print(notYigit,notAda,notCinar)

print(sonuc)