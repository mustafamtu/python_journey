# for item in liste:
#     if(kosul):
#         expression

# [expression for item in liste if kosul]

sayilar = [3,5,7,6,56,34]
sonuc = []

for sayi in sayilar:
    if (sayi % 2 == 0):
        sonuc.append(sayi)

print(sonuc)

sonuc = [sayi for sayi in sayilar if(sayi % 2 == 0)]


print(sonuc)