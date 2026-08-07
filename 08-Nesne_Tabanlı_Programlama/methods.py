# Class 
class Product:
    pass
    # method
    # attribute, property
    def __init__(self,name,price,isActive):
        print("Nesne Başarıyla Oluşturuldu!")
        self.name = name
        self.price = price
        self.isActive = isActive

    # Instance Method
    def intro(self):
        return f"Ürün Adı:{self.name} Ürün Fiyat:{self.price}"

    def kdv_price(self):
        return self.price * 1.20



# Instance, Nesne
urun1 = Product("IPhone 17", 84999, True)
urun2 = Product("Samsung J7 Prime", 5999, False)
urun3 = Product("Samsung S24", 12500, True)

urunler = [urun1, urun2, urun3]

for urun in urunler:
    if urun.isActive == True:
        print(urun.intro())
        print(urun.kdv_price ())


