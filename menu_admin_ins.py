import tkinter as tk
import sys
import subprocess


def execute_file1():
    subprocess.Popen([sys.executable, 'Direct_material_ins.py'])
def execute_file2():
    subprocess.Popen([sys.executable, 'Direct_labour_ins.py'])
    
def execute_file3():
    subprocess.Popen([sys.executable,'Actual_MOH_insert.py'])    
    
def execute_file4():
    subprocess.Popen([sys.executable,'COGS.COGM.py'])  
    
def execute_file5():
    subprocess.Popen([sys.executable,'Allocated_MOH.py'])    
      

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
button3 = tk.Button(root, text="Actul MOH", command=execute_file3)
set_button_style(button3)
button3.pack(pady=15)  

button4 = tk.Button(root, text="Cost of good sold", command=execute_file4)
set_button_style(button4)
button4.pack(pady=10)  

button5 = tk.Button(root, text="Allocated  MOH", command=execute_file5)
set_button_style(button5)
button5.pack(pady=5)  



root.configure(bg='white')  
root.geometry("900x600") 

root.mainloop()
