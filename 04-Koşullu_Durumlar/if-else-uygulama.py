# Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan 
# uygulamayı yapınız.

# benzin: 39.35
# dizel: 41.71
# lpg:   20.28


# fuelType = input("Yakıt Tipi Giriniz: ")
# distance = int(input("Mesafe Giriniz: "))

# if(fuelType == "benzin"):
#     fuelPrice = 39.35
# elif(fuelType == "dizel"):
#     fuelPrice = 41.71
# elif(fuelType == "lpg"):
#     fuelPrice = 20.28

# cost = fuelPrice * distance
# print(cost)


# Bir öğrencinin 2 yazılı notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına
# karşılık gelen değerlendirmeyi yazdırınız.    

not1 = int(input("1. Notu Giriniz: "))
not2 = int(input("2. Notu Giriniz: "))

ortalama = (not1 + not2)/2

if(ortalama >= 0) and (ortalama <= 24):
    degerlendirme = 0
elif(ortalama >= 25) and (ortalama <= 44):
    degerlendirme = 1
elif(ortalama >= 45) and (ortalama <= 54):
    degerlendirme = 2
elif(ortalama >= 55) and (ortalama <= 69):
    degerlendirme = 3
elif(ortalama >= 70) and (ortalama <= 84): 
    degerlendirme = 4
elif(ortalama >= 85) and (ortalama <= 100):
    degerlendirme = 5
else:
    print("Geçersiz Not Tekrar Deneyiniz!")

print(f"Öğrencinin 1. Notu {not1}, 2. Notu {not2}, ortalaması {ortalama} ve değerlendirme notu {degerlendirme}")




# 0 -24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3 
# 70-84 => 4
# 85-100=> 5

