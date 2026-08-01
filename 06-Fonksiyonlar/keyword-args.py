def full_name(name: str,surname: str) -> str:
    return f"Your name is {name} {surname}"

sonuc = full_name("Mustafa","Mutlu")
sonuc = full_name(surname = "Mutlu",name = "Mustafa")
sonuc = full_name(surname = 40,name = "Mustafa")
sonuc = full_name(surname = "Mutlu",name = "Mustafa")


print(sonuc)