my_list = [1,2,3]
my_tuple = (1,2,3)

print(type(my_list))
print(type(my_tuple))

sonuc = my_list[0] = 2
# sonuc = my_tuple[0] = 2

my_list.append(3)

my_tuple2 = tuple([2,3,4])

sonuc = my_tuple
sonuc = my_list


print(sonuc)