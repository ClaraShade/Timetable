import sqlite3

import datetime

from datetime import datetime
from datetime import date

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
    hour = str(input("Please type time in 24-hour format: "))
    task = str(input("Please type task "))
    mydate = (day + ' ' + hour)
    c.execute('INSERT INTO tasks (userID, time, task) VALUES (?,?,?)', (myID[0], mydate, task))


def del_task():
    toremove = str(input("Which task do you want to remove? "))
    c.execute("DELETE FROM tasks WHERE userID = ? AND task =?", (myID[0], toremove))


def show_tasks():
    # global whatifound if needed in future
    toshow = str(input("Type 'today' show today's task(s). \n"
    "Type 'week' to show this week's task(s) \n"
    "Type 'month' to show tasks(s) at given month \n"
    "Type 'date' to show tasks(s) at given date \n"))
    if toshow == 'today':
        daytoday = str(date.today())
        c.execute('SELECT t.time, t.task FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND t.time like ?',
                  (myID[0], daytoday + '%'))
        whatifound = c.fetchall()
        if whatifound:
            print(whatifound)
        else:
            print("You have no tasks today")

    elif toshow == 'week':
        daytoday = date.today()
        weekofyear = daytoday.isocalendar()[1]
        #weektoday = date.isoweekday(daytoday)
        print(weekofyear)
        c.execute(
            'SELECT t.time, t.task FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND datetime.fromisoformat(t.time) = ?',
            (myID[0], 15))
        whatifound = c.fetchall()
        if whatifound:
            print(whatifound[0][0] + ': ' +whatifound[0][1])
        else:
            print("You have no tasks this week")
    elif toshow == 'month':
        somemonth = int(input('Type month 1-12: '))
        daytoday = date.today()
        yeartoday = daytoday.year
        while somemonth > 12:
            somemonth = int(input('Type month 1-12: '))
        if somemonth > 9:
            month = str(yeartoday) + '-' + str(somemonth) + '-'
        else:
            month = str(yeartoday) + '-0' + str(somemonth) + '-'
        c.execute(
            'SELECT t.time, t.task FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND t.time like ?',
            (myID[0], month + '%' + '%'))
        whatifound = c.fetchall()
        if whatifound:
            print(whatifound)
        else:
            print("You have no tasks this month")
    elif toshow == 'date':
        isomeday = 0
        while isomeday == 0:
            try:
                someday = str(input('Type date: '))
                isomeday = datetime.fromisoformat(someday)
            except:
                print('Ivalid date. Type again.')
        c.execute(
            'SELECT t.time, t.task FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND t.time like ?',
            (myID[0], someday + '%'))
        whatifound = c.fetchall()
        if whatifound:
            print(whatifound[0][0] + ': ' +whatifound[0][1])
        else:
            print("You have no tasks at this date")

def switch_tasks():
    day1 = str(input("Please type the date of the first task in format yyyy-mm-dd: "))
    hour1 = str(input("Please type the time of the first task in 24-hour format: "))
    task1 = str(input("Please type the name of the first task "))
    time1 = day1 + ' ' + hour1
    firsttask = (myID[0], time1, task1)
    print(firsttask)
    day2 = str(input("Please type the date of the second task in format yyyy-mm-dd: "))
    hour2 = str(input("Please type the time of the second task in 24-hour format: "))
    task2 = str(input("Please type the name of the second task "))
    time2 = day2 + ' ' + hour2
    secondtask = (myID[0], time2, task2)
    print(secondtask)
    c.execute("UPDATE tasks SET time = ? WHERE userID = ? AND time =? AND task =?", (time2, myID[0], time1, task1))
    c.execute("UPDATE tasks SET time = ? WHERE userID = ? AND time =? AND task =?", (time1, myID[0], time2, task2))


#add_task()
#del_task()
#show_tasks()
#switch_tasks()

#def find_task():
#mytask = str(input('Type task name to find: '))
#c.execute('SELECT * FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND t.task = ?', (myID[0], mytask))
#whatifound = c.fetchall()
#print(whatifound)

# del_task()




con.commit()
con.close()