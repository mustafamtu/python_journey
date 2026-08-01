# sayilar = (10,20,30,40,50,60,90,150,240,390,400,420,530,640)

# def toplam(liste):
#     sonuc = 0
#     for i in liste:
#         sonuc += i
#     return sonuc

def toplam(*args):
    print(args)
    print(type(args))
    sonuc = 0
    for i in args:
        sonuc += i
    return args



# sonuc  = toplam(10,20)
# sonuc  = toplam(10,20,30)
sonuc  = toplam(10,20,30,40)
print(sonuc)