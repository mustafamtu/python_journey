#lambda argument: expression

def kareAl(a):
    return a ** 2

sonuc = kareAl(4)

sonuc = (lambda a: a ** 2)(3)

toplama = lambda a,b,c:a + b + c
sonuc = toplama(3,4,5)

def myFunc(n):
    return lambda a: a * n

carpma2 = myFunc(2)

sonuc = myFunc(2)(3)

print(sonuc)