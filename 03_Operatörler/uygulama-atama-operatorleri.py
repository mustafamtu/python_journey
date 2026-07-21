# a, b, c = 4, 8, (12, 2)

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir?

# sayi1 = int(input("Birinci Sayıyı Giriniz: "))
# sayi2 = int(input("İkinci Sayıyı Giriniz: "))

# carpim = (sayi1 * sayi2) 
# toplam = (a + b + (c[0] + c[1]))
# sonuc = carpim - toplam

# 2- c' nin b' ye kalansız bölümünü hesaplayınız.

# sonuc = (c[0] + c[1]) // b

# 3- (a,b,c) toplamının mod 7' si nedir?

# sonuc = (a + b + (c[0] + c[1])) % 7

# 4- b' nin a. kuvvetini hesaplayınız.

# sonuc = b ** a

# 5- a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?

# a, *b, c = (2,4,6,8,13)

# print(c ** 3)

# 6- a, b, ic = (2,4,6,8,13) işlemine göre c' nin değerleri toplamı nedir?,

a, b, *c = (2,4,6,8,13)

csum = c[0] + c[1] + c[2]
print(csum)

