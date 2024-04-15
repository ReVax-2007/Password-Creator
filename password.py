import tkinter as tk
from tkinter import *
from tkinter import ttk
from PasswordLogic import PasswordLogic
from tkinter import Tk, PhotoImage



# VARIABLES
CharacterCount = " "
Characters = " "
On_switch = False
On_switch2 = False
Password = " "
Characters = 15

# LOGIC code
def show_values(value):
    global Characters
    Characters = str(int(round(float(value))))  # Ensure only full value numbers
    print("Characters:", Characters)
    CharacterCount.config(text="Number Of Characters: " + Characters)

def toggle_switch():
    global On_switch
    if toggle_var.get() == 1:
        print("Toggle switched on")
        include_numbers.config(borderwidth=5,relief=tk.SUNKEN)
        On_switch = True
    else:
        print("Toggle switched off")
        include_numbers.config(borderwidth=5,relief=tk.RAISED)
        On_switch = False

def toggle_switch2():
    global On_switch2
    if toggle_var2.get() == 1:
        print("Toggle2 switched on")
        include_symbols.config(borderwidth=5,relief=tk.SUNKEN)
        On_switch2 = True
    else:
        print("Toggle2 switched off")
        include_symbols.config(borderwidth=5,relief=tk.RAISED)
        On_switch2 = False

def gtc():
    root.clipboard_clear()
    root.clipboard_append(myPassword)

def update_tooltip_pos():
    x, y, _, _ = w.bbox("handle")
    val = round(w.get())
    tooltip.place(x=x, y=y-30)
    tooltip.configure(text=str(val))

def on_click_pg():
    global myPassword
    myPassword = PasswordLogic.generate(int(Characters), On_switch, On_switch2)
    password_var.set(myPassword)
    Output_Label.config(text=myPassword)
    print(f"The newly generated password is: {myPassword}")


# UI code

root = tk.Tk()
root.geometry("1000x600")
root.title("Password Generator")
root.config(bg="gray")
password_var = tk.StringVar()


CharacterCount = tk.Label(root, bg="gray", text="Number Of Characters: 12", font=('Arial', 20, 'bold'), fg="black")
CharacterCount.pack()

style = ttk.Style()
style.configure("Rounded.Horizontal.TScale", sliderthickness=20, troughcolor="light gray", background="gray", troughrelief="flat", sliderrelief="flat")

w = ttk.Scale(root, from_=12, to=52, orient=tk.HORIZONTAL, length=500, style="Rounded.Horizontal.TScale", command=show_values)
w.pack(pady=30)

tooltip = tk.Label(root, bg="white", fg="black", borderwidth=1, relief="solid")
tooltip.bind("<Motion>", lambda event: update_tooltip_pos())

Select = tk.Button(root, text='Select', command=lambda: show_values(w.get()), borderwidth=5, relief=RIDGE)
Select.pack(pady=(0,10))
toggle_var = tk.IntVar()
toggle_var.trace('w', lambda *args: toggle_switch())  
include_numbers = tk.Checkbutton(root, width=15, height=2, text="Include Numbers", variable=toggle_var, borderwidth=5, relief=tk.RAISED)
include_numbers.pack(padx=10, pady=5, side="left", anchor="nw")

toggle_var2 = tk.IntVar()
toggle_var2.trace('w', lambda *args: toggle_switch2())  
include_symbols = tk.Checkbutton(root, width=15, height=2, text="Include Symbols", variable=toggle_var2, borderwidth=5, relief=tk.RAISED)
include_symbols.pack(padx=10, pady=5, side="right", anchor="ne")

Generate_Button = tk.Button(root, borderwidth=10, relief=RIDGE, text="------ GENERATE  ------", command=lambda : on_click_pg(), font=('Arial', 20, 'bold'))
Generate_Button.pack(pady=10)

Output_Label = tk.Label(root, height=5, width=50, text=password_var, borderwidth=10, relief="raised", font=('Arial', 20, 'bold'))
Output_Label.pack(pady=(30,0))

Copy_Button = tk.Button(text='Copy Password', command=gtc, borderwidth=5, relief=RIDGE)
Copy_Button.pack(pady=10, side="right", anchor="n")

root.mainloop()
