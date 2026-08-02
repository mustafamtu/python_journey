# Bankamatik Uygulaması

# Hesap bilgileri tutulacak. (dict)
# menu, paraCekme, bakiyeSorgula, paraYatirma fonksiyonları tanımlanacak.
# çekilmek istenen tutar hesapta yoksa ek hesabın kullanılmak istendiği sorulacak.

hesaplar = [
{
    "ad":"Sadık Turan",
    "hesapNo": "001",
    "bakiye": 20000,
    "username":"sadikturan",
    "password":"1234"
},
{
    "ad":"Mustafa Mutlu",
    "hesapNo": "002",
    "bakiye": 500,
    "username":"asd",
    "password":"2341"
}
]


def paraCekme(hesap,miktar):
    if hesap["bakiye"] >= miktar:
       hesap["bakiye"] = hesap["bakiye"] - miktar 
       print(f"Yeni Bakiyeniz: {hesap["bakiye"]}")
        
    else:
        print("Yetersiz Bakiye.")
        return None
    
def paraYatirma(hesap,yatırılan):
    hesap["bakiye"] = hesap["bakiye"] + yatırılan
    print(f"Yeni Bakiyeniz: {hesap["bakiye"]}")

def bakiyeSorgula(hesap):
    print(f"Bakiyeniz: {hesap["bakiye"]}")

def login(**kwargs):
    girilen_user = input("Kullanıcı Adı Giriniz: ")
    girilen_password = input("Şifre Giriniz: ")
    
    for i in hesaplar:
        if girilen_user == i["username"]:
           
            if girilen_password ==   i["password"]:
                print(f"\nHoşgeldin {i["ad"]}!")
                return i
            else:
                print("Yanlış Şifre Tekrar Deneyiniz!")
                return None
  
    print("Böyle Bir Kullanıcı Bulunamadı.")
    return None
        

aktif_hesap = login()


def menu():
    print("1- Para Çek")
    print("2- Para Yatır")
    print("3- Bakiye Sorgula")
    print("4- Çık")

    
if aktif_hesap != None:
    
    while True:
        menu()  
        secim = input("\nSeçim Yapınız: ")
        
        if secim == "1":
            istenenPara = int(input("Çekmek İstediğiniz Miktarı Giriniz: "))
            paraCekme(aktif_hesap, istenenPara)
            
        elif secim == "2":
            verilenPara = int(input("Yatırmak İstediğiniz Miktarı Giriniz: "))
            paraYatirma(aktif_hesap, verilenPara)

        elif secim == "3":
            bakiyeSorgula(aktif_hesap)

        elif secim == "4":
            print("Bankamatik sisteminden çıkış yapıldı. İyi günler dileriz!")
            break  

        else:
            print("Geçersiz seçim yaptınız, tekrar deneyiniz.")