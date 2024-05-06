import tkinter as tk
import sys
import subprocess


def execute_file1():
    subprocess.Popen([sys.executable, 'Direct_material_update.py'])
def execute_file2():
    subprocess.Popen([sys.executable, 'Direct_labour_update.py'])
    
def execute_file3():
    subprocess.Popen([sys.executable,'Actual_MOH_update.py'])    
    
  
      

root = tk.Tk()
root.title("Execute Python Files")

def set_button_style(button):
    button.config(bg="white", fg="black", width=20, height=2, relief="groove")

def label_style(label):
    label.config(font=("Arial", 12), pady=5)


button1 = tk.Button(root, text="Direct material", command=execute_file1)
set_button_style(button1)
button1.pack(pady=25) 
button2 = tk.Button(root, text="Direct labour", command=execute_file2)
set_button_style(button2)
button2.pack(pady=20)  
button3 = tk.Button(root, text="Actual MOH", command=execute_file3)
set_button_style(button3)
button3.pack(pady=15)  




root.configure(bg='white')  
root.geometry("900x600") 

root.mainloop()
