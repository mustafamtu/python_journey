liste = ["1","3","5","20b","abc","10a","60"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.   

# for eleman in liste:
#     try:
#         sonuc = int(eleman)
#         print(sonuc)
#     except:
#         print(f"{eleman} Elemanı sayısal değer değildir.")


# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata
# mesajı yazın.

# while True:
#     sayi = input("Değer Giriniz: ")
#     if(sayi == 'q'):
#         break
#     try:
#         sonuc = int(sayi)
#         print(f"Girilen sayı: {sonuc}")
#         break
#     except ValueError:
#         print("Geçersiz sayı!")
#         continue
    
    
# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict, key) fonksiyonu hazırlayınız.

urun = {"urunAdi":"samsung s10"}

# d["fiyat"] => KeyError
# get(urun, "fiyat") => None
# get(urun, "urunAdi") => samsung S20

def get(list,key):
    try:
        return list[key]
    except KeyError:
        return None

sonuc = get(urun, "fiyat")
# sonuc = get(urun, "urunAdi")

print(sonuc)

    