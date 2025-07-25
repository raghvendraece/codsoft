from tkinter import *
import pickle

def add_task():
    task = task_entry.get()
    if task:
        todo_list.append(task)
        list_box.insert(END, task)
        task_entry.delete(0, END)

def remove_task():
    selected_item = list_box.curselection()
    if selected_item:
        index = selected_item[0]
        list_box.delete(index)
        del todo_list[index]

def mark_done():
    selected_item = list_box.curselection()
    if selected_item:
        index = selected_item[0]
        item = list_box.get(index)
        if item.startswith("[✓] "):
            item = item[4:]
            list_box.delete(index)
            list_box.insert(index, item)
            list_box.itemconfig(index, fg="black")
            todo_list[index] = item
        else:
            item = "[✓] " + item
            list_box.delete(index)
            list_box.insert(index, item)
            list_box.itemconfig(index, fg="gray")
            todo_list[index] = item

def save_task():
    with open('todo_list.pkl', "wb") as f:
        pickle.dump(todo_list, f)

def load_task():
    global todo_list
    try:
        with open('todo_list.pkl', 'rb') as f:
            todo_list = pickle.load(f)
    except FileNotFoundError:
        todo_list = []

    list_box.delete(0, END)
    for item in todo_list:
        list_box.insert(END, item)
        if item.startswith("[✓] "):
            index = list_box.size() - 1
            list_box.itemconfig(index, fg="gray")

app = Tk()
app.title("To-Do List")
app.resizable(False, False)
app.geometry("720x480")
app.config(bg="#242424")
todo_list = []

# Main heading
title = Label(app, text="To-Do List", font=("consolas", 18, "bold"), bg="#242424", fg="#FFFFFF")
title.place(x=290, y=10)

# Input field
task_entry = Entry(app, width=34, font=("consolas", 12), fg="black")
task_entry.place(x=215, y=60)

# Buttons
add = Button(app, text="ADD", width=5, font=("consolas", 12), command=add_task)
add.place(x=205, y=110)

remove = Button(app, text="REMOVE", width=6, font=("consolas", 12), command=remove_task)
remove.place(x=450, y=110)

mark = Button(app, text="MARK", width=12, font=("consolas", 12), command=mark_done)
mark.place(x=300, y=130)

save = Button(app, text="SAVE", width=5, font=("consolas", 12), command=save_task)
save.place(x=205, y=170)

load = Button(app, text="LOAD", width=6, font=("consolas", 12), command=load_task)
load.place(x=450, y=170)

# Listbox to show tasks 
list_box = Listbox(app, height=15, width=65, font=("consolas", 12))
list_box.place(x=75, y=220)

app.mainloop()
