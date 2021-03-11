import sqlite3
import datetime
con = sqlite3.connect('harmonogram.db')
c = con.cursor()

def get_user_id():
    p = ('Wilczyca',)
    c.execute('SELECT user_id FROM users WHERE user_name = ?', p)
    my_id = c.fetchall()
    return my_id[0][0]
my_id = get_user_id()

def add():
    day = str(input("Please type day in format yyyy-mm-dd: "))
    hour = str(input("Please type hour in 24-hour format: "))
    task = str(input("Please type task "))
    mydate = (day + ' ' + hour)
    c.execute('INSERT INTO tasks VALUES (?,?,?,?)', (1, my_id, mydate, task))

def del_task():
    t = (1,)
    c.execute('DELETE FROM tasks WHERE task_id = ?', a)
#del_task()

#user_input = input("Type 'a' to add a new task. \n"
                  # "Type 's' to show task(s) \n"
                   #"Type 'd' to delete task(s) \n"
                   #"Type 'c' to switch task(s) \n"
                  # "Type 'stop' to exit \n")


#add()
print(my_id)
con.commit()
con.close()



