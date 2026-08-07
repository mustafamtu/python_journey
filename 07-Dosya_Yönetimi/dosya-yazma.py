# "w": (Write) yazma modu.
#       ** Dosyayı konumda oluşturur.
#       ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur.

with open("dosya.txt","w",encoding = "utf-8") as file:
    file.write("Sadık Turan\n")
    file.write("Mustafa Mutlu\n")

    
with open("dosya.txt","r",encoding = "utf-8") as file:
    for i in file:
        print(i, end = "")


