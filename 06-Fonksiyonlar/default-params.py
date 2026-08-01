def selamlama(isim = "User",mesaj = "Hoşgeldin"):
    return f"{mesaj} {isim}"

sonuc = selamlama("Mustafa","Merhaba")
sonuc = selamlama("Ali")
sonuc = selamlama()

def usAlma(taban,us = 2):
    return taban ** us

sonuc = usAlma(2,3)
sonuc = usAlma(8)

def toplam(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a * b

def islem(a,b,mdef):
    return mdef(a,b)

sonuc = islem(10,20,carpma)

print(sonuc)