from termcolor import colored

print("30 * (5+2) = ?")
cevap = input("Cevabı Giriniz: ")

if(cevap == "210"):
    sonuc = colored("Doğru Cevabı Girdiniz",color="green")
else:
    sonuc = colored("Yanlış Cevabı Girdiniz",color="red" )

# sonuc = colored("Merhaba",color="green" )
# sonuc = colored("Merhaba",color="red" )

print(sonuc)