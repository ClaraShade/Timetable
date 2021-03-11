import sqlite3
import datetime
con = sqlite3.connect('harmonogram.db')
c = con.cursor()

def get_user_id():
    p = ('Wilczyca',)
    c.execute('SELECT user_id FROM users WHERE user_name = ?', p)
    my_id = c.fetchall()
    return my_id[0]

my_id = get_user_id()

def add():
    day = str(input("Please type day in format yyyy-mm-dd: "))
    hour = str(input("Please type hour in 24-hour format: "))
    task = str(input("Please type task "))
    mydate = (day + ' ' + hour)
    newid = my_id[0]
    c.execute('INSERT INTO tasks VALUES (?,?,?,?)', (1, newid, mydate, task))

add()

c.execute('SELECT t.task FROM tasks t, users u WHERE t.user_id = u.user_id AND u.user_id = ?', my_id)
whatifound = c.fetchall()
print(whatifound)

    #del_task()

#def del_task():
   #t = (1,)
   #c.execute('DELETE FROM tasks WHERE task_id = ?', a)
#del_task()

#user_input = input("Type 'a' to add a new task. \n"
                  # "Type 's' to show task(s) \n"
                   #"Type 'd' to delete task(s) \n"
                   #"Type 'c' to switch task(s) \n"
                  # "Type 'stop' to exit \n")


#add()
con.commit()
con.close()



