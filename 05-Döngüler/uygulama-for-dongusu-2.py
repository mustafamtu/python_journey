#

urunler = [
{"urunAdi":"Hp Victus", "fiyat": 32999},
{"urunAdi":"Lenovo ThinkPad", "fiyat": 25499},
{"urunAdi":"Apple Macbook", "fiyat": 49999},
{"urunAdi":"Huawei Matebook", "fiyat": 26999},
{"urunAdi":"Casper Nirvana", "fiyat": 20000}
]


# 1- Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
"Hp Victus marka ürünün fiyatı 32999 Türk Lirası."

#kutu_adi['etiket_adi']

# for urun in urunler:
#     print(f"{urun['urunAdi']} marka ürünün fiyatı {urun['fiyat']} TRY")


# 2- Ürünlerin fiyatları toplamı nedir?

# toplam = 0
# for urun in urunler:
#     toplam += urun['fiyat']

# print(toplam)

# 3- 25000 ile 40000 arasındaki ürünleri listeleyiniz.

# for urun in urunler:
#     if(urun['fiyat'] >= 25000) and (urun['fiyat'] <= 40000):
#         print(urun)

# 4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.

# search = input("Arama Yapmak İçin Yazınız: ")

# for urun in urunler:
#     if(search in urun['urunAdi']):
#         print(urun)
