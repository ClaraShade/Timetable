import sqlite3
con = sqlite3.connect('harm.db')
c = con.cursor()
# c.execute('''CREATE TABLE users (id int, username str, password str)''')
your_username = input("Wpisz nazwę użytkownika: ")
your_password = input("Wpisz hasło: ")
# if your_username jest w bazie
# your_password = input("Wpisz hasło: ")
# if password =  
# if your_username nie jest w bazie
# print("Nie ma takiego uzytkownika. Wciśnij R aby stworzyć użytkownika")
# your_username = input("Wpisz nazwę użytkownika: ")
# while your username nie jest w bazie
# search
# print("Ta nazwa jest zajęta. Wpisz inną nazwę")
# your_password = input("Wpisz hasło: ")
# our_password_check = input("Wpisz ponownie hasło: ")
c.execute('INSERT INTO users(id, username, password) VALUES (?, ?, ?)', (1, str(your_username), str(your_password)))
con.commit()
con.close()
