# local scope
# global scope 

# x = "global scope"

# def my_func():
#     x = "local scope"
#     print(x)

# my_func()
# print(x)

# name = "Çınar"

# def change_name(new_name):
#     global name
#     name = new_name
#     print(name)

# change_name("Mustafa")
# print(name)

# name = "global string"  # 3.Öncelik
# def greeting():
#     # name = "Çınar" 2. Öncelik

#     def hello():
#         # name = "Ada"  1. Öncelik
#         print("Merhaba " ,name)

#     hello()
# greeting()

x = 50

def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"Changed x to {x}")

test()
print(x)