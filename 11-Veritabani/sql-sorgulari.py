import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

sql = "INSERT INTO artists(name) VALUES('Mustafa Mutlu')"
cursor.execute(sql)

connection.commit()
# cursor.execute("select * from albums where artistid=8")
# result = cursor.fetchall()

# for album in result:
#     print(album[1]) 

connection.close()
print("Veritabanı Bağlantısı Hazır.")

