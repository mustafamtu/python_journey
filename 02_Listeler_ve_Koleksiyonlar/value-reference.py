# value types
# x = 10
# y = 20
# x = y
# y = 30
# print(x,y)

# reference 
a = ["elma","armut"]
b = ["elma","armut"]

a = b #adres kopyaladınız

a[0] = "üzüm"

print(a, b)

# liste kopyalama

listeA = [10,20]
# listeB = listeA.copy()
listeB = list(listeA)     

listeB[0] = 30

print(listeA,listeB)
