# 1- (1-100) arasındaki sayılardan 12' e tam bölünebilen sayı listesini oluşturunuz.

# liste = []
# for sayi in range(1,100):
#     if(sayi % 12 == 0):
#         liste.append(sayi)

# liste = [sayi for sayi in range(1,100) if(sayi % 12 == 0)]
# print(liste)


# 2- Verilen text içerisindeki rakamları içeren bir liste oluşturunuz.
# text = "Hello 12345 World" => [1,2,3,4,5]

text = "Hello 12345 World" 

# for char in text:
#     if(char.isdigit()):
#         print(char)

# text = [char for char in text if(char.isdigit())]
# print(text)

# 3- Sicakliklar listesinde bulunan her hava sıcaklık bilgisine göre 4 derecenin altında buzlanma tehlikesi yazınız.
# sicakliklar = [20,15,0,-5,-2] => [20,15,"Buzlanma Tehlikesi","Buzlanma Tehlikesi","Buzlanma Tehlikesi"]

# sicakliklar = [20,15,0,-5,-2]

# sonuc = [i if i >= 4 else "Buzlanma Tehlikesi" for i in sicakliklar]
# print(sonuc)

# 4- ogrenciler ve notlar listelerindeki notu 50 den fazla olan kişileri ekrana dict verisinde yazdırınız.

# ogrenciler = ["ali","ahmet","canan"]
# notlar = [50,60,80]
# # => "{'ahmet': 60, 'canan': 80}"

# liste = [(ogrenciler[i], notlar[i])for i in range(0, len(ogrenciler))]

# liste_dict = {key:value for (key,value) in liste if value > 50}

# print(liste_dict)

# 5- For döngüsüyle yazılan uygulamayı list comprehension ile yazınız.  

sonuc = []

# for x in range(3):
#     for y in range(3):
#         sonuc.append((x,y))

sonuc = [(x,y) for x in range(3) for y in range(3)]

print(sonuc)