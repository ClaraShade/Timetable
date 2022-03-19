"""Personal timetable for multiple users created with sqlite3.
Enables various operations on tasks
Written: April 2021
Refactored: March 2022"""

import sqlite3

import datetime

from datetime import datetime
from datetime import date
import d_harm_log as log_me

con = sqlite3.connect('timetable.db')
c = con.cursor()


def get_user_id():
    """Gets the user id by calling the separate d_harm_log module"""
    my_id = log_me.main()
    return my_id


def find_task(my_id):
    """Finds the task based on the user's imput"""

    mytask = str(input('Type task name to find: '))
    c.execute('SELECT t.time, t.task FROM tasks t, users u WHERE'
              't.userID = u.userID AND u.userID = ? AND t.task = ?',
              (my_id[0], mytask))
    whatifound = c.fetchall()
    print(whatifound)


def add_task(my_id):
    """Adds the task based on the user's imput. The user needs to specify
    date and the name of the task"""
    day = str(input("Please type day in format yyyy-mm-dd: "))
    hour = str(input("Please type time in 24-hour format: "))
    task = str(input("Please type task "))
    mydate = (day + ' ' + hour)
    c.execute('INSERT INTO tasks (userID, time, task) VALUES (?,?,?)',
              (my_id[0], mydate, task))


def del_task(my_id):
    """Removes the task based on the user's imput"""
    toremove = str(input("Which task do you want to remove? "))
    c.execute("DELETE FROM tasks WHERE userID = ? AND task =?",
              (my_id[0], toremove))


def show_tasks(my_id):
    """Shows the taks from today or from a given date/week/month based on the
    user's imput"""
    toshow = str(input("Type 'today' show today's task(s);\nType 'week' to show"
                       " this week's task(s);\n"
                       "Type 'month' to show tasks(s) at given month\n"
                       "Type 'date' to show tasks(s) at given date: "))
    if toshow == 'today':
        daytoday = str(date.today())
        c.execute(
            'SELECT t.time, t.task FROM tasks t, users u'
            'WHERE t.userID = u.userID AND u.userID = ? AND t.time like ?',
            (my_id[0], daytoday + '%'))
        whatifound = c.fetchall()
        if whatifound:
            print(whatifound)
        else:
            print("You have no tasks today")
    elif toshow == 'week':
        daytoday = date.today()
        weekofyear = daytoday.isocalendar()[1]
        # weektoday = date.isoweekday(daytoday)
        print(weekofyear)
        c.execute(
            'SELECT t.time, t.task FROM tasks t, users u'
            'WHERE t.userID = u.userID AND u.userID = ?'
            'AND datetime.fromisoformat(t.time) = ?', (my_id[0], 15))
        whatifound = c.fetchall()
        if whatifound:
            print(whatifound[0][0] + ': ' + whatifound[0][1])
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
            'SELECT t.time, t.task FROM tasks t, users u'
            'WHERE t.userID = u.userID AND u.userID = ?'
            'AND t.time like ?',
            (my_id[0], month + '%' + '%'))
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
            except TypeError:
                print('Ivalid date. Type again.')
        c.execute(
            'SELECT t.time, t.task FROM tasks t, users u'
            'WHERE t.userID = u.userID AND u.userID = ?'
            'AND t.time like ?',
            (my_id[0], someday + '%'))
        whatifound = c.fetchall()
        if whatifound:
            print(whatifound[0][0] + ': ' + whatifound[0][1])
        else:
            print("You have no tasks at this date")


def switch_tasks(my_id):
    """Switches the date and time of the two tasks"""
    day1 = str(
        input("Please type the date of the first task in format yyyy-mm-dd: "))
    hour1 = str(
        input("Please type the time of the first task in 24-hour format: "))
    task1 = str(
        input("Please type the name of the first task "))
    time1 = day1 + ' ' + hour1
    firsttask = (my_id[0], time1, task1)
    print(firsttask)
    day2 = str(
        input("Please type the date of the second task in format yyyy-mm-dd: "))
    hour2 = str(
        input("Please type the time of the second task in 24-hour format: "))
    task2 = str(
        input("Please type the name of the second task "))
    time2 = day2 + ' ' + hour2
    secondtask = (my_id[0], time2, task2)
    print(secondtask)
    c.execute(
        "UPDATE tasks SET time = ? WHERE userID = ? AND time =? AND task =?",
        (time2, my_id[0], time1, task1))
    c.execute(
        "UPDATE tasks SET time = ? WHERE userID = ? AND time =? AND task =?",
        (time1, my_id[0], time2, task2))


def count_tasks(my_id):
    """Counts the specific tasks"""
    task = str(input("Please type task "))
    tasktuple = (task,)
    c.execute(
        'SELECT COUNT() FROM tasks t, users u WHERE t.userID = u.userID'
        'AND u.userID = ? AND t.task =?',
        (my_id[0], tasktuple[0]))
    whatifound = c.fetchall()
    print("You have " + str(whatifound[0][0]) + " tasks named: " + task)


def latest_task(my_id):
    """Shows the latest task"""
    c.execute(
        'SELECT t.time, t.task FROM tasks t, users u WHERE t.userID = u.userID'
        'AND t.time = (SELECT MAX(time) FROM tasks) AND u.userID = ?',
        my_id)
    whatifound = c.fetchall()
    print(whatifound)


def earliest_task(my_id):
    """Shows the earliest task"""

    c.execute(
        'SELECT t.time, t.task FROM tasks t, users u WHERE t.userID = u.userID '
        'AND t.time = (SELECT MIN(time) FROM tasks) AND u.userID = ?',
        my_id[0])
    whatifound = c.fetchall()
    print(whatifound)


def what_to_do():
    """Asks the user what they want to do"""
    ask_user = str(input("Type 'find' to find a task(s);\n"
                         "Type 'add' to add a new task;\n"
                         "Type 'del' to delete task(s);\n"
                         "Type 'show' to show tasks(s) of given year,month,"
                         " week,or date\n"
                         "Type 'switch' to switch two time of two tasks \n"
                         "Type 'count' to show how many tasks of given name"
                         "you have\n"
                         "Type 'latest' to show the latest task\n"
                         "Type 'earliest' to show the earliest task\n"))
    return ask_user


def main():
    """The main function of the scipt"""
    my_id = get_user_id()
    user_decision = what_to_do()


    if user_decision == 'find':
        find_task(my_id)
    elif user_decision == 'add':
        add_task(my_id)
    elif user_decision == 'del':
        del_task(my_id)
    elif user_decision == 'show':
        show_tasks(my_id)
    elif user_decision == 'switch':
        switch_tasks(my_id)
    elif user_decision == 'count':
        count_tasks(my_id)
    elif user_decision == 'latest':
        latest_task(my_id)
    elif user_decision == 'earliest':
        earliest_task(my_id)
    else:
        print('Ivalid operation')

    con.commit()
    con.close()

if __name__ == "__main__":
    main()
