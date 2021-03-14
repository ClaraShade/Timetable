import sqlite3
con = sqlite3.connect('mytimetable.db')
c = con.cursor()
# create database if not present
# c.execute('CREATE TABLE users (userID INTEGER PRIMARY KEY AUTOINCREMENT, username str, password str)')
# c.execute('CREATE TABLE tasks (taskID INTEGER PRIMARY KEY AUTOINCREMENT, userID int, time str, task str, FOREIGN KEY(userID) REFERENCES users(userID))')

your_username = input(str("Hi, what is your name? "))
u = (your_username,)
c.execute('SELECT username FROM users WHERE username = ?', u)
found_user = c.fetchall()
while not found_user:
    print('Hello there, first time? \n'
    'Do you want to create new user?')
    add_user = input(str('Type "y", if you want to create new user. Type "n", if you want to type another name '))
    if add_user == 'y':
        your_password = input(str("Type your password: "),)
        c.execute('INSERT INTO users (username, password) VALUES (?,?)', (your_username, your_password))
        print('Congratulations, ' +your_username+ ', now you can create your timetable!')
        found_user = your_username
    else:
        your_username = input(str("Please, type your name: "))
        u = (your_username,)
        c.execute('SELECT username FROM users WHERE username = ?', u)
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


def get_user_id():
    p = (your_username,)
    c.execute('SELECT userID FROM users WHERE username = ?', p)
    myid = c.fetchall()
    return myid[0]


myID = get_user_id()


def add_task():
    day = str(input("Please type day in format yyyy-mm-dd: "))
    hour = str(input("Please type hour in 24-hour format: "))
    task = str(input("Please type task "))
    mydate = (day + ' ' + hour)
    newid = myID[0]
    c.execute('INSERT INTO tasks (userID, time, task) VALUES (?,?,?)', (newid, mydate, task))


def del_task():
    newid = myID[0]
    task = str(input("Which task do you want to remove? "))
    aram = (task,)
    # c.execute('SELECT t.task FROM tasks t, users u WHERE t.userID = u.userID AND u.username = "Wilczyca" AND t.task =?', newtask)
    c.execute("DELETE FROM tasks WHERE userID = 1 AND task =?", aram)
    # del_task()

del_task()
#c.execute('SELECT t.task FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ?', myID)
#whatifound = c.fetchall()
#print(whatifound)


# del_task()

# add_task()

con.commit()
con.close()