"""
module1 (db)        : urunler
module2 (methods)   : urunEkle(), urunGuncelle(), urunleriGetir()
module3 (app)       :

    yeni ürün ekleme    => urunEkle("iphone 15",60000)
    ürün güncelle       => urunGuncelle(1,"iphone 15", 80000)
    ürünleri listele    => urunleriGetir()

"""

from methods import * 

sonuc = urunleriGetir()

print(sonuc)

urunEkle("Iphone 20", 90000)
urunEkle("Samsung s20", 90000)

# for i in urunleriGetir():
#     print(i["urunAdi"])

urunGuncelle(1,"Samsung J7 Prime",9000)

for i in urunleriGetir():
    print(i["urunAdi"])