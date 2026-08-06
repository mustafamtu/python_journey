# Not Uygulaması

# 1- Menu
# 1- Not Gir
# 2- Ortalamaları Göster (90-100 -> AA, 85-89 -> BA)
# 3- Notları Kayıt Et
# 4- Çıkış

def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if ortalama >= 90 and ortalama <= 100:
        harf = "AA"
    elif ortalama >= 80 and ortalama <= 89:
        harf = "BA"
    elif ortalama >= 75 and ortalama <= 79:
        harf = "BB"
    elif ortalama >= 70 and ortalama <= 74:
        harf = "CB"
    elif ortalama >= 65 and ortalama <= 69:
        harf = "CC"
    elif ortalama >= 60 and ortalama <= 64:
        harf = "DC"
    elif ortalama >= 50 and ortalama <= 59:
        harf = "DD"
    elif ortalama >= 40 and ortalama <= 49:
        harf = "FD"
    elif ortalama >= 0 and ortalama <= 39:
        harf = "FF"

    return f"{ogrenciAdi} : {harf} ( {ortalama} )\n"
    
def not_gir():
    ad = input("Öğrenci Adı Giriniz: ")
    soyad = input("Öğrenci Soyadı Giriniz: ")
    not1 = input("1. Notu Giriniz: ")
    not2 = input("2. Notu Giriniz: ")
    not3 = input("3. Notu Giriniz: ")

    
    with open("sinav_notlari.txt","a", encoding = "utf-8") as file:
        file.write(ad+ " "+ soyad+ ":"+ not1+","+ not2+ ","+ not3 + "\n")

def not_kaydet():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste = []

        for satir in file:
            liste.append(not_hesapla(satir))
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            file2.writelines(liste)




def not_oku():
    with open("sinav_notlari.txt","r",encoding = "utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
    

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
        not_kaydet()
    elif(secim == '4'):
        print("Çıkış Yaptınız...")
        break
