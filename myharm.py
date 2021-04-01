import sqlite3

import datetime

from datetime import datetime


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
    isdate = datetime.isoformat(mydate)
    c.execute('INSERT INTO tasks (userID, time, task) VALUES (?,?,?)', (myID[0], isdate, task))


def del_task():
    toremove = str(input("Which task do you want to remove? "))
    c.execute("DELETE FROM tasks WHERE userID = ? AND task =?", (myID[0], toremove))

# del_task()

def show_tasks():
    toshow = str(input("Type 'today' show today's task(s). \n"
    "Type 'week' to show this week's task(s) \n"
    "Type 'month' to show tasks(s) at given month \n"
    "Type 'date' to show tasks(s) at given date \n"))
    if toshow == 'today':
        daytoday = str(datetime.date.today())
        c.execute('SELECT t.task FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND t.time like ?',
                  (myID[0], '%' + daytoday + '%'))
        whatifound = c.fetchall()
    elif toshow == 'week':
        daytoday = (datetime.date.today())
        print(datetime.date.isoweekday(daytoday))
    elif toshow == 'month':
        daytoday = datetime.strptime(now)
        strptime
        c.execute('SELECT t.task FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND t.time like ?',
                  (myID[0], '%' + someday + '%'))
        whatifound = c.fetchall()
        print(daytoday)
    elif toshow == 'date':
        isomeday = 0
        while isomeday == 0:
            try:
                someday = str(input('Type date: '))
                isomeday = datetime.fromisoformat(someday)
                startday = someday+' 00:00'
                endday = someday+' 23:59'
            except:
                print('Ivalid date. Type again.')
        print(startday)
        print(endday)
        c.execute('SELECT t.task FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND t.time > ? AND t.time < ?',
                  (myID[0], startday, endday))
        whatifound = c.fetchall()
    print(whatifound)

#add_task()

show_tasks()

#def find_task():
#mytask = str(input('Type task name to find: '))
#c.execute('SELECT * FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND t.task = ?', (myID[0], mytask))
#whatifound = c.fetchall()
#print(whatifound)

# del_task()




con.commit()
con.close()