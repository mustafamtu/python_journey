sayilar = [4,6,8,2,56,78,90,4,4]
isimler = ['ahmet','canan','zeynep','gökmen']

sonuc = min(sayilar)
sonuc = min(isimler)
sonuc = max(sayilar)
sonuc = max(isimler)


#ekleme
# sayilar.append(12)
# isimler.append('çınar')

# sayilar.insert(2, 100)
# sayilar.insert(-3,100)
# sayilar.insert(len(sayilar))

# silme

# sayilar.pop()
# sayilar.pop(0)

# isimler.remove('canan')

# sıralama
sayilar.sort()
isimler.sort()
sayilar.reverse()

# sonuc = sayilar
# sonuc = sayilar.count(4)

# armaa
sonuc = sayilar.index(4)


print(sonuc)