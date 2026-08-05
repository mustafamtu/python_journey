# Not Uygulaması

# 1- Menu
# 1- Not Gir
# 2- Ortalamaları Göster (90-100 -> AA, 85-89 -> BA)
# 3- Notları Kayıt Et
# 4- Çıkış

def not_gir():
    ad = input("Öğrenci Adı Giriniz: ")
    soyad = input("Öğrenci Soyadı Giriniz: ")
    not1 = input("1. Notu Giriniz: ")
    not2 = input("2. Notu Giriniz: ")
    not3 = input("3. Notu Giriniz: ")

    
    with open("sinav_notlari.txt","a", encoding = "utf-8") as file:
        file.write(ad+ " "+ soyad+ ":"+ not1+","+ not2+ ","+ not3)

def not_oku():
    with open("sinav_notlari.txt","r",encoding = "utf-8") as file:
        for satir in file:
            print(satir)
    

while True:
    print("*** NOT UYGULAMASI ***")
    print("1- Not Gir")
    print("2- Notları Oku")
    print("3- Notları Kayıt Et")
    print("4- Çıkış Yap")

    secim = input("Seçim Yapınız: ")
 
    if(secim == '1'):
        print("+--+ NOT GİRME MENÜSÜ +--+")
        not_gir()
        print("\nNot Girişiniz Başarıyla Tamamlandı Menüye Yönlendiriliyorsunuz...")
    elif(secim == '2'):
        print("+--+ NOT OKUMA MENÜSÜ +--+")
        not_oku()
    elif(secim == '3'):
        print("+--+ NOT KAYDETME MENÜSÜ +--+")
        pass
    elif(secim == '4'):
        print("Çıkış Yaptınız...")
        break
