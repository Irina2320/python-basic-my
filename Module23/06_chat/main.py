from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Radiobutton

users = [("Маша", 1), ("Аня", 2), ("Петя", 3), ("Ваня", 4)]
window = Tk()
window.title("Говночат на Python v_1.0.0")
user = IntVar()
message_history = ''
user_write = ''
input_data = None
new_window = None
sel = None


def select():
    global user_write
    global sel
    l = user.get()
    message = 'Печатает сообщение: ' + users[l-1][0]
    sel.config(text=message)
    user_write = users[l-1][0]

def message_window(message_history):
    txt = scrolledtext.ScrolledText(window, width=40, height=10)
    txt.grid(column=0, row=0)
    txt.configure(state='normal')
    txt.insert(INSERT, message_history)
    txt.configure(state='disabled')

message_window(message_history)

header = Label(text="Пользователи:", padx=15, pady=10)
header.grid(row=1, column=0, sticky=W)



def users_strind():
    global sel
    column=1
    for txt, val in users:
        Radiobutton(text=txt, value=val, variable=user, command=select) \
            .grid(row=1, column=column, sticky=W)
        column += 1

    sel = Label(padx=15, pady=10)
    sel.grid(row=2, sticky=W)


users_strind()


def clicked():
    global txt
    global message_history
    message_history += '\n' + user_write + ':  ' + txt.get()
    message_window(message_history)
    txt.delete(0, END)



def insert_text():
    lbl = Label(window, text="Новое сообщение:")
    lbl.grid(column=0, row=3)
    txt = Entry(window, width=50)
    txt.grid(column=0, row=4)
    txt.focus()
    btn = Button(window, text="Отправить!", command=clicked)
    btn.grid(column=0, row=5)

def append_new_user():
    global new_window
    global input_data
    new_user_name = input_data.get()
    new_user_index = len(users) + 1
    users.append((new_user_name, new_user_index))
    print(users)
    new_window.destroy()
    users_strind()




def new_user():
    global input_data
    global new_window
    new_window = Toplevel()
    new_window['bg'] = 'white'
    new_window.title("Регистрация нового пользователя")
    lbl = Label(new_window, text="Регистрация нового пользователя", padx=15, pady=10)
    lbl.grid(column=0, row=0)
    lbl = Label(new_window, text="Имя нового пользователя:")
    lbl.grid(column=0, row=1)
    input_data = Entry(new_window, width=50)
    input_data.grid(column=0, row=2)
    btn = Button(new_window, text="Добавить!", command=append_new_user)
    btn.grid(column=0, row=5)



lbl = Label(window, text="Новое сообщение:")
lbl.grid(column=0, row=3)
txt = Entry(window,width=50)
txt.grid(column=0, row=4)
txt.focus()
btn = Button(window, text="Отправить!", command=clicked)
btn.grid(column=0, row=5)

new_user_button = Button(window, text="Новый \nпользователь", command=new_user)
new_user_button.grid(column=1, row=0)


window.mainloop()