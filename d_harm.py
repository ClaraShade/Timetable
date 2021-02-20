import sqlite3
con = sqlite3.connect('harmonogram.db')
c = con.cursor()
# create database if not present
# c.execute('CREATE TABLE users (user_id int, user_name str, password str)')
# c.execute('CREATE TABLE tasks (task_id int, user_id int, time str, task str)')
your_username = input(str("Hi, what is your name? "))
u = (your_username,)
c.execute('SELECT user_name FROM users WHERE user_name = ?', u)
found_user = c.fetchall()
while found_user == []:
    print('Hello there, first time? \n'
    'Do you want to create new user?')
    add_user = input(str('Type "y", if you want to create new user. Type "n", if you want to type another name '))
    if add_user == 'y':
        your_username = input(str("Type your name: "),)
        your_password = input(str("Type your password: "),)
        c.execute('Select user_id COUNT FROM users')
        count_user = c.fetchall()
        your_id = (len(count_user)) +1
        c.execute('INSERT INTO users VALUES (?,?,?)', (your_id, your_username, your_password))
        print('Congratulations, ' +your_username+ ', now you can create your harmonogram!')
        raw_input()
    else:
        your_username = input(str("Type your name: "))
        u = (your_username,)
        c.execute('SELECT user_name FROM users WHERE user_name = ?', u)
        found_user = c.fetchall()
print('Hello, '+ your_username)
your_password = input(str("Type your password: "))
p = (your_password,)
c.execute('SELECT password FROM users WHERE password = ?', p)
found_password = c.fetchall()
listed_p = [p]
while found_password != listed_p:
    print('Wrong password, type again')
    your_password = input(str("Type your password: "))
    p = (your_password,)
    c.execute('SELECT password FROM users WHERE password = ?', p)
    found_password = c.fetchall()
    listed_p = [p]
print('Welcome to your harmonogram, ' + your_username)
raw_input()
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

con.commit()
con.close()
