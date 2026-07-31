def selamlama(isim):
    return "Merhaba, "+ isim

# print(selamlama("Mehmet"))

def toplam(sayi1, sayi2):
    return sayi1 + sayi2

# print(toplam(10,20))
# print(toplam(10,30))

def yasHesapla(dogumYili):
    return 2026 - dogumYili

def emekliligeKacKaldi(dogumYili,isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas 
    if(kalanSure > 0):
        return f"{isim}, emekliliğinize {kalanSure} yıl kaldı!"
    else:
        return f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz."

print(emekliligeKacKaldi(1983,"Sadık"))
print(emekliligeKacKaldi(1980,"Ali"))
print(emekliligeKacKaldi(2007,"Mustafa"))




                       
# print(yasHesapla(2007))
