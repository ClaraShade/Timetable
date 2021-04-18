import sqlite3

import datetime

from datetime import datetime
from datetime import date

con = sqlite3.connect('mytimetable.db')
c = con.cursor()
myuserID = 1


def CountTasks():
    task = str(input("Please type task "))
    tasktuple = (task, )
    c.execute(
        'SELECT COUNT() FROM tasks t, users u WHERE t.userID = u.userID AND u.userID = ? AND t.task =?',
        (myuserID, tasktuple[0]))
    whatifound = c.fetchall()
    if whatifound:
        print("You have "+str(whatifound[0][0])+" tasks named: "+task)
    else:
        print("You have no tasks named "+task)

CountTasks()

con.commit()
con.close()