import sqlite3
con = sqlite3.connect('harmonogram.db')
c = con.cursor()
# create database if not present
# c.execute('CREATE TABLE users (user_id int, user_name str, password str)')
# c.execute('CREATE TABLE tasks (task_id int, user_id int, time str, task str)')
your_username = input(str("Type your login: "))
u = (your_username,)
c.execute('SELECT user_id FROM users WHERE user_name = ?', u)
found_user = c.fetchall()
if found_user == []:
    print('O, hello, first time?')
# def add(?,?,?):
# input("Wpisz hasło: ")
# id = len()
# id = id+1
# c.execute('INSERT INTO tasks(id, fk, time, task) VALUES (?, ?, ?)', (id, str(time), str(task)))

#
# your_password = input(str(("Wpisz hasło: "))

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
# c.execute('INSERT INTO users(id, username, password) VALUES (?, ?, ?)', (increment, str(your_username), str(your_password)))
# logowanie():
#   x
#   return fk
#
con.commit()
con.close()
