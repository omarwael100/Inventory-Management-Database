import tkinter as tk
import sys
import subprocess
from tkinter import simpledialog

def execute_file1():
    password = simpledialog.askstring("Password", "Enter password:", show='*')
    
    if password == "faris642003":  
        subprocess.Popen([sys.executable, 'menu_admin.py'])
    else:
        print("Incorrect password")

def execute_file2():
    subprocess.Popen([sys.executable, 'user.py'])

root = tk.Tk()
root.title("Inventory Accounting Application")

def set_button_style(button):
    button.config(bg="white", fg="black", width=20, height=2, relief="groove")

def label_style(label):
    label.config(font=("Arial", 12), pady=5)

button1 = tk.Button(root, text="ADMIN", command=execute_file1)
set_button_style(button1)
button1.pack(pady=100)  

button2 = tk.Button(root, text="USER", command=execute_file2)
set_button_style(button2)
button2.pack(pady=0)

root.configure(bg='white')  
root.geometry("900x600") 

root.mainloop()
