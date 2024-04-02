import tkinter as tk

# VARIABLES

CharacterCount = " "
Characters = " "
On_switch = " "
On_switch2 = " "

# LOGIC code

def show_values():
    global Characters
    print(w.get())
    Characters = str(w.get())
    print("Characters:", Characters)
    return Characters

def toggle_switch():
    global On_switch
    if toggle_var.get() == 1:
        print("Toggle switched on")
        # Add your code to record data when switch is on
        On_switch = True
    elif toggle_var.get() == 2:
        print("Toggle switched off")
        # Add your code to record data when switch is off
        On_switch = False

def toggle_switch2():
    global On_switch2
    if toggle_var2.get() == 1:
        print("Toggle2 switched on")
        # Add your code to record data when switch is on
        On_switch2 = True
    elif toggle_var2.get() == 2:
        print("Toggle2 switched off")
        # Add your code to record data when switch is off
        On_switch2 = False

# UI code
    
root = tk.Tk()
root.geometry("1000x600")
root.title("Password Generator")
root.resizable(height=None, width=None)
root.config(bg="gray")

CharacterCount = tk.Label(root, bg="gray", text="Number Of Characters", font=('Arial', 20,'bold'), fg="black")
CharacterCount.pack(pady=50)

w = tk.Scale(root, from_=12, to=32, orient=tk.HORIZONTAL, length=600, width=30)
w.pack()

Button1 = tk.Button(root, text='Show', command=show_values)
Button1.pack()

toggle_var = tk.IntVar()
toggle_button = tk.Checkbutton(root, text="Toggle 1", variable=toggle_var, command=toggle_switch)
toggle_button.pack(padx=10, pady=10)

toggle_var2 = tk.IntVar()
toggle_button2 = tk.Checkbutton(root, text="Toggle 2", variable=toggle_var2, command=toggle_switch2)
toggle_button2.pack(padx=10, pady=10)

def Check_toggle():
    if On_switch == True:
        print("switch is on")
    else:
        print("switch isnt on")

Check_toggle()

root.mainloop()
