import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(task_entry.get())
        if length <= 0:
            raise ValueError
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_display.config(state='normal')
        password_display.delete(0, tk.END)
        password_display.insert(0, password)
        password_display.config(state='readonly')
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_display.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350+100+200")
root.resizable(False, False)
root.configure(bg="#1B91DF")

title = tk.Label(root, text="Enter length of the password:", font=("Calibri", 12), bg="#7DA0D0", fg="white")
title.pack(pady=20)

task_entry = tk.Entry(root, width=10, font=("Consolas", 20), fg="black", justify='center')
task_entry.pack()

generate_btn = tk.Button(root, text="Generate password", font=("Arial", 12), bg="#1f6aa5", fg="white", command=generate_password)
generate_btn.pack(pady=15)

pwd_label = tk.Label(root, text="Generated password:", font=("Calibri", 12), bg="#153157", fg="white")
pwd_label.pack(pady=(10, 0))

password_display = tk.Entry(root, width=25, font=("Consolas", 16), justify='center', state='readonly')
password_display.pack(pady=5)

copy_btn = tk.Button(root, text="copy to clipboard", font=("Arial", 11), bg="#3dbd54", fg="white", command=copy_to_clipboard)
copy_btn.pack(pady=10)

root.mainloop()
