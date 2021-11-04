import sqlite3
con = sqlite3.connect('timetable.db')
c = con.cursor()
# create database if not present
# c.execute('CREATE TABLE users (user_id int, user_name str, password str)')
# c.execute('CREATE TABLE tasks (task_id int, user_id int, time str, task str)')
your_username = input(str("Hi, what is your name? "))
u = (your_username,)
c.execute('SELECT user_name FROM users WHERE user_name = ?', u)
found_user = c.fetchall()
while not found_user:
    print('Hello there, first time? \n'
    'Do you want to create new user?')
    add_user = input(str('Type "y", if you want to create new user. Type "n", if you want to type another name '))
    if add_user == 'y':
        your_password = input(str("Type your password: "),)
        c.execute('Select user_id COUNT FROM users')
        count_user = c.fetchall()
        your_id = (len(count_user)) +1
        c.execute('INSERT INTO users VALUES (?,?,?)', (your_id, your_username, your_password))
        print('Congratulations, ' +your_username+ ', now you can create your timetable!')
        found_user = your_username
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
print('Welcome to your timetable, ' + your_username)
x = input()
con.commit()
con.close()
