# 1- Faktoriyel fonksiyonu oluşturunuz ve fonksiyona gelen deger icin hata mesajlari verin.

# def faktoriyel(sayi):
#     sayi = int(sayi)
#     if(sayi < 0):
#         raise ValueError("Sayı 0'dan küçük olamaz.")
#     sonuc = 1
#     for i in range(1,sayi + 1):
#         sonuc *= i
#     print(sonuc)

# faktoriyel(30)

# 2- Girilen parola içinde türkçe karakter hatası veriniz.

parola = input("Parola Giriniz: ")

turkce = ["ü","ğ","ş","ö","ç"]
for i in parola:
    for x in turkce:
        if i == x:
            raise TypeError("Parolanızda türkçe karakter kullanamazsınız.")
   



# raise Exception("Parolanızda türkçe karakter kullanamazsınız!")


