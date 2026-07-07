"""
Aşağıdaki müşterinin bilgilerini ve satın aldığı ürün bilgilerini değişkenler içerisinde saklayınız.

Toplam ödenen ücret nedir?

Ödenen miktarın kdv oranı nedir?


Sadık Turan
05321234567
info@sadikturan.com
Kocaeli

Satın Alınan Ürünler

Ürün adı = Kablosuz Mouse
Fiyatı = 550 TL

Ürün adı = Kablosuz Klavye
Fiyatı = 650 TL

Ürün Adı = Dizüstü Bilgisayar
Fiyatı: 55.000 TL


"""

customerName = "Sadık"
customerSurname = "Turan"
customerMail = "info@sadikturan.com"
customerCity = "Kocaeli"
customerPhoneNumber = "05321234567"

productName = "Kablosuz Klavye"
productCost = 650

product2Name = "Kablosuz Mouse"
product2Cost = 550

product3Name = "Dizüstü Bilgisayar"
product3Cost = 55000

sumCost = productCost + product2Cost + product3Cost
print("Toplam Ücret = " + str(sumCost))
print("Ödenen Toplam KDV = " + str(sumCost * 0.18))
 
# Veri Tipi Dönüşümü Şart