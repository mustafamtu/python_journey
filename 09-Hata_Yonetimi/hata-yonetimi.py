while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)

    except Exception as e:
        print("Bilinmeyen bir hata oluştu") 
        print(e)
    else:
        print("Başarıyla Tamamlandı!")
        break
    finally:
        print("Finally bloğu çalıştı!")