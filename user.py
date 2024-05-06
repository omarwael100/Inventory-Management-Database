import tkinter as tk
import sys
import subprocess


def execute_file1():
    subprocess.Popen([sys.executable, 'Search.py'])

      

root = tk.Tk()
root.title("User panel")

def set_button_style(button):
    button.config(bg="white", fg="black", width=20, height=2, relief="groove")

def label_style(label):
    label.config(font=("Arial", 12), pady=5)


button1 = tk.Button(root, text="Search for jobs data", command=execute_file1)
set_button_style(button1)
button1.pack(pady=200) 

 



root.configure(bg='white')  
root.geometry("900x600") 

root.mainloop()
