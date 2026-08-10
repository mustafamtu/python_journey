# print(10 / 0)

# x = 0

# if x <= 0:
#     raise Exception("x Değeri 0'a eşit veya 0'dan küçük olamaz")

def renklendir(metin,renk):
    renkler = ("blue","red","yellow","white","black","orange","green")
    if type(metin) is not str:
        raise TypeError("Metni string formatında giriniz!")
    if type(renk) is not str:
        raise TypeError("Rengi string formatında giriniz!")
    if renk not in renkler:
        raise ValueError("Geçersiz Renk!")
    print(f"({renk}) {metin} olarak yazıldı")
        
try:
    renklendir("selam","red")
    renklendir("merhaba","yellow")
    renklendir("hola","purple")

except (TypeError, ValueError) as e:
    print(e)